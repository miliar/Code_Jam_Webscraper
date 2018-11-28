#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
#define cin fin
#define cout fout

int main()
{
    int T, i, j;
    int ans;
    char Ri[100];
    vector<int> POi;
    vector<int> PBi;
    int pos[2] = {1,1}; //pos[0] : O, pos[1] : B
    //bool presionado = false;
    bool termino = false;
    bool siguiente = false;
    //int destino[2] = {0,0}; //destino[0] destino de O, dest..[1]... B

    cin >> T;
    for(i=0;i<T;i++){
        int N, p, Oidx, Bidx, Ridx;
        char r;

        cin >> N;
        for(j=0;j<N;j++){
            cin >> r;
            Ri[j] = r;
            cin >> p;
            if(r=='O')POi.push_back(p);
            if(r=='B')PBi.push_back(p);

            //if(destino[0] == 0 && r == 'O') destino[0] = p;
            //if(destino[1] == 0 && r == 'B') destino[1] = p;
        }
        j=0;
        Ridx = 0;
        Bidx = 0;
        Oidx = 0;
        termino = false;

        while(true){
            termino = true;
            siguiente = false;
            if(Oidx < POi.size()){

                termino = false;
                if(Ri[Ridx] == 'O' && POi[Oidx] == pos[0]){Oidx++; siguiente = true;} // O presiona
                else if(POi[Oidx] > pos[0]){pos[0]++;} // O avanza
                else if(POi[Oidx] < pos[0]){pos[0]--;} // O retrocede
            }

            if(Bidx < PBi.size()){

                termino = false;
                if(Ri[Ridx] == 'B' && PBi[Bidx] == pos[1]){Bidx++; siguiente = true;} // B presiona
                else if(PBi[Bidx] > pos[1]){pos[1]++;} // B avanza
                else if(PBi[Bidx] < pos[1]){pos[1]--;} // B retrocede
            }
            if(termino==true) break;
            if(siguiente==true) Ridx++;
            j++;
        }
        ans = j;
        cout << "Case #" << i+1 << ": " << ans << endl;
        PBi.clear();
        POi.clear();
        pos[0] = 1;
        pos[1] = 1;
    }

    return 0;
}
