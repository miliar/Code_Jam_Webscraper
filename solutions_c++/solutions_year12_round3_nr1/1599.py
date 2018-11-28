#include <iostream>
#include <fstream>
#include <vector>

#define nmax 55

using namespace std;

ifstream f("a.in");
ofstream g("a.out");

int n, viz[nmax];
vector<int> gf[nmax];
int rez;
int t;
void df(int nod, int fin){

    viz[nod] = 1;
    //if (rez == 2)
    for(int i=0; i<gf[nod].size(); i++){
        if (gf[nod][i] == fin) ++rez;
        if (rez >= 2) return;
        if (viz[gf[nod][i]] == 0){
            df(gf[nod][i], fin);
        }
    }

}

int main(){

    f >> t;
    for(int w=1; w<=t; w++){
        f >> n;
        g << "Case #" << w << ": ";
        for(int i=0; i<=n; i++) gf[i].clear();
        for(int i=1; i<=n; i++){
            int cate, x;
            f >> cate;
            for(int j=1; j<=cate; j++){
                f >> x;
                gf[i].push_back(x);
            }
        }
        int ok = 1;
        for(int i=1; i<=n && ok; i++){
            for(int j=1; j<=n && ok; j++){
                for(int k=0; k<nmax; k++) viz[k] = 0;
                rez = 0;
                df(i,j);
                //if (rez >= 2) cout << i << " "  << j << " " << w << "\n", ok = 0;
                if (rez >= 2) g << "Yes" << "\n", ok = 0;
            }
        }
        if (ok == 1) g << "No" << "\n";
    }

    f.close();
    g.close();

    return 0;

}
