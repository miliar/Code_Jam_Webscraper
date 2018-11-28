#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

#define LOOP(i,a,b) for((i)=(a);(i)<(b);++(i))
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define SZ(v) ((int)((v).size()))
#define PB push_back
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;

int main() {
    ios_base::sync_with_stdio(false);
    ofstream fout("b.out");
    ifstream fin("b.in");

    int t;
    fin >> t;
    FOR(tt,t)
    {
        int n,m,w;
        fin >> n >> m >> w;
        vector< vector<int> > ws(n,vector<int>(m));
        FOR(i,n) FOR(j,m) {
            char ch;
            fin >> ch;
            ws[i][j] = w+(int)(ch-'0'); }

        int res = 0;
        for(int k=min(n,m); k>=3; --k)
        {
            if(res) break;
            for(int i=0; i<=n-k; ++i)
            {
                if(res) break;
                for(int j=0; j<=m-k; ++j)
                {
                    if(res) break;
                    bool ok = true;
                    int cur = 0;
                    int leverage = -(k-1);
                    for(int di = 0; di<k; ++di) {
                        for(int dj=0; dj<k; ++dj) if(!(((di==0)||(di==k-1))&&((dj==0)||(dj==k-1)))) cur += leverage*ws[i+di][j+dj];
                        leverage += 2; }
                    if(cur) ok = false;
                    if(ok) {
                        cur = 0;
                        int leverage = -(k-1);
                        for(int dj = 0; dj<k; ++dj) {
                            for(int di=0; di<k; ++di) if(!(((di==0)||(di==k-1))&&((dj==0)||(dj==k-1)))) cur += leverage*ws[i+di][j+dj];
                            leverage += 2; }
                        if(cur) ok = false; }
                    if(ok) res = k;
                }
            }
        }

        if(res) fout << "Case #" << tt+1 << ": " << res << '\n';
        else fout << "Case #" << tt+1 << ": IMPOSSIBLE\n";
    }

    fout.close();
    fin.close();
    return 0;
}
