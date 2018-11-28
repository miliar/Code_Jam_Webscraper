#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
using namespace std;
int t,c,d,n;
bool dd[10][10];
char cc[10][10],s[200],ch;

int main()
{
	map<char,int> mp;
	mp['Q']=1;mp['W']=2;mp['E']=3;mp['R']=4;
	mp['A']=5;mp['S']=6;mp['D']=7;mp['F']=8;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for (int tt=1;tt<=t;tt++)
	{
		memset(cc,0,sizeof(cc));
		memset(dd,false,sizeof(dd));
		scanf("%d",&c);
		for (int i=1;i<=c;i++)
		{
			scanf("%s",s);
			cc[mp[s[0]]][mp[s[1]]]=s[2];
			cc[mp[s[1]]][mp[s[0]]]=s[2];
		}
		scanf("%d",&d);
		for (int i=1;i<=d;i++)
		{
			scanf("%s",s);
			dd[mp[s[0]]][mp[s[1]]]=true;
			dd[mp[s[1]]][mp[s[0]]]=true;
		}
		int l=0;
		memset(s,0,sizeof(s));
		scanf("%d ",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%c",&ch);
			if (l==0)
			{
				s[l]=ch;
				l++;
			}
			else
			{
				while (cc[mp[ch]][mp[s[l-1]]]!=0)
				{
					ch=cc[mp[ch]][mp[s[l-1]]];
					s[l-1]=0;
					l--;
					if (l==0) break;
				}
				s[l]=ch;
				l++;
				for (int i=0;i<l;i++)
					if (dd[mp[s[i]]][mp[s[l-1]]])
					{
						while (l>0)
						{
							l--;
							s[l]=0;
						}
					}
			}
		}
		printf("Case #%d: [",tt);
		if (l>0) printf("%c",s[0]);
		for (int i=1;i<l;i++)
			printf(", %c",s[i]);
		printf("]\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}