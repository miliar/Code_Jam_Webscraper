#include<string>
#include<iostream>
#include<cstring>
using namespace std;
string dict[5001];
string s;
char f[30][30];
int t[30];
int l,d,n,ans;
bool flag;
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	scanf("%d %d %d\n",&l,&d,&n);
	for (int i=1;i<=d;i++)
		cin>>dict[i];
	for (int casenum=1;casenum<=n;casenum++)
	{
		cin>>s;
		memset(t,0,sizeof(t));
		for (int i=1;i<=l;i++)
		{
			if (s[t[0]]!='(')
			{
				t[i]=1;
				f[i][1]=s[t[0]];
				t[0]++;
			}
			else
			{
				t[0]++;
				while (s[t[0]]!=')')
				{
					t[i]++;
					f[i][t[i]]=s[t[0]];
					t[0]++;
				}
				t[0]++;
			}
		}
		ans=0;
		for (int i=1;i<=d;i++)
		{
			for (int j=1;j<=l;j++)
			{
				flag=false;
				for (int k=1;k<=t[j];k++)
					if (f[j][k]==dict[i][j-1])
					{
						flag=true;
						break;
					}
				if (!flag) break;
			}
			if (flag) ans++;
		}
		printf("Case #%d: %d\n",casenum,ans);
	}
	return 0;
}
