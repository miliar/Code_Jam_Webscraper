#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
int TT;
int A1,A2,B1,B2;
map<pair<int,int> , int > PD;
int calc(int A, int B) {
	pair<int,int> par=make_pair(A,B);

	if(PD.find(par) != PD.end())
		return PD[par];
	if(B<=0)
		return PD[par]=1;

	PD[par]=0;

	for(int i=0;i<2;i++) {
		for(int k=A/B+2;k>=1;k--) {
			int a=A-k*B;
			if(calc(max(a,B),min(a,B)) == 0)
				return PD[par]=1;
		}
		swap(A,B);
	}

	return PD[par];
}
int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		scanf("%d %d %d %d",&A1,&A2,&B1,&B2);
		int ans=0;
		PD.clear();
		for(int i=A1;i<=A2;i++)
			for(int j=B1;j<=B2;j++) {
				if( calc(max(i,j),min(i,j)) )
					ans++;
			}
		printf("Case #%d: %d\n",T,ans);

	}
	return 0;
}
