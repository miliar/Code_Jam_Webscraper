#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;

typedef long long LL;
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()


string WW ="welcome to code jam";
LL mod = 10000L;

int main()
{
   int tst;
   cin >> tst; string S;getline(cin,S);
   for(int cas=1;cas<=tst;cas++)
   {
      getline(cin,S);
	  vector <LL> T(S.size(),0);
	  vector < long double > W(S.size(), 0);
	  vector <int> L(S.size(), -1);
	  REP(i,S.size())
	  {
	    if(S[i] == WW[0]) { T[i]++; W[i]+=1.0; L[i] = 0; }
	  }
	  
	  for(int i=1;i<WW.size();i++)
	  {
	    REP(j,S.size())
		{
	       if( S[j] == WW[i] )
		   {
		     W[j] = 0.;
			 T[j] = 0L;
		     L[j] = i;
		     REP(k,j)
			 {
			   if( L[k] == i-1 )
			   {
			     T[j] += T[k];
				 T[j] %=mod;
		//	     W[j] += W[k];
	//			 if(W[j] > 10000000000.) W[j] = 10000000.;
			   }
			 
			 }
		   
		   }
		 
		}
		/*REP(i,S.size())
		{
		  cout << W[i] << " ";
		}
		cout << endl;*/
		
	  }
      // cas
	  LL wyn = 0L;
//	  long double cos = 0.0;
	  REP(i,S.size())
	  {
	    if( L[i] == WW.size()-1) 
		{
		  wyn += T[i];
	//	  cos += W[i];
		}
	  }
        wyn%=mod;
		string O;
		while( wyn > 0L )
		{
		  O += (char) ('0' + wyn%10L);
		  wyn/=10L;
		}
		while(O.size() < 4) O+="0";
		reverse(ALL(O));
		cout << "Case #" << cas <<": " << O << endl;
	//    printf("Case #%d: %lld\n", cas, wyn);

   }
   return 0;
}
