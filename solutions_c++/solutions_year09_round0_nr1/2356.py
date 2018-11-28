#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;

char store[5010][20];
char str[10000];
int num[20][30];

int main()
{
	int l,d,n,ii,i,j,len,flg,ll,var,cc;

	//freopen("A-large.in","r",stdin);
	//freopen("A-out.txt","w",stdout);

	while(scanf("%d %d %d",&l,&d,&n)==3)
	{
		for(ii=0;ii<d;ii++)
		{
			scanf("%s",&store[ii]);
		}
		for(ii=0;ii<n;ii++)
		{
			scanf("%s",&str);
			len=strlen(str);
			for(i=0;i<=15;i++)
			{
				for(j=0;j<=26;j++)
				{
					num[i][j]=0;
				}
			}
			flg=0;
			ll=0;
			for(i=0;i<len;i++)
			{
				if(str[i]=='(') flg=1;
				else if(str[i]==')') 
				{
					flg=0;
					ll++;
				}
				else
				{
					if(flg==0)
					{
						var=int(str[i]-'a');
						num[ll][var]=1;
						ll++;
					}
					else
					{
						var=int(str[i]-'a');
						num[ll][var]=1;
					}
				}
			}
			cc=0;
			for(i=0;i<d;i++)
			{
				flg=0;
				for(j=0;j<l;j++)
				{
					var=int(store[i][j]-'a');
					if(num[j][var]!=1)
					{
						flg=1;
						break;
					}
				}
				if(flg==0) cc++;
			}
			printf("Case #%d: %d\n",(ii+1),cc);
		}
	}
	return 0;
}