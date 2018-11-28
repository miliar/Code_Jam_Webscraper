#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <utility>

using namespace std;

#define LOOP(i,a,b) for((i)=(a);(i)<(b);++(i))
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define SZ(v) ((int)((v).size()))
#define PB push_back
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;

int convert(char ch) {
    return((int)(ch-'A')); }

int main() {
    ios_base::sync_with_stdio(false);
    ofstream fout("b2.out");
    ifstream fin("b2.in");

    int t,c,d,n;
    string s;
    fin >> t;
    FOR(tt,t)
    {
        fin >> c;
        map<pair<int,int>,int> comb;
        FOR(i,c) {
            fin >> s;
            comb.insert(make_pair(make_pair(convert(s[0]),convert(s[1])),convert(s[2])));
            comb.insert(make_pair(make_pair(convert(s[1]),convert(s[0])),convert(s[2]))); }
        fin >> d;
        vvi opp(26);
        FOR(i,d) {
            fin >> s;
            opp[convert(s[0])].PB(convert(s[1]));
            opp[convert(s[1])].PB(convert(s[0])); }
        fin >> n;
        vi a(n);
        fin >> s;
        FOR(i,n) a[i] = convert(s[i]);

        vector<int> has(26,0);
        vector<int> res(n);
        int l=-1;
        FOR(i,n) {
            if((l>-1) && (comb.count(make_pair(res[l],a[i])))) {
                --has[res[l]];
                res[l] = comb.find(make_pair(res[l],a[i]))->second;
                continue; }
            bool clear=false;
            FOR(j,SZ(opp[a[i]])) if(has[ opp[ a[i] ][j] ]) {
                l=-1;
                FOR(j,26) has[j] = 0;
                clear=true;
                break; }
            if(clear) continue;
            ++l;
            res[l] = a[i];
            ++has[a[i]]; }

        fout << "Case #" << tt+1 << ": [";
        FOR(i,l) fout << ((char)(res[i]+((int)('A')))) << ", ";
        if(l>-1) fout << ((char)(res[l]+((int)('A'))));
        fout << "]\n";
    }

    fout.close();
    fin.close();
    return 0;
}
