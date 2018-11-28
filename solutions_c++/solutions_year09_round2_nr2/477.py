#include<iostream>
#include<algorithm>
#include<string>
#include<vector>

#include<cmath>
#include<cstdio>
#include<queue>
#include<list>
#include<stack>
#include<utility>
#include<numeric>
#include<map>
#include<cctype>
#include<cstring>
#include<sstream>

using namespace std;

#define F(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)

#define s scanf
#define p printf

#define ALL(x) x.begin(), x.end()

#define INF 1000000000

int main()
{
	string str,tmp;
	int t;
	s("%d",&t);
	F(tc,t)
	{
		cin>>str;
		tmp=str;
		next_permutation(ALL(str));
		if(str>tmp)
			cout<<"Case #"<<tc+1<<": "<<str<<endl;
		else
		{
			str='0'+tmp;
			next_permutation(ALL(str));
			cout<<"Case #"<<tc+1<<": "<<str<<endl;
		}
	}
	return 0;
}
