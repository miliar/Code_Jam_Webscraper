#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

#define FOR(i) for(int i = 0;  i< 3; ++i)
typedef  long long int Int;
Int NT[3][3];
char buf[10000];
#define MX 20000
int ndt[MX], ndg[MX], ndv[MX], ndc[MX], M, V;

typedef pair<int,int> par;
typedef pair<par,par> ops;


par tscan(int nd){
	par r;
	if( ndt[nd] ==  0){
		r.first = (ndv[nd]==0? 0:-1);
		r.second = (ndv[nd]==1?0:-1);
	} else {
		par r1 = tscan(2*nd);
		par r2 = tscan(2*nd+1);
		par ror, rand;
		ror.first = (r1.first == -1 || r2.first == -1) ? -1 : r1.first+r2.first;
		ror.second = r1.second == -1 && r2.second == -1 ? -1 :
			(r1.second == -1 ? r2.second : (r2.second==-1 ? r1.second : min(r1.second,r2.second)));
		rand.second = (r1.second == -1 || r2.second == -1) ? -1 : r1.second+r2.second;
		rand.first = r1.first == -1 && r2.first == -1 ? -1 :
			(r1.first == -1 ? r2.first : (r2.first==-1 ? r1.first : min(r1.first,r2.first)));
		r = ndg[nd]==1?rand:ror;
		if( ndc[nd] == 1 && ndg[nd] == 0 ){
			if(rand.first !=-1 &&( r.first == -1 ||  rand.first+1 < r.first)) r.first = rand.first + 1;
			if(rand.second !=-1 && (r.second == -1 || rand.second+1 < r.second))r.second = rand.second + 1;
		} else if( ndc[nd] == 1 && ndg[nd] == 1 ){
			if(ror.first !=-1 && (r.first == -1 || ror.first+1 < r.first))r.first = ror.first + 1;
			if(ror.second !=-1 &&(r.second == -1 || ror.second+1 < r.second))r.second = ror.second + 1;
		}
	}
	return r;
}

int nch(){
	int j;
	scanf( " %d %d", &M, &V);
	for(j = 1; j <= (M-1)/2; ++j){
		ndt[j] = 1; ndv[j] = -1;
		scanf("%d %d",&ndg[j],&ndc[j]);
	}
	for(; j<=M; ++j){
		ndt[j] = 0; ndg[j]; ndc[j] = 0;
		scanf("%d",&ndv[j]);
	}
	par r = tscan(1);
	return V==1 ? r.second : r.first;
}

int main(){
	freopen("Ain.txt","r",stdin);
	freopen("Aout.txt","w",stdout);

	int N;
	gets(buf); sscanf(buf,"%d", &N);

	for(int nc = 1; nc <= N; ++nc){
		fprintf(stderr,"%d / %d ",nc,N);
		int r = nch();
		if( r == -1 )
			printf( "Case #%d: IMPOSSIBLE\n", nc);
		else
			printf( "Case #%d: %d\n", nc,r);

	}
}
