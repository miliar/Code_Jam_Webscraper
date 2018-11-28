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
    ofstream fout("d2.out");
    ifstream fin("d2.in");

    int t,n;
    fin >> t;
    FOR(tt,t) {
        int res=0;
        fin >> n;
        vi a(n);
        FOR(i,n) fin >> a[i];
        vi b = a;
        sort(b.begin(),b.end());
        FOR(i,n) if(a[i]!=b[i]) ++res;
        fout << "Case #" << tt+1 << ": " << res << ".000000\n"; }

    fout.close();
    fin.close();
    return 0;
}
