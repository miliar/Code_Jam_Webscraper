#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back


int main()
{
	int L,D,N;
	cin >> L >> D >> N;
	vector <string> DIC(D);
	REP(i,D) cin >> DIC[i];
	string S; getline(cin,S);
	int tst = 1;
	while(N--)
	{
	   getline(cin,S);
	   int num = 0;
	   vector <string> Z = DIC;
	   int i = 0;
	   while(i < S.size())
	   {
	      if( S[i] == '(')
		  {
		    set <string> SE;
		    while( S[i] != ')')
			{
			  
		      if( S[i] >= 'a' && S[i] <= 'z')	
			  {
			     REP(j,Z.size())
				 {
				   if(Z[j][num] == S[i]) SE.insert(Z[j]);
				 }
			  }
			  
			  i++;
			}
			Z.clear();
			for(set<string>::iterator ii=SE.begin();ii!=SE.end();++ii)
			{
			  Z.PB(*ii);
			}
			num++;
		  }
		  else
		  {
		    if( S[i] >= 'a' && S[i] <= 'z')
		    {
			   vector <string> Z1;
			   REP(j,Z.size())
			   {
			     if(Z[j][num] == S[i]) Z1.PB(Z[j]);
			   }
			   Z = Z1;
			   num++;
			}
			i++;
		  }
	   
	   }
	   cout << "Case #" << tst << ": " <<  Z.size() << endl;
	   tst++;	
	}
	

	return 0;
}
