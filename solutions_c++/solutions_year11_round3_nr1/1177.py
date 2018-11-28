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
#define rep(i,n) for(int i=0;i<(int)n;i++)
#define repc(p) for(int i=0;p[i]!='\0';i++)
#define repl(i,s,e) for(int i=s;i<e;i++)
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
	int t,r,c,flag=0,cnt_c=0;
	char n[100][100];
	cin>>t;
	while(t--)
	{
		cin>>r>>c;
		flag=0;
		cnt_c++;
		rep(i,r)
			rep(j,c)
			cin>>n[i][j];
		rep(i,r-1)
		{
			rep(j,c-1)
			{
				if(n[i][j]=='#' && n[i][j+1]=='#' && n[i+1][j]=='#' && n[i+1][j+1]=='#')
				{
					n[i][j]='/';
					n[i+1][j]='\\';
					n[i+1][j+1]='/';
					n[i][j+1]='\\';

				}
				else if(n[i][j]=='.' || n[i][j]=='/' || n[i][j]=='\\')
				{
				}
				else
				{
					flag=1;
					break;
				}
			}
			if(flag==1)
				break;
		}
		rep(i,r)
			if(n[i][c-1]=='#')
				flag=1;
		rep(i,c)
			if(n[r-1][i]=='#')
				flag=1;
		cout<<"Case #"<<cnt_c<<":"<<endl;
		if(flag==1)
		{
			cout<<"Impossible\n";

		}
		else
		{
			rep(i,r)
			{
				rep(j,c)
					cout<<n[i][j];
				cout<<endl;
			}
		}
	}
	return 0;
}
