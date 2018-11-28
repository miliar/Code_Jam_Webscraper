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
    ofstream fout("b2.out");
    ifstream fin("b2.in");

    int t;
    fin >> t;
    FOR(tt,t)
    {
        int n,c,l;
        long long tm;
        fin >> l >> tm >> n >> c;
        tm*=2;
        vector<long long> distNext(n);
        FOR(i,c) fin >> distNext[i];
        for(int i=c; i<n; ++i) distNext[i] = distNext[i-c];

        long long res = 0;
        FOR(i,n) {
            if(res + (distNext[i]*4) < tm) {
                res += distNext[i]*4;
            } else {
                int timeSlow = max(min(4*distNext[i],tm-res),0LL);
                int timeFast = (4*distNext[i] - timeSlow) / 2;
                res += timeSlow;
                vector<long long> rem;
                rem.PB(timeFast);
                for(int j=i+1; j<n; ++j) rem.PB(distNext[j]*2);
                sort(rem.rbegin(),rem.rend());
                for(int j=0; j<min(SZ(rem),l); ++j) res+=rem[j];
                for(int j=min(SZ(rem),l); j<SZ(rem); ++j) res+=rem[j]*2;
                break;
            }
        }


        fout << "Case #" << tt+1 << ": " << (res/2) << '\n';
        cerr << tt+1 << " done!\n";
    }

    fout.close();
    fin.close();
    return 0;
}
