#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf (1<<30)
#define clr(a,b) memset(a,b,sizeof(a))
#define pb push_back

string a;
set<char> st;

int flag[200],val[200];

int conv(char a)
{
	return val[a];
}
__int64 conv(__int64 b)
{
	__int64 s,i;
	s=0;
	for(i=0;i<a.size();i++)
	{
		s=s*b+conv(a[i]);
	}
	return s;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,t=1,i;
	__int64 r,mx;
	cin>>cs;
	while(cs--)
	{
		cin>>a;
		mx=0;
		st.clear();
		for(i=0;i<a.size();i++)
		{
			st.insert(a[i]);
		}
		mx=st.size();
		clr(val,0);
		clr(flag,0);
		val[a[0]]=1;
		flag[a[0]]=1;
		int k=0;
		for(i=1;i<a.size();i++)
		{
			if(flag[a[i]])
				continue;
			if(k==1)
				k++;
			val[a[i]]=k++;
			flag[a[i]]=1;
		}
		if(mx==1)
			mx=2;
		r=conv(mx);
		printf("Case #%d: %I64d\n",t++,r);
	}
	return 0;
}


