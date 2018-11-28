#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

#define FOR(i) for(int i = 0;  i< 3; ++i)
typedef  long long int Int;
int DK[1000001];
int NX[1000001];
int PV[1000001];
char buf[10000];

int ntr(int nc){
	gets(buf);
	int k; sscanf(buf,"%d",&k);
	for(int j = 1; j < k; ++j)NX[j]=j+1, PV[j+1]=j; NX[k] = 1; PV[1] = k;
	int p = k;
	for(int i = 1; i <= k; ++i){
		for( int j = 0; j<i; ++j ){ p = NX[p]; }
		DK[p] = i;
		NX[PV[p]]=NX[p];
		PV[NX[p]]=PV[p];
		p = PV[p];
	}
	printf( "Case #%d:", nc);
	int n; scanf("%d",&n);
	for(int j = 0; j < n; ++j){
		int x; scanf(" %d",&x);
		printf(" %d",DK[x]);
	}
	printf("\n");
	gets(buf);
	return 0;
}



int main(){
	freopen("Cin.txt","r",stdin);
	freopen("Cout.txt","w",stdout);

	int N;
	gets(buf); sscanf(buf,"%d", &N);

	for(int nc = 1; nc <= N; ++nc){
		int r = ntr(nc);
		//printf( "Case #%d: %lld\n", nc, r);
	}
}
