#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)

ifstream fin("I://fin.txt");
ofstream fout("I://out.txt");

void solve(){
   int n;
   vector <double> wp,owp,oowp,rpi,tot,won,lost;
   vector <string> games;

   fin >> n;
   games.resize(n);
   wp.resize(n);
   owp=oowp=tot=won=lost=wp;


   REP(i,n){
	   fin >> games[i];
   }

   //wp;
   REP(i,n){
	   won[i]=lost[i]=0;
	   REP(j,n){
		   if(games[i][j]=='1')won[i]++;
		   if(games[i][j]=='0')lost[i]++;
	   }
	   wp[i] = won[i] / (won[i]+lost[i]);
	   tot[i]=won[i]+lost[i];
   }
   
   REP(i,n){
	   owp[i]=0;
	   REP(j,n){
		   if(games[i][j]=='1')owp[i]+=won[j]/(tot[j]-1);
		   if(games[i][j]=='0')owp[i]+=(won[j]-1)/(tot[j]-1);
	   }
	   owp[i]/=tot[i];
   }
   REP(i,n){
	   oowp[i]=0;
	   REP(j,n){
		   if(games[i][j]!='.')oowp[i]+=owp[j];
	   }
	   oowp[i]/=tot[i];
   }

   REP(i,n){
	   fout << (0.25 * wp[i] + 0.5 * owp[i] + 0.25*oowp[i]) << endl;
   }
}


int main(int argc, char *argv[])
{
    int t;

    fin >> t;
	

    REP(i,t){
cout << i+1 << " / " << t << "..." << endl;
        fout << "Case #" << i+1 << ": " << endl;
        solve();
        fout << endl;
    }
    
    fin.close();
    fout.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}