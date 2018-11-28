#include<cstdio>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;
bool end;
char s[200],c1[40][3],c2[40][2],an[200];
bool check(int a,int b,int aa,int bb)
{
	if((a==aa&&b==bb)||(a==bb&&b==aa))return 1;
	else return 0;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,c,d,n,i,j,k,top,z=0;
	scanf("%d",&t);
	while(t--)
	{
		z++;
		scanf("%d",&c);
			for(i=0;i<c;i++)scanf("%s",&c1[i]);
		scanf("%d",&d);
			for(i=0;i<d;i++)scanf("%s",&c2[i]);
		scanf("%d",&n);
		scanf("%s",&s);
		top=0;
		for(i=0;i<strlen(s);i++)
		{
			an[top++]=s[i];
			end=0;
			while(!end)
			{
				end=1;
				for(j=0;j<c;j++)
					if(top>1)
						if(check(an[top-1],an[top-2],c1[j][0],c1[j][1]))
						{
							an[top-2]=c1[j][2];
							top--;
							end=0;
							break;
						}
			}
			for(j=0;j<d;j++)
				if(top>1)
				{
					for(k=0;k<top-1;k++)
					if(check(an[top-1],an[k],c2[j][0],c2[j][1]))
					{
						top=0;
						break;
					}
				}
		}
		printf("Case #%d: [",z);
		for(i=0;i<top;i++)
		{
			if(i==0)printf("%c",an[i]);
			else printf(", %c",an[i]);
		}
		printf("]\n");
		
	}
}
