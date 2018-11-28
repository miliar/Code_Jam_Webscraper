#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <math.h>
#include <memory.h>
#include <set>
#include <vector>
#include <map>
#include <sstream>
#include <queue>

using namespace std;

ifstream fin("A-small-attempt1.in");
ofstream fout("A-small.out");

#define ll long long
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))

int N, Pd, Pg;
int main() {
    int T;
    fin>>T;
    for(int k = 1;k<=T;++k) {
        fin>>N>>Pd>>Pg;
        bool possible = false;
        for(int i = 1;i<=N;++i) {
            int p = Pd*i;
            if(p%100 || p/100>i) continue;
            int s = i*(Pg-Pd);
            for(int j = 0;j<=100000;++j) {
                if(Pg*j+s>=0 && (Pg*j+s)%100 == 0 && (Pg*j+s)/100<=j) {
                    possible = true;
                    break;
                }
            }
            if(possible) break;
        }
        fout<<"Case #"<<k<<": ";
        if(possible) fout<<"Possible"<<endl;
        else fout<<"Broken"<<endl;
    }
    system("pause");
    return 0;
}
