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

long long lnko(long long a, long long b)
{
    if(b) return lnko(b,a%b);
    return a;
}

long long lkkt(long long a, long long b)
{
    return ((a/lnko(a,b))*b);
}

int main() {
    ios_base::sync_with_stdio(false);
    ofstream fout("c.out");
    ifstream fin("c.in");

    int t;
    fin >> t;
    FOR(tt,t)
    {
        int n;
        long long min,max;
        fin >> n >> min >> max;
        vector<long long> a(n);
        FOR(i,n) fin >> a[i];
        sort(a.begin(),a.end());

        vi d(n+1,0);
        for(int i=n-1; i>=0; --i) d[i] = lnko(a[i],d[i+1]);
        vi m(n+1,1);
        FOR(i,n) m[i+1] = lkkt(a[i],m[i]);

        bool ok=false;
        long long res = -1;
        for(long long i=min; i<=max; ++i) {
            if(ok) break;
            FOR(j,n+1) if((!(i%m[j])) && (!(d[j]%i))) {
                res = i;
                ok = true;
                break; } }

        fout << "Case #" << tt+1 << ": ";
        if(ok) fout << res << '\n';
        else fout << "NO\n";
    }

    fout.close();
    fin.close();
    return 0;
}
