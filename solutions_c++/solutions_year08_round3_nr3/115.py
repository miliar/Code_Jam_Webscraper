#include<algorithm>
#include<cstdio>
#include<vector>
#include<string>

using namespace std;

int n, m;
long long X, Y, Z;

vector<int> speed;

bool Read(){
	scanf("%d%d%lld%lld%lld", &n, &m, &X, &Y, &Z);
	vector<int> A(m, 0);
	for(int i = 0; i < m; ++i){
		scanf("%d", &A[i]);
	}
	speed.clear();
	for(int i = 0; i < n; ++i){
		speed.push_back( A[ i % m ] );
		A[ i % m ] = int((X * A[i % m] + Y * (i + 1)) % Z);
	}
	return true;
}

int Solve(){
	vector<int> ms;
	ms.assign( speed.size(), 1 );

	for(int i = 0; i < n; i++)
	{
		for( int j = 0; j < i; j++)
		{
			if( speed[i] > speed[j] ) ms[i] = (ms[i] + ms[j])%1000000007 ;
		}
	}
	int res = 0;
	for(int i = 0; i < ms.size(); ++i){
		res = (res + ms[i])%1000000007;
	}
	return res;
}

void Write( int num, int ans ){
	printf( "Case #%d: %d\n", num, ans );
}

int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int n;
	scanf( "%d", &n );
	for(int i = 0; i < n; ++i){
		Read();
		Write( i+1, Solve() );
	}

	return 0;
}