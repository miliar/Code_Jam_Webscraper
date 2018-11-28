#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <string>
using namespace std;

#define MOD 1000000007
/*
for i = 0 to n-1
  print A[i mod m]
  A[i mod m] = (X * A[i mod m] + Y * (i + 1)) mod Z
  */

ifstream fin("in.in");
ofstream fout("out.out");
unsigned long long i,j,n,m,T,X,Y,Z;
/*    -----> fool... haven't read statement carefuly... :(
string add(string A, string B) {
       int i,ost;
       list<char> ret;
       while (A.size() < B.size()) A.insert(A.begin(),'0');
       while (A.size() > B.size()) B.insert(B.begin(),'0');
       ost = 0;
       for (i=A.size()-1;i>=0;i--) {
           ret.insert(ret.begin(), (A[i]+B[i]-2*'0'+ost)%10 + '0');
           ost = (A[i]+B[i]-2*'0'+ost)/10;
           }
       if (ost) ret.insert(ret.begin(),'1');
       string RET; 
       RET.resize(ret.size()); i=0;
       for (list<char>::iterator it=ret.begin();it!=ret.end();it++)
           RET[i++] = *it;
       return RET;
       }
*/ 
int main() {
    fin >> T;
    for (int t=1;t<=T;t++) {
        cout << "Solving Case #" << t << "..." << endl;
        vector<unsigned long long> work,in;
        vector<unsigned long long> dp;
        fin >> n >> m >> X >> Y >> Z;
        for (i=0;i<m;i++) work.push_back( (fin>>j)?j:0 );
        for (i=0;i<n;i++) { in.push_back( work[i%m] ); work[i%m] = (X * work[i%m] + Y * (i+1)) % Z; }
        /*
        cout << "Generated: ";
        for (i=0;i<n;i++) cout << in[i] << " "; cout << endl;
        */
        
        dp.resize(n);
        fill(dp.begin(),dp.end(),1);
        for (i=0;i<n;i++) 
            for (j=i+1;j<n;j++) 
                if (in[j] > in[i]) dp[j] = ( dp[j] + dp[i] ) % MOD;
        
        /*
        cout << "dp[]: ";
        for (i=0;i<n;i++) cout << dp[i] << " ";
        cout << endl;
        */
        int SOL(0);
        for (i=0;i<n;i++) SOL = ( SOL + dp[i] ) % MOD;
        fout << "Case #" << t << ": " << SOL << endl;
        }
    system("pause");
}
