#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;

int ma[1002][101];
string s[101];

int mini(int m,int id,int k)
{
	int cont=1<<20;
	for(int i=0;i<m;i++)
		if(i!=k)
			cont=min(cont,ma[id][i]);
	return cont;
}

int main()
{
	int n,m,r;
	char c;
	string t;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		scanf("%d",&m);
		scanf("%c",&c);
		for(int k=0;k<m;k++)
		{
			s[k]="";
			for(int j=0;j<101;j++)
			{
				scanf("%c",&c);
				if(c!='\n')
				{
					s[k]+=c;
				}else
				{
					break;
				}
			}
		}
		for(int k=0;k<m;k++)
			ma[0][k]=0;
		scanf("%d",&r);
		scanf("%c",&c);
		for(int k=0;k<r;k++)
		{
			t="";
			for(int j=0;j<101;j++)
			{
				scanf("%c",&c);
				if(c!='\n')
				{
					t+=c;
				}else
				{
					break;
				}
			}
			for(int j=0;j<m;j++)
			{
				if(t==s[j])
				{
					ma[k+1][j]=mini(m,k,j)+1;
				}else
					ma[k+1][j]=ma[k][j];
			}
		}
		int res=1<<20;
		for(int j=0;j<m;j++)
		{
			res=min(res,ma[r][j]);
		}
		printf("Case #%d: %d\n",i+1,res);
	}
}