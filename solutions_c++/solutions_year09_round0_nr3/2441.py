#include<cstdio>
#include<cstring>

char a[1000];
char t[1000];
int d[101][100];
char s[100]="welcome to code jam";
int n;
int l;

int main()
{
	gets(t);
	freopen(t,"r",stdin);
	scanf("%d\n",&n);
	freopen("output.txt","w",stdout);
	for(int i=0;i<n;i++)
	{
		gets(a);
		l=strlen(a);
		d[0][0]=a[0]==s[0];
		for(int j=1;j<l;j++)
		{
			d[0][j]=d[0][j-1];
			if(s[0]==a[j]) d[0][j]++;
		}
		for(int j=1;j<19;j++)
		{
			for(int k=j;k<l;k++)
			{
				d[j][k]=d[j][k-1];
				if(s[j]==a[k]) d[j][k]+=d[j-1][k-1];
			}
		}
		printf("Case #%d: %04d\n",i+1,d[18][l-1]);
	}
}