#include <iostream>

#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> TIV;
typedef vector<short> TSV;

typedef vector<long long> TLV;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int numCases = 0;
    in >> numCases;

    for(int c = 0; c < numCases; c++) {
        long long N = 0;
        long long L = 0;
        long long H = 0;

        in >> N;
        in >> L;
        in >> H;

        TLV others;
        long long I = 0;

        for(long long i = 0; i < N; i++){
            in >> I;
            others.push_back(I);
        }

        long long note = L;

        bool inharmony = false;
        for(; note <= H; note++) {
            bool harmony = true;
            TLV::iterator it = others.begin();
            for(;it!=others.end();++it){
                if(*it % note != 0 && note % *it != 0){
                    harmony = false;
                    break;
                }
            }

            if(harmony){
                inharmony = true;
                break;
            }
        }

        out << "Case #" << c + 1 << ": ";
        if(inharmony){
            out << note;
        }
        else {
            out << "NO";
        }
        out << endl;
    }

    in.close();
    out.close();
    return 0;
}
