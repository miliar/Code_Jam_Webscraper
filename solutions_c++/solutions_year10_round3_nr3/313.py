#include <iostream>
using namespace std;

int r,c;
int map[512][512];
int ans[513];

void set(int y, int x, char ch) {
	int num;
	if( ch>='0' && ch<='9' ) num = ch-'0';
	if( ch>='A' && ch<='F' ) num = (ch-'A'+10);

	for( int i=3; i>=0; i-- ) {
		map[y][x+i] = num%2;
		num /= 2;
	}
}

void solve() {

	int fsize = min(r,c);
	for( int i=1; i<=fsize; i++ ) {
		ans[i]=0;
	}
	int distans=0;

	for( int size=fsize; size>=1; size-- ) {
	for( int i=0; i<=r-size; i++) {
		for( int j=0; j<=c-size; j++ ) { 
			if( map[i][j]==2 ) continue;

			int head = map[i][j];
			bool inval = false;
			for(int k=0; k<size; k++ ) {
				for( int l=0; l<size; l++ ) {
					if( !((map[i+k][j+l]==head && (k+l)%2== 0) || (map[i+k][j+l]!=head && (k+l)%2== 1)) || (map[i+k][j+l] == 2)) {
						inval=true;
						break;
					}
				}
				if( inval==true) break;
			}

			if( inval == false ) {
				for(int k=0; k<size; k++ ) {
					for( int l=0; l<size; l++ ) {
						map[i+k][j+l]=2;
					}
				}


				if( ans[size]==0 ) distans++;
				ans[size]++;
			}
		}
	}
	}

	cout<<distans<<endl;
	for( int i=fsize; i>=1; i-- ) {
		if( ans[i] > 0 ) 
			cout<<i<<" "<<ans[i]<<endl;
	}


}

int main() {
	freopen("C-small-attempt1.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	//freopen("c.in", "rt", stdin);
	int t;
	cin>>t;
	for( int i=0; i<t; i++ ) {
		cin>>r>>c;

		for( int j=0; j<r; j++ ) {
			char row[512];
			for( int k=0; k<c/4; k++ ) {
				cin>>row[k];
			}
			for( int k=0; k<c/4; k++ ) {
				set(j, k*4, row[k]);
			}
		}

		cout<<"Case #"<<i+1<<": ";
		solve();

	}
	return 0;
}