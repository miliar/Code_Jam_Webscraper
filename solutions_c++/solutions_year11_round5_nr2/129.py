// by shik
#include <cstdio>
#include <cstring>
#include <algorithm>
#define N 1010
#define S 10010
using namespace std;
int n,num[N],app[S];
bool chk( int M ) {
	memset(app,0,sizeof(app));
	for ( int i=0; i<n; i++ ) app[num[i]]++;
	for ( int i=0,j; i<S; i++ ) {
		while ( app[i] ) {
			for ( j=i+1; j<S&&app[j]>=app[j-1]; j++ );
			if ( j-i<M ) return 0;
			for ( int k=i; k<j; k++ ) app[k]--;
		}
	}
	return 1;
}
int main()
{
	int T,cas=0;
	int L,M,R;
	scanf("%d",&T);
	while ( T-- ) {
		scanf("%d",&n);
		for ( int i=0; i<n; i++ ) scanf("%d",num+i);
		L=0; R=n;
		while ( L!=R ) {
			M=(L+R+1)/2;
			if ( chk(M) ) L=M;
			else R=M-1;
		}
		printf("Case #%d: %d\n",++cas,L);
	}
	return 0;
}
