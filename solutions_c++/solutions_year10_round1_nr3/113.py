#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int Test,Case,A1,A2,B1,B2,L[1000005],R[1000005];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	double P=(sqrt(5)+1)/2;
	for (int i=1;i<=1000000;i++) {
		L[i]=int(i/P)+1;
		R[i]=int(i*P);
	}
	for (scanf("%d",&Test);Test;--Test) {
		scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
		long long Ret=(long long)(B2-B1+1)*(A2-A1+1);
		for (int i=A1;i<=A2;i++) {
			int LL=max(L[i],B1);
			int RR=min(R[i],B2);
			Ret-=max(RR-LL+1,0);
		}
		printf("Case #%d: %I64d\n",++Case,Ret);
	}
	return 0;
}
