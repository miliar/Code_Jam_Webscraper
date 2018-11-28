#include<iostream>
using namespace std;
#include<set>
char s[5009][19];
char ss[5000];
int main()
{
	int l,d,n,j,k,i;
	freopen("out.txt","w",stdout);
	freopen("A-small-attempt0.in","r",stdin);
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++)
	{
		scanf("%s",&s[i]);
	}
	for(j=0;j<n;j++)
	{
		set<char> mm[40];
		scanf("%s",ss);
		int nn=strlen(ss);
		k=0;
		int last=0;
		int brac=0;
		for(i=0;i<nn;i++)
		{
			if(ss[i]==')')
			{
				k++;
				brac=0;
			}
			else if(ss[i]!='(')
			{
				if(brac==0)
				{
					if(i>0&&ss[i-1]!='('&&ss[i-1]!=')')
						k++;
				}
				mm[k].insert(ss[i]);
			}
			else
			{
				brac=1;
			}
		}
		int cnt=0;
		for(i=0;i<d;i++)
		{
			for(k=0;k<l;k++)
				if(mm[k].find(s[i][k])==mm[k].end())
					break;
			if(k>=l)
				cnt++;
		}
		printf("Case #%d: %d\n",j+1,cnt);
	}
}
