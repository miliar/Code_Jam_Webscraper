#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
using namespace std;
int A,B;
int calc(int n)
{
	char s[20]={};
	int ans=0;
	itoa(n,s,10);
	while(1)
	{
		rotate(s,s+1,s+strlen(s));
		//printf("%s\n",s);
		int k=atoi(s);
		if(k==n)return ans;
		if(k<=B && k > n)ans++;
	}
}
int main()
{
	int T,w=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&A,&B);
		printf("Case #%d: ",w++);
		int ans=0;
		for(int i=A;i<=B;i++)
			ans+=calc(i);
		printf("%d\n",ans);
	}
}
