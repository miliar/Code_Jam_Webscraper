#include <stdio.h>
#include <algorithm>
using namespace std;
int N;
int A[800];
int B[800];
int recur(int a,int s)
{
	if (a>=N) return 0;
	int b,m,v=1,t;
	for (b=0;b<N;b++)
		if ( !(s&(1<<b)) )
		{
			t=recur(a+1,s|(1<<b))+A[a]*B[b];
			if (v || m>t) { v=0;m=t; }	
		}
	return m;
}
int solve()
{
	return recur(0,0);
}
typedef long long ll;
ll solve2()
{
	sort(A,A+N);
	sort(B,B+N);
	int q;
	ll s=0;
	for (q=0;q<N;q++)
		s+=((ll)A[q])*((ll)B[N-q-1]);
	return s;
}
int main()
{
	int t,T;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		int q;
		scanf("%d",&N);
		for (q=0;q<N;q++) scanf("%d",A+q);
		for (q=0;q<N;q++) scanf("%d",B+q);
		printf("Case #%d: %lld\n",t,solve2());
	}
	
	return 0;
}
