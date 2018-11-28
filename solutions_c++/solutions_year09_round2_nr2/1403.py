
#include<cstdio>
#include<iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>

using namespace std;
#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 
int t,c,n,lim,ans;

int cnt, b[505];
string s,temp;
string::iterator it;
int main()
{
	cin>>t;
	FOR(cas,0,t)
	{
		cin>>s;
		temp=s;
		sort(temp.begin(), temp.end());
		

        	cout<<"Case #"<<cas+1<<": ";
		if(!next_permutation(s.begin(), s.end()))
		{
//			cout<<s<<endl;
			//if(s==temp)
			it = s.begin();
			++it;       // it points now to number 2          
			s.insert (it,'0');   
			
		//	break;
		}
		while(s[0]=='0')
		{
			next_permutation(s.begin(), s.end());
		}
		cout<<s<<endl;
//       		cout<<s<<endl;
/*		ans=(double)(c+n)/(double)n;
 	printf("%0.7lf\n",ans);*/
		
		
	}
	return 0;
}

