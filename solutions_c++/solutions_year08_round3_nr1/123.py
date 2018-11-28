#include<algorithm>
#include<cstdio>
#include<vector>
#include<string>

using namespace std;

int p, k, l;
vector<int> freq;


bool Read(){
	scanf("%d%d%d", &p, &k, &l );
	freq.clear();
	freq.assign( l, 0 );
	for(int i = 0; i < l; ++i){
		scanf( "%d", &freq[i] );
	}
	return true;
}

long long Solve(){
	long long res = 0;
	sort( freq.rbegin(), freq.rend() );
	int cur = 0;
	int num = 1;
	while( cur < l ){
		for(int j = 0; (j < k) && (cur < l) ; ++j, ++cur ){
			res = res + num*freq[cur];
		}
		num++;
	}
	return res;
}

void Write( int num, long long ans ){
	printf( "Case #%d: %lld\n", num, ans );
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