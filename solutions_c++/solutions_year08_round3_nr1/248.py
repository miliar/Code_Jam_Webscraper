#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	long long int N,P,K,L,k,t;
	vector<long long int> A;
	freopen("A-small.in","r",stdin);
	freopen("out.in","w",stdout);
	scanf("%lld",&N);
	for(int z=0;z<N;z++)
	{
		A.clear();
		k=0;
		scanf("%lld%lld%lld",&P,&K,&L);
		for(int i=0;i<L;i++)
		{
			scanf("%lld",&t);
			A.push_back(t);
		}
		if(L>(P*K))
		{
			printf("Case #%d: Impossible\n",z+1);
			break;
		}
		for(int i=0;i<(L-1);i++)
		{
			for(int j=0;j<(L-i-1);j++)
			{
				if(A[j]<A[j+1])
				{
					t=A[j];
					A[j]=A[j+1];
					A[j+1]=t;
				}
			}
		}
		
		for(int i=0;i<L;i++)
		{
			k+=((int)(i/K)+1)*A[i];
		}
		printf("Case #%d: %lld\n",z+1,k);
	}
		
	return 0;
}
