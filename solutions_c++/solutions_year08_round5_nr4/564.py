#include<algorithm>
#include<cstdio>
#include<vector>
#include<string>

using namespace std;

vector<vector<int> > ms;

bool Read(){
	int xl, yl;
	scanf("%d%d", &yl, &xl);
	ms.assign( yl, vector<int>(xl, -1));
	int r;
	scanf("%d", &r);
	for(int i = 0; i < r; ++i){
		scanf("%d%d", &yl, &xl );
		ms[yl - 1][xl - 1] = -2;
	}
	return true;
}

int rec( int y, int x ){
	if( y < 0 || x < 0 ) return 0;
	if( ms[y][x] == -2 ) return 0;
	if( ms[y][x] >= 0 ) return ms[y][x];
	ms[y][x] = (rec( y - 1, x - 2 ) + rec( y - 2, x - 1 ))%10007;
	return ms[y][x];
}

int Solve(){
	ms[0][0] = 1;
	return rec( ms.size() -1, ms[0].size() -1 );
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