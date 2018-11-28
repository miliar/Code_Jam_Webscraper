
#include<iostream>
#include<vector>
#include<set>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<queue>
#include<stack>
#include<stdlib.h>
#include<cmath>
#include<map>
#include<list>
#include<deque>
#include<sstream>
#include<climits>
using namespace std;
#define rep(i,n) for(long i=0;i<(long)n;i++)
#define repc(p) for(long i=0;p[i]!='\0';i++)
#define repl(i,s,e) for(long i=s;i<=e;i++)
#define pb push_back
#define si(name,value) name.insert(value)
#define bn begin()
#define mp(a,b) make_pair(a,b)
#define ed end()
#define itint(name) set<int>::iterator name
#define itch(name) set<char>::iterator name
#define itstr(name) set<string>::iterator name
#define mp3(a,b,c) mp(a,mp(b,c))
#define mp4(a,b,c,d) mp(mp(a,b),mp(c,d))
int main()
{
	long t,n,l,h,flag=0,cnt_c=0,ans;
	long c[100000];
	cin>>t;
	while(t--)
	{
		cin>>n>>l>>h;
		flag=0;
		ans=-1;
		cnt_c++;
		rep(i,n)
			cin>>c[i];
		repl(i,l,h)
		{
			flag=0;
			for(int j=0;j<n;j++)
			{
//				cout<<i<<" "<<c[j]<<endl;
				if(c[j]%i==0 || i%c[j]==0)
				{
					flag=0;
				}
				else
				{
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				ans=i;
				break;
			}
		}
		
		cout<<"Case #"<<cnt_c<<": ";
		if(ans==-1)
		{
			cout<<"NO";

		}
		else
		{
			cout<<ans;
		}
		cout<<endl;
	}
	return 0;
}
