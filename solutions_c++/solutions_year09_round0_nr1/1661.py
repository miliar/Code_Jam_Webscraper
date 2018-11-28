#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define N 1000
char a[300][30], b[1000], t[100][30];
int l, d, n, top, num[N];
void solve()
{
	int i, j, ans, k, p, len, r, found, flag;
	for(i=0;i<d;i++)
		scanf("%s",a[i]);
	for(i=1;i<=n;i++)
	{
		scanf("%s",b);
		len=strlen(b);
		memset(num,0,sizeof(num));
		top=0;
		for(j=0;j<len;j++)
		{
			if(b[j]=='(')
			{
				for(k=j+1;k<len;k++)
				{
					if(b[k]==')')
						break;
				}
				for(p=j+1;p<k;p++)
				{
					t[top][num[top]]=b[p];
					num[top]++;
				}
				j=k;
			}
			else if(b[j]!=')')
			{
				t[top][0]=b[j];
				num[top]++;
			}
			top++;
		}
		ans=0;
		for(k=0;k<d;k++)
		{
			found=1;
			len=strlen(a[k]);
			for(j=0;j<len;j++)
			{
				flag=0;
				for(r=0;r<num[j];r++)
				{
					if(a[k][j]==t[j][r])
					{
						flag=1;
						break;
					}
				}
				if(flag==0)
				{
					/*printf("%d %d\n",k,j);
					printf("%c \n",a[k][j]);
					for(int ss=0;ss<num[j];ss++)
						printf("%c",t[j][ss]);
					printf("\n");*/
					found=0;
					break;
				}
			}
			if(found)
			{
				ans++;
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
}
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
    freopen("asmall.out","w",stdout);
	while(scanf("%d%d%d",&l,&d,&n)==3)
	{
		solve();
	}
	return 0;
}

