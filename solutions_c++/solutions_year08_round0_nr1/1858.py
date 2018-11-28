#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
using namespace std;

const int MaxS = 101;
const int MaxQ = 1001;

typedef string TSEngArr[MaxS + 1];
typedef string TQuerArr[MaxQ + 1];


void Trucate(TQuerArr &Queries, TSEngArr &SEngines, int SEng, int &Quer) {
        for (int i = 2; i <= Quer; i++)
                if (Queries[i-1]==Queries[i]){
                        for(int u = i; u < Quer; u++)
                                Queries[u] = Queries[u+1];
                        Quer--;
                }
}

int MaxSwitches(TSEngArr &SEngines, TQuerArr &Queries, int SEng, int Quer) {
        int Switcher[MaxQ+1][MaxS+1];
        int tmp;
        for(int i = 1; i <= SEng; i++)
                if(SEngines[i] != Queries[Quer])
                        Switcher[Quer][i] = 0;
                else
                        Switcher[Quer][i] = 1;
        for(int i = Quer-1; i >= 1; i--) {
                copy(Switcher[i+1]+1, Switcher[i+1]+SEng+1, Switcher[i]+1);
                for(int o = 1; o <= SEng; o++)
                        if(SEngines[o] == Queries[i]) {
                                tmp = o;
                                break;
                        }
                Switcher[i][tmp] = 30000;
                Switcher[i][tmp] = *min_element(Switcher[i]+1, Switcher[i]+SEng+1)+1;
        }
        return *min_element(Switcher[1]+1, Switcher[1]+SEng+1);
}

int main () {
        // Get initial data
        int N;
        TSEngArr SEngines;
        TQuerArr Queries;
        ifstream fin("uni.in");
        ofstream fout("uni.out");
        fin >> N;
        for (int i = 1; i <= N; i++) {
                int SEng, Quer;
                char c[101];
                fin >> SEng;
                fin.getline(c, 100);
                for(int u = 1; u <= SEng; u++) {
                        fin.getline(c, 100);
                        SEngines[u] = c;
                }
                fin >> Quer;
                fin.getline(c, 100);
                for(int u = 1; u <= Quer; u++) {
                        fin.getline(c, 100);
                        Queries[u] = c;
                }
                Trucate(Queries, SEngines, SEng, Quer);
                fout << "Case #" << i << ": " << MaxSwitches(SEngines, Queries, SEng, Quer) << endl;
        }
        fin.close();
        fout.close();
        return 0;
}
