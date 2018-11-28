#include <stdio.h>
#include <string>
#include <set>
using namespace std;

int l,d,n;
string strs[5000];
char s[1000];
set<char> cans[20];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	//
	scanf("%d%d%d",&l,&d,&n);
	for(int i=0;i<d;i++)
	{
		scanf("%s",s);
		strs[i]=s;
	}
	for(int i=0;i<n;i++)
	{
		scanf("%s",s);
		int t=0;
		for(int j=0;j<l;j++)
		{
			cans[j].clear();
			if(s[t]=='(')
			{
				for(t++;(s[t]>='a')&&(s[t]<='z');t++)
					cans[j].insert(s[t]);
				t++;
			}
			else
				cans[j].insert(s[t++]);
		}
		int rez=0;
		for(int j=0;j<d;j++)
		{
			bool p=true;
			for(int t=0;t<l;t++)
				if(cans[t].find(strs[j][t])==cans[t].end())
				{
					p=false;
					break;
				}
			if(p)
				rez++;
		}
		printf("Case #%d: %d\n",i+1,rez);
	}
	//
	return 0;
}