#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <complex>
#include <cmath>
#include <vector>
#include <list>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <set>
#include <map>
#include <ctime>
using namespace std;
int T,casenum,i,x,y,xp,yp,cur,n,anum,bnum,ans;
char ch;
int a[200],b[200],f[200];
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case "<<"#"<<casenum<<": ";
		cin>>n;
		anum=bnum=0;
		for (i=1;i<=n;i++)
		{
			cin>>ch;
			if (ch=='O')
			{
				f[i]=0;
				anum++;
				cin>>a[anum];
			}
			else
			{
				f[i]=1;
				bnum++;
				cin>>b[bnum];
			}
		}
		ans=0;x=y=1;xp=1;yp=1;cur=1;
		while (1)
		{
			ans++;
			if (f[cur]==0)
			{
				if (yp<=bnum&&y<b[yp]) y++;
				else if (yp<=bnum&&y>b[yp]) y--;
				if (x==a[xp])
				{
					cur++;
					xp++;
				}
				else
				{
					if (x<a[xp]) x++;
					else x--;
				}
			}
			else
			{
				if (xp<=anum&&x<a[xp]) x++;
				else if (xp<=anum&&x>a[xp]) x--;
				if (y==b[yp])
				{
					cur++;
					yp++;
				}
				else
				{
					if (y<b[yp]) y++;
					else y--;
				}
			}
			if (cur>n) break;
		}
		cout<<ans<<endl;
	}
	return 0;
}
