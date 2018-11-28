#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int Test,N,K,A[205][205],TA[205],B[205][205],TB[205];

inline void XXX(int T[],int N)
{
	for (int i=1,j=1;i<2*N;i++) {
		T[i]=j;
		if (i<N) ++j;
			else --j;
	}
}

inline bool Check()
{
	for (int i=1;i<2*N;i++)
	for (int j=1;j<=TB[i];j++)
	if (B[i][j]!=-1) {
		if (B[i][j]!=B[i][TB[i]-j+1] && B[i][TB[i]-j+1]>=0) return false;
		if (B[i][j]!=B[2*N-i][j] && B[2*N-i][j]>=0) return false;
	}
	return true;
}

inline bool Check(int R)
{
	if (R<K) return false;
	XXX(TB,N=R);
	for (int i=1;i<=N;i++)
	for (int j=1;j<=TB[i];j++) {
		memset(B,-1,sizeof(B));
		bool Flag=true;
		for (int u=1,k=j;u<2*K && Flag;u++) {
			if (k<=0) Flag=false;
			for (int v=1;v<=TA[u] && Flag;v++) {
				B[i+u-1][k+v-1]=A[u][v];
				if (i+u-1>=2*N || k+v-1>TB[i+u-1]) Flag=false;
			}
			if (u<K && i+u-1>=N) --k;
			if (u>=K && i+u-1<N) ++k;
		}
		if (Flag && Check()) return true;
	}
	return false;
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	scanf("%d",&Test);
	for (int Case=1;Case<=Test;Case++) {
		scanf("%d",&K);
		XXX(TA,K);
		for (int i=1;i<2*K;i++)
		for (int j=1;j<=TA[i];j++)
			scanf("%d",&A[i][j]);
		Check(3);
		int L,R;
		for (L=0,R=52;L+1<R;) {
			int M=(L+R)>>1;
			if (Check(2*M-1)) R=M;
				else L=M;
		}
		int Ret=2*R-1;
		for (L=0,R=52;L+1<R;) {
			int M=(L+R)>>1;
			if (Check(2*M)) R=M;
				else L=M;
		}
		Ret<?=2*R;
		printf("Case #%d: %d\n",Case,Ret*Ret-K*K);
	}
	return 0;
}
