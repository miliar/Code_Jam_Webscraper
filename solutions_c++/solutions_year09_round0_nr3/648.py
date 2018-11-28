#include <cstdio>
#include <string>

int n;
char a[]="welcome to code jam";
char str[1000];

int d[512][32];

void process(int nCase)
{
	gets(str);
	memset(d,0,sizeof(d));
	int al=strlen(a);
	int len=strlen(str);
	int sum=0;
	for (int i=0;i<len;i++)
	{
		if (str[i]==a[0])
		{
			sum++;
		}
		d[i][0]=sum;
	}
	for (int i=1;i<al;i++)
	{
		int ts=0;
		for (int j=i;j<len;j++)
		{
			if(str[j]==a[i]){
				ts+=d[j][i-1];
			}
			ts%=10000;
			d[j][i]=ts;
		}
	}
	printf("Case #%d: %04d\n",nCase,d[len-1][al-1]);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&n);
	gets(str);
	for (int i=1;i<=n;i++)
	{
		process(i);
	}
	return 0;
}