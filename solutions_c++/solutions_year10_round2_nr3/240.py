#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<queue>
#include<set>
#include<algorithm>
#include<sstream>
#include<cmath>
#include<cstdlib>
#include<deque>
#include<list>
#include<stack>
using namespace std;

#define INF 0x7fffffff
#define PI acos(-1.0)
#define EPS (1e-10)
#define SZ(a) int((a).size())

#define M 100003

typedef long long LL;

int gcd(int a,int b){return b>0?gcd(b,a%b):a;}

int t[505][505],f[505]={1};

int main()
{
	//freopen("C:\\Users\\LL\\Desktop\\GCJ\\1.in","r",stdin);
	//freopen("C:\\Users\\LL\\Desktop\\GCJ\\1.out","w",stdout);

	int i,j,k;
	for(i=0;i<=500;i++)
		t[i][0]=1;
	for(i=1;i<=500;i++)
	{
		t[i][0]=t[i][1]=1;
		for(j=2;j<=500;j++)
		{
			t[i][j]=t[i][j-1];
			for(k=2;k<=i&&k<=j;k++)
			{
				t[i][j]+=t[i][j-k];
				t[i][j]%=M;
			}
		}
	}
	for(i=1;i<=500;i++)
	{
		f[i]=1;
		for(j=1;j<=i;j++)
		{
			f[i]=(f[i]+t[j][i+1-j])%M;
		}
	}
	int csNum,cs;
	scanf("%d",&csNum);
	for(cs=1;cs<=csNum;cs++)
	{
		int n;
		scanf("%d",&n);
		printf("Case #%d: ",cs);
		printf("%d\n",f[n-2]);
	}
}