#include <iostream>
#include <vector>
#include <string>

using namespace std;
typedef long long int64;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define pb push_back
const int maxn = 101;

int n,k;
string str[maxn];

void rotate() {
	string str2[maxn];
	for (int i=0;i<n;i++) str2[i] = str[i];
	for (int i=0;i<n;i++) 
		for (int j=0;j<n;j++) str2[j][n-1-i] = str[i][j];
	for (int i=0;i<n;i++) str[i] = str2[n-1-i];
}

void gravity() {
//	for (int i=n-1;i>=0;i--) cout<<str[i]<<endl;
	//cout<<endl;
	for (int i=1;i<n;i++) {
		for (int j=0;j<n;j++) if (str[i][j]!='.') {
			int i2=i-1;
			while (i2>=0 && str[i2][j]=='.') {str[i2][j] = str[i2+1][j];str[i2+1][j]='.';i2--;}
		}
	}
	//for (int i=n-1;i>=0;i--) cout<<str[i]<<endl;
}

bool check(char c) {
	for (int i=0;i<n;i++) 
		for (int j=0;j<n;j++) if (str[i][j]==c) {
			bool ok;
			if (i<=n-k && j<=n-k) {
				ok = true;
				for (int x=1;x<k;x++) if (str[i+x][j+x]!=c) ok = false;
				if (ok) return true;
			}
			if (j<=n-k) {
				ok = true;
				for (int x=1;x<k;x++) if (str[i][j+x]!=c) ok = false;
				if (ok) return true;
			}

			if (i<=n-k) {
				ok = true;
				for (int x=1;x<k;x++) if (str[i+x][j]!=c) ok = false;
				if (ok) return true;
			}
			if (j>=k-1) {
				ok = true;
				for (int x=1;x<k;x++) if (str[i+x][j-x]!=c) ok = false;
				if (ok) return true;
			}
		}
	return false;
}

int main() {
	int nTest;
	cin>>nTest;
	for (int test=1;test<=nTest;test++) {
		cin>>n>>k;
		for (int i=0;i<n;i++) cin>>str[i];

		rotate();
		gravity();

		bool isBlue = check('B');
		bool isRed  = check('R');

		cout<<"Case #"<<test<<": ";
		if (isBlue) {
			if (isRed) cout<<"Both"; else cout<<"Blue";
		} else {
			if (isRed) cout<<"Red"; else cout<<"Neither";
		}

		cout<<endl;
	}
	return 0;
}
