#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;
#define inf 10000000
int Case,Test;
int A1,A2,B1,B2;
const double g=(sqrt((double)5)-(double)1)/(double)2+1;

inline void Readin()
{
	scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
}

inline void Solve()
{
	long long Ans=0;
	for (int i=A1;i<=A2;++i)
	{
		int L=int(i*g)+1,R=B2;
		
		L>?=B1;
		Ans+=max(0,R-L+1);
	}
	for (int i=B1;i<=B2;++i)
	{
		int L=int(i*g)+1,R=A2;
		
		L>?=A1;
		Ans+=max(0,R-L+1);
	}
	
	printf("%I64d\n",Ans);
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
