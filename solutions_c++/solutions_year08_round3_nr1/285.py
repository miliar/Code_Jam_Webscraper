#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 1010;
int wz[maxn], a[maxn];
long long res;
int N, P, K, L;

void read(){
	scanf("%d%d%d", &P, &K, &L );
	for( int i=1; i<=L; i++)
		scanf("%d", &a[i]);
}

int getmin( ){
	int i, id=0, mini = 1000000;
	for( i=K; i>=1; i--){
		if( wz[i]<mini && wz[i]<=P){
			mini = wz[i];		
			id = i;
		}
	}
	return id;
}

void solve(){
	int i, id;
	bool ok=1;
	sort( &a[1], &a[L+1] );
	for( i=1; i<=K; i++)
		wz[i]=1;
	res = 0;
	for( i=L; i>=1; i-- ){
		id = getmin();
		if( id == 0 ) {
			ok=0; 
			break;
		}
		res += a[i]*wz[id];
		wz[id]++;
	}
	if( ok==0 )
		printf("Impossible\n");
	else
		printf("%lld\n", res);
}

int main(){
//	freopen("D:\\A.txt", "r", stdin );
//	freopen("D:\\out.txt", "w", stdout);
	int tc, i;
	scanf("%d", &tc);
	for( i=1; i<=tc; i++ ){
		printf("Case #%d: ", i);
		read();
		solve();
	}
	return 0;
}
