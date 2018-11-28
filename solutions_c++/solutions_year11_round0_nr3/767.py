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
    ofstream fout("c2.out");
    ifstream fin("c2.in");

    int t,n,a;
    fin >> t;
    FOR(tt,t) {
        int xsum=0,sum=0,min=1234567;
        fin >> n;
        FOR(i,n) {
            fin >> a;
            xsum ^= a;
            sum += a;
            if(min>a) min = a; }
        fout << "Case #" << tt+1 << ": ";
        if(xsum) {
            fout << "NO\n";
        } else {
            fout << sum-min << '\n';
        } }

    fout.close();
    fin.close();
    return 0;
}
