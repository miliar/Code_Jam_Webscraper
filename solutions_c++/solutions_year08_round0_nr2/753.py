#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

typedef struct train_t{
    int tini, tfin;
    string hini, hfin;
    char station; // A, B
    bool ok, reserved;

    train_t(){
        station = 0;
        tini = tfin = 0;
        ok = reserved = false;
    }

    train_t(char st, string histr, string hfstr, int hi, int mi, int hf, int mf){
        station = st;
        hini = histr;
        hfin = hfstr;
        tini = hi * 60 + mi;
        tfin = hf * 60 + mf;
        ok = reserved = false;
    }
} train;

int main()
{
    ifstream entrada("B-large.in");
    ofstream saida("B-large.out");
    vector<train> trains;

    int ncases;

    entrada >> ncases;

    for (int ccase = 1; ccase <= ncases; ccase++){
        int timeout;
        int na, nb;
        int ta = 0, tb = 0; // Total of trains needed

        entrada >> timeout >> na >> nb;

        string inih, finh;
        int hi, mi, hf, mf;
        istringstream conv;

        for (int i = 0; i < na; i++){
            entrada >> inih >> finh;

            conv.str(inih.substr(0, 2)); conv >> hi; conv.clear();
            conv.str(inih.substr(3, 2)); conv >> mi; conv.clear();
            conv.str(finh.substr(0, 2)); conv >> hf; conv.clear();
            conv.str(finh.substr(3, 2)); conv >> mf; conv.clear();

            trains.push_back(train('A', inih, finh, hi, mi, hf, mf));
        }

        for (int i = 0; i < nb; i++){
            entrada >> inih >> finh;

            conv.str(inih.substr(0, 2)); conv >> hi; conv.clear();
            conv.str(inih.substr(3, 2)); conv >> mi; conv.clear();
            conv.str(finh.substr(0, 2)); conv >> hf; conv.clear();
            conv.str(finh.substr(3, 2)); conv >> mf; conv.clear();

            trains.push_back(train('B', inih, finh, hi, mi, hf, mf));
        }

        // hey ho, let's go

        //cout << "CASO "  << ccase;
        for (int i = 0; i < trains.size(); i++){
            int mintime = 1500; // the max is 24 * 60 = 1440
            int maxtime = 0;
            int pos = -1;

            // First/next train
            for (int j = 0; j < trains.size(); j++){
                if ((!trains[j].ok) && (trains[j].tini < mintime)){
                    mintime = trains[j].tini;
                    pos = j;
                }
            }

            //cout << "trem: estacao " << trains[pos].station << ", " << trains[pos].hini << " - " << trains[pos].hfin << endl;

            bool found = false;
            int posreserved = -1;
            for (int j = 0; j < trains.size(); j++){
                if ((j != pos) && (trains[j].station != trains[pos].station) && (!trains[j].reserved)
                    && (trains[j].tfin > maxtime) && (trains[j].tfin + timeout <= trains[pos].tini)){
                    posreserved = j;
                    found = true;
                }
            }

            if (found){
                //cout << "    conexao com trem da estacao " << trains[pos].station << ", " << trains[pos].hini << " - " << trains[pos].hfin << endl;
                trains[posreserved].reserved = true;
            }else{
                if (trains[pos].station == 'A') ta++; else tb++;
                //cout << "    solicitar novo trem para estacao " << trains[pos].station << ", num total de " << (trains[pos].station == 'A'? ta: tb) << endl;
            }

            trains[pos].ok = true;
        }

        saida << "Case #" << ccase << ": " << ta << " " << tb;
        if (ccase < ncases)
            saida << endl;
        trains.clear();
    }

    saida.close();
    entrada.close();
    return 0;
}
