#include <cstdio>
#include <algorithm>
#include <vector>
#define LLD long long int
#define MOD 1000000007
using namespace std;

int main()
{
	int lw;
	scanf("%d",&lw);
	vector<LLD> T;
	vector<LLD> A;
	LLD X;
	for (int L=1;L<=lw;L++)
	{
		LLD n,m,x,y,z;
		scanf("%lld%lld%lld%lld%lld",&n,&m,&x,&y,&z);
		A.clear();
		T.clear();
		for (int i=0;i<m;i++)
		{
			scanf("%lld",&X);
			T.push_back(X);
		}
		for (int i=0;i<n;i++)
		{
			A.push_back(T[i%m]);
			T[i%m] = (x * T[i % m] + y * (i + 1)) % z;
		}
		T.clear();
		for (int i=0;i<n;i++)
			T.push_back(A[i]);
		sort(T.begin(),T.end());
		for (int i=0;i<n;i++)
			A[i] = lower_bound(T.begin(),T.end(),A[i])-T.begin();
		LLD All = 0;
		for (int i=0;i<n;i++)
			T[i] = 0;
		for (int i=0;i<n;i++)
		{
			LLD Temp = 0;
			for (int j=0;j<A[i];j++)
			{
				Temp += T[j];
				Temp %= MOD;
			}
			Temp++;
			All += Temp;
			All %= MOD;
			T[ A[i] ] += Temp;
			T[ A[i] ] %= MOD;
		}
		printf("Case #%d: %lld\n",L,All);
	}
	T.clear();
	A.clear();

	return 0;
}
