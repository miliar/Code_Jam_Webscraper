#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
const int MAXN=40+10;
const int MAXC=2*3*5*7+10;
char s[MAXN];
long long dp[MAXN][MAXC];
int mod(int a,int b,int x)
{
	int i;
	int p=0;
	for(i=a;i<=b;i++)
	{
		p*=10;
		p+=s[i]-'0';
		p%=x;
	}
	return p;
}
long long count(int x)
{
	int i,j,n=strlen(s);
	/*for(i=0;i<x;i++)
		dp[0][i]=mod(0,0,x);*/
	int k,e;
	for(i=0;i<n;i++)
		for(j=0;j<x;j++)
		{
			dp[i][j]=0;
			for(k=0;k<=i;k++)
			{
				e=mod(k,i,x);
				if(k)
				{
					dp[i][j]+=dp[k-1][((j-e)%x+x)%x];
					dp[i][j]+=dp[k-1][(e+j)%x];
				}
				else dp[i][j]+=((e==j)?1:0);
			}
		}
	return dp[n-1][0];
}
int d[]={2,3,5,7};
int bc[16];
void solution(int num)
{
	scanf("%s",s);
	int i,j;
	bc[0]=0;
	long long res=0;
	for(i=1;i<16;i++)
	{
		int e=1;
		bc[i]=bc[i/2]+(i&1);
		for(j=0;j<4;j++)
			if((i>>j)&1) e*=d[j];
		res+=((bc[i]&1)?1:-1)*count(e);
	}
	printf("Case #%d: ",num);
	cout<<res<<endl;
	fprintf(stderr,"%d\n",num);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d",&n);
	int i;
	for(i=0;i<n;i++)
		solution(i+1);
	return 0;
}
	
