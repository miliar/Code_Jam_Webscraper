#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
int a[10],n;
char temp[1200];
void rever(char s[])
{
	int i,j;
	for(i=0;s[i];i+=n)
	{
		char tt[10];
		for(j=0;j<n;j++)
			tt[j]=s[i+a[j]];
		for(j=0;j<n;j++)
			s[i+j]=tt[j];
	}
}
int cal(char s[])
{
	int cnt = 0;
	for(int i=0;s[i];i++)
	{
		if(i==0 || s[i] != s[i-1]) cnt++;
	}
	return cnt;
}
int main()
{
	freopen("D-small.in","r",stdin);
	freopen("D-small.out","w",stdout);
	//freopen("D-large.in","r",stdin);
	//freopen("D-large.out","w",stdout);
	int t,i;
	char str[1200];
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		scanf("%d",&n);
		scanf("%s",&str);
		printf("Case #%d: ",c);
		for(i=0;i<n;i++)
			a[i]=i;
		int min=100000000;
		do
		{
			strcpy(temp,str);
			rever(temp);
			int val = cal(temp);
			if(val<min) min = val;
		}while(next_permutation(a,a+n));
		printf("%d\n",min);
	}
	return 0;
}