#pragma comment linker("/STACK:16000000");
#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector> 
#include <functional>

using namespace std; 

template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const double pi = 3.1415926;
const ld eps = 1e-9;
const int N = (int)1e5+5;
const int INF = (int)1e9+10;

const double EPS = 0.00001;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int t;
	cin >> t;
	string s[4];
	for(int o = 0; o < t; o++) {
		
		for(int i = 0; i < 4; i++)
			cin >> s[i];
		int k = 0;
		bool f = false;
		for(int i = 0; i < 4; i++) {
			k = 0;
			for(int j = 0; j < 4; j++) {
				if(s[i][j] == 'X') k++;
				else if(s[i][j] == 'O') k--;
				else if(s[i][j] == '.') { f = true; break; }
			}
			if(k >= 3) {
				cout << "Case #" << (o+1) << ": X won" << endl;
				goto end;
			}
			else if(k <= -3) {
				cout << "Case #" << (o+1) << ": O won" << endl;
				goto end;
			}
		}
		k=0;
		for(int i = 0; i < 4; i++) {
			k = 0;
			for(int j = 0; j < 4; j++) {
				if(s[j][i] == 'X') k++;
				else if(s[j][i] == 'O') k--;
				else if(s[j][i] == '.') { f = true; break; }
			}
			if(k >= 3) {
				cout << "Case #" << (o+1) << ": X won" << endl;
				goto end;
			}
			else if(k <= -3) {
				cout << "Case #" << (o+1) << ": O won" << endl;
				goto end;
			}
		}
		k=0;
		for(int i = 0, j = 0; i < 4 && j < 4; i++, j++) {
			if(s[j][i] == 'X') k++;
			else if(s[j][i] == 'O') k--;
			else if(s[j][i] == '.') { f = true; break; }
		}
		if(k >= 3) {
			cout << "Case #" << (o+1) << ": X won" << endl;
			goto end;
		}
		else if(k <= -3) {
			cout << "Case #" << (o+1) << ": O won" << endl;
			goto end;
		}
		k=0;
		for(int i = 0, j = 3; i < 4 && j >= 0; i++, j--) {
			if(s[i][j] == 'X') k++;
			else if(s[i][j] == 'O') k--;
			else if(s[i][j] == '.') { f = true; break; }
		}
		if(k >= 3) {
			cout << "Case #" << (o+1) << ": X won" << endl;
			goto end;
		}
		else if(k <= -3) {
			cout << "Case #" << (o+1) << ": O won" << endl;
			goto end;
		}

		if(f) { cout << "Case #" << (o+1) << ": Game has not completed" << endl; }
		else cout << "Case #" << (o+1) << ": Draw" << endl;

		end:
		;

	}
}