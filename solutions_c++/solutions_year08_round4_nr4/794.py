#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

#define FOR(i) for(int i = 0;  i< 3; ++i)
typedef  long long int Int;
Int NT[3][3];
char buf[10000],buf2[10000];
#define MX 20000
int ndt[MX], ndg[MX], ndv[MX], ndc[MX], M, V;

typedef pair<int,int> par;
typedef pair<par,par> ops;
int p[20];

int clen(int k){
	int nc=0,t=0;
	char lch = 0;
	for(char *c=buf; *c; c+=k){
		for(int j = 0; j <k; ++j,++t){
			buf2[t]=c[p[j]];
			if( c[p[j]] != lch){
				lch = c[p[j]];
				nc++;
			}
		}
	}
	return nc;
}
int RLE(){
	int k;
	gets(buf); sscanf(buf,"%d",&k);
	gets(buf);
	char *c = buf;
	for(int j = 0; j <k; ++j)p[j]=j;
	int m = clen(k);
	while( next_permutation(p,&p[k]) ){
		int m2 = clen(k);
		if( m2 < m)m = m2;
	}
	return m;
}

int main(){
	freopen("Din.txt","r",stdin);
	freopen("Dout.txt","w",stdout);

	int N;
	gets(buf); sscanf(buf,"%d", &N);

	for(int nc = 1; nc <= N; ++nc){
		fprintf(stderr,"%d / %d ",nc,N);
		int r = RLE();
		printf( "Case #%d: %d\n", nc,r);

	}
}
