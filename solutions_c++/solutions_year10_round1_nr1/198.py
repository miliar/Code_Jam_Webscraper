#include <iostream>
using namespace std;

char a[100][100];
int n,m;
const int dx[4]={0,1,1,1};
const int dy[4]={1,0,-1,1};

char ask(int x,int y) {
	if (x>=0 && y>=0 && x<n && y<n) return a[x][y];
	return '.';
}

bool check(int x,int y,int dx, int dy, char w) {
	//cerr<<x<<' '<<y<<' '<<dx<<' '<<dy<<' '<<w<<endl;
	for(int i=0;i<m;i++) {
		if (ask(x,y)!=w) return false;
		x+=dx;
		y+=dy;
	}
	return true;
}

bool win(char w) {
	for(int i=0;i<n;i++) for(int j=0;j<n;j++) if (a[i][j]==w) {
		for(int k=0;k<4;k++) if (check(i,j,dx[k],dy[k],w)) return true;
	}
	return false;
}

int main() {
	int TT;
	cin>>TT;
	for(int T=1;T<=TT;T++) {
		cin>>n>>m;
		cout<<"Case #"<<T<<": ";
		for(int i=0;i<n;i++) for(int j=0;j<n;j++) cin>>a[j][i];
		//cerr<<'a'<<endl;
		for(int j=0;j<n;j++) {
			int t=n-1;
			for(int i=n-1;i>=0;i--) if (a[i][j]!='.') {
				a[t][j]=a[i][j];
				t--;
			}
			for(int i=0;i<=t;i++) a[i][j]='.';
		}
		//for(int i=0;i<n;i++) { for(int j=0;j<n;j++) cout<<a[i][j]; cout<<endl; }
		if (win('B')) {
			if (win('R')) cout<<"Both";
			else cout<<"Blue";
		} else {
			if (win('R')) cout<<"Red";
			else cout<<"Neither";
		}
		cout<<endl;
	}
	return 0;
}
