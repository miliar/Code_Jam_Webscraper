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

int main()
{
    ios_base::sync_with_stdio(false);
    ofstream fout("c.out");
    ifstream fin("c.in");

    int t;
    fin >> t;
    FOR(tt,t)
    {
        int n;
        fin >> n;
        int min=1,max=1;
        if(n>1)
        {
            vector<bool> prime(n+1,true);
            prime[0] = prime[1] = false;
            ++max;
            FOR(i,n) {
                if(prime[i]) {
                    ++min;
                    for(int j=i*2; j<=n; j+=i) prime[j] = false;
                    int j=i;
                    while(j<=n) {
                        j*=i;
                        ++max; } } }
        }

        fout << "Case #" << tt+1 << ": " << max-min << '\n';
    }

    fout.close();
    fin.close();
    return 0;
}
