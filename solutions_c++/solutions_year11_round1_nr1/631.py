#include<cstdio>
#include<string>

using namespace std;

int memo[101][100];

bool solve(long long int& n,int& pd,int& pg)
{
	if(pd!=100&&pg==100)return false;
	if(pd!=0&&pg==0)return false;
	if(n>=100)return true;
	for(int i=1;i<=n;i++)
	{
		if(i*pd%100==0)return true;
	}
	return false;
}

int main()
{
	int t,pd,pg;
	long long int n;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%lld %d %d",&n,&pd,&pg);
		printf("Case #%d: ",i+1);
		if(solve(n,pd,pg))
		{
			printf("Possible\n");
		}else{
			printf("Broken\n");
		}
	}
	return 0;
}
