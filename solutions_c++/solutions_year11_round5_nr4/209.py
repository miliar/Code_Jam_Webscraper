#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <cassert>
#include <cmath>
#include <algorithm>
typedef long long LL; 
using namespace std;
 
#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define REP(k,a) for(int k=0; k < (a); ++k)

bool isS(LL a)
{
	if(a==1LL)
		return true;
	LL tmp=1LL<<30;
	LL root=0;
	while(tmp)
	if((root+tmp)*(root+tmp)>a)
	{
		tmp/=2;
	}
	else
	{
		root+=tmp;
		tmp/=2;
	}
	return(root*root==a);
}

int main()
{
	int testCaseCounter;
	cin >> testCaseCounter;
	for(int actTestCase=1;actTestCase<=testCaseCounter;++actTestCase)
	{
		string tmp;
		cin>> tmp;
		vector<int> v;
		LL c=0;
		int n=tmp.size();
		REP(i,n)
		{
			if(tmp[i]=='?')
			{	
				v.push_back(n-i-1);
				tmp[i]='0';
			}
			c<<=1;
			c+=tmp[i]-'0';
		}	
		LL c2=c;
		REP(i,(1<<v.size()))
		{
			c2=c;
			FOR(j,0,v.size())
			 if((1LL<<j)&i)
				 c2|=(1LL<<v[j]);
			if(isS(c2))
			{	
				//cout << "found" << endl;
				break;
			}
		}
		//cout << c2 << endl;
		cout << "Case #" << actTestCase << ": ";
		bool start=false;
		for(int i=63;i>-1;--i)
		{
			int dig=0;
			if(1LL<<i & c2)
			{	
				start=true;
				dig=1;
				
			}	
			if(start)
				cout<< dig ;
		}
		
		cout << endl;
	}
	return 0;
}
