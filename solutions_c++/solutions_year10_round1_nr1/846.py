#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

char buf[1024*1024];

int main() {
	freopen("C:\\Projects\\GCJ\\input", "rt", stdin);
	freopen("C:\\Projects\\GCJ\\output.txt", "wt", stdout);

	int c;
	cin >> c;
	for (int z=0;z<c;z++)
	{
		int n,m;
		cin >> n >> m;
		vector<string> board;
		for (int i=0;i<n;i++) {
			string str;
			cin >> str;
			board.push_back(str);
		}

		string t = "";
		for (int i=0;i<n;i++) {
			t += ".";
		}

		bool red=false,blue=false;
		for (int k=0;k<8;k++) {
			vector<string> temp;
			
			for (int i=0;i<n;i++) {
				temp.push_back(t);
			}

			for (int i=0;i<n;i++) {
				for (int j=0;j<n;j++) {
					temp[i][j] = board[n-j-1][i];
				}
			}

			/*for (int i=0;i<n;i++) {
				for (int j=0;j<n;j++) {
					cout << temp[i][j];
				}
				cout << endl;
			}*/

			for (int i=n-1;i>=0;i--)
			{
				for (int j=0;j<n;j++) {
					if (temp[i][j] == '.') {
						bool isAny=false;
						for (int k=i;k>0;k--) {
							if (temp[k-1][j] != '.') isAny = true;
							temp[k][j] = temp[k-1][j];
						}
						temp[0][j] = '.';
						if (isAny){
						i++;
						break;}
					}
				}
			}

			bool q = false;
			for (int i=0;i<n;i++) {
				for (int j=0;j<n;j++) {
					if (temp[i][j] != '.') {
						char ch = temp[i][j];

						if (ch == 'R' && red == true) continue;
						if (ch == 'B' && blue == true) continue;

						bool flag[4] = {true, true, true, true};

						for (int a=0;a<m;a++) {
							if (i+a >= n || temp[i+a][j] != ch) {
								flag[0] = false;
							}
							if (j+a >= n || temp[i][j+a] != ch) {
								flag[1] = false;
							}
							if (i+a >= n || j+a >= n || temp[i+a][j+a] != ch) {
								flag[2] = false;
							}
							if (i+a >= n || j-a < 0 || temp[i+a][j-a] != ch) {
								flag[3] = false;
							}
						}

						if (flag[0] || flag[1] || flag[2] || flag[3]) {
							//cout << ch << "=" << i << "," << j << endl;
							if (ch == 'R') red = true;
							if (ch == 'B') blue = true;
						}
					}
				}
			}

			/*cout << endl;
			for (int i=0;i<n;i++) {
				for (int j=0;j<n;j++) {
					cout << temp[i][j];
				}
				cout << endl;
			}*/

			if (red || blue) break;
		}
		cout << "Case #" << (z+1) << ": ";
		if (red && blue) cout << "Both";
		else {
			if (red) cout << "Red";
			if (blue) cout << "Blue";
		}
		if (!(red || blue)) cout << "Neither";
		cout << endl;
	}

	exit(0);
}
