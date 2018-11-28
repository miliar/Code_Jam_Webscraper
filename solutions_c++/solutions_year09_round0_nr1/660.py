#include<iostream>
using namespace std;
char s[5000][20];
char a[100000];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-largeout.txt","w",stdout);
	int zu;
	int m,n;
	scanf("%d%d%d",&m,&n,&zu);
	for(int i=0;i<n;i++)scanf("%s",s[i]);
	for(int ca=1;ca<=zu;ca++)
	{
		printf("Case #%d: ",ca);
		int num=0;
		scanf("%s",a);
		for(int ii=0;ii<n;ii++)
		{
			char *b=s[ii];
			int p=0;
			bool f=1;
			for(int i=0;i<m;i++)
			{
				if(a[p]=='(')
				{
					bool fff=0;
					for(p++;a[p]!=')';p++)
						if(a[p]==b[i])
							fff=1;
					if(!fff){f=0;break;}
					p++;
				}
				else
				{
					if(a[p]!=b[i]){f=0;break;}
					p++;
				}
			}
			num+=f;
		}
		printf("%d\n",num);
	}
}
