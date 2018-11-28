#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int MaxN = 1003;
const int MaxL = 3;

int L,N,C;
int a[MaxN];
long long t;
long long f[MaxN][MaxL];

void solve(){
	memset( f , -1 , sizeof( f ));
	//scanf("%d%d%d%d",&L,&t,&N,&C);
	cin>>L>>t>>N>>C;
	for( int i = 0 ; i < C ; ++i ){
		scanf("%d",&a[i]);
		a[i] <<= 1;
	}
	f[0][0] = 0;
	for( int i = 0 ; i < N ; ++i ){
		long long dis = a[i%C];
		for( int j = 0 ; j <= L ; ++j ){
			if( f[i][j] == -1 ) continue;
			if( f[i+1][j] == -1 || f[i+1][j] > f[i][j] + dis ){
				f[i+1][j] = f[i][j] + dis ;
			}
			if( j == L ) continue;
			long long used = t - f[i][j];
			if( used < 0 ) used = 0;
			long long val = used + (dis-used)/2;
			
			if( f[i+1][j+1] == -1 || f[i+1][j+1] > f[i][j] + val ){
				f[i+1][j+1] = f[i][j] + val;
			}
			
		}
	}
	long long Ans = -1;
	for( int i = 0 ; i <= L ; ++i ){
		if( Ans == -1 || Ans > f[N][i] )
			Ans = f[N][i];
	}
	cout<<Ans<<endl;
}
int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for( int i = 1 ; i <= T ; ++i ){
		printf("Case #%d: ",i);
		solve();
	}
}