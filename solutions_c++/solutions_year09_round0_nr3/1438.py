#include <iostream>
#include <string>
#include <fstream>
using namespace std;

#define LL long
#define MAX 505
#define MOD 10000
string in;
string pat("welcome to code jam");
LL t,T;
ifstream fin("C.in");
ofstream fout("C.out");

LL f(string &in) {
   LL n = pat.size(), m = in.size();
   LL dp[n][m];
   LL i,j;
   memset(dp, 0, sizeof dp);
   
   dp[0][0] = in[0] == pat[0];
   for (i=1;i<m;i++) dp[0][i] = (pat[0] == in[i]);
   
   for (i=1;i<n;i++) {
       LL sum(0);
       for (j=0;j<m;j++) {
           sum = ( sum + dp[i-1][j] ) % MOD;
           if (in[j] != pat[i]) continue;
           dp[i][j] = ( dp[i][j] + sum ) % MOD; 
           }
       }
   
   LL ret(0);
   for (i=0;i<m;i++) ret = ( ret + dp[n-1][i] ) % MOD;
   return ret;
   }

string format(LL sol) {
       LL g = 0;
       string ret;
       if (sol < 1000) g++;
       if (sol < 100) g++;
       if (sol < 10) g++;
       for (LL i=0;i<g;i++) ret += '0';
       return ret;
       }

int main() {
    fin >> T;
    getline(fin,in);
    for (t=0;t<T;t++) {
        cout << "Case #" << t + 1 << endl;
        getline(fin,in);
        LL out = f(in);
        fout << "Case #" << t + 1 << ": " << format(out) << out << endl;
        }
    cout << "Done!" << endl;
    system("pause");
}
