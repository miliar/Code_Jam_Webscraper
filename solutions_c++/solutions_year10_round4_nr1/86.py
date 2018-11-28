#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>

using namespace std;

int n;
int a[310][310];
int start[310];
int len[310];
int ans;


bool check(int x1,int y1, int x2 , int y2){
	if (x1<0 || y1<0 || x2<0 || y2<0) return true;
	if (a[x1][y1]<0 || a[x2][y2]<0) return true;
	if (a[x1][y1]==a[x2][y2]) return true;
	return false;
}


bool centers(int x, int y) {
	int i,j,k;
	for ( int i=1; i<=2*n-1; ++i )
		for ( int j=1; j<=2*n-1; ++j )
			if ( a[i][j]>=0 )
				if ( ! ( check( i, j, 2*x-i, j ) && check( i, j, i, 2*y-j ) ) )
					return false;
	return true;
}

int Abs(int x){
	if (x<0) return -x; else return x;
}
int find(int x, int y){
	int ret=0;
	int i,j;
	for ( int i=1; i<=2*n-1; ++i )
		for ( int j=1; j<=2*n-1; ++j )
			if ( a[i][j]>=0 )
				ret=max(ret,Abs(x-i)+Abs(y-j));
	return ret+1;
}

int main(){
	int test=0;
	scanf("%d", &test);
	for ( int T=1; T<=test; ++T ){
		scanf("%d",&n);
		memset(a,-1,sizeof(a));
		for ( int i=1; i<=n; ++i ){
			int j=n-i+1;
			len[i]=i;
			start[i]=j;
			for ( int k=1; k<=len[i]; ++k ){
				scanf("%d",&a[i][j]);	
				j+=2;
			}	
		}
		for ( int i=n+1; i<=2*n-1; ++i ){
			int j=i-n+1;
			len[i]=2*n-i;
			start[i]=j;
			for ( int k=1; k<=len[i]; ++k ){
				scanf("%d",&a[i][j]);
				j+=2;
			}
		}
		ans = 1000;
		for ( int i=1; i<=2*n-1; ++i )
			for ( int j=1; j<=2*n-1; ++j )
				if (centers(i,j))
					ans=min(ans , find(i,j));
		n = (1+n)*n - n;
		ans = (1+ans)*ans - ans;
		printf("Case #%d: %d\n", T, ans - n);
	}
	
	return 0;	
}
