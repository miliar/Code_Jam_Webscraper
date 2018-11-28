#include <cstdio>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
 
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define sz size()
#define sqr(x) (x) * (x)
#define all(x) (x).begin(), (x).end()

int dx[] = {1, -1, 0, 0, -1, 1, 1, -1};
int dy[] = {0, 0, 1, -1, -1, -1, 1, 1};

char check(vector<int> &cn) {
	if(cn[0] == 4) return 'X';
	if(cn[1] == 4) return 'O';

	if(cn[0] == 3 && cn[2] == 1) return 'X';
	if(cn[1] == 3 && cn[2] == 1) return 'O';
	return 'Z';
}

void solveA() {
	vector<string> voc(12, "............");
	vector<int> cn(3);
	set<char> cw;
	int emp = 0;
	char ch;
	string s;
	for(int i = 4; i < 8; i++) {
		cin >> s;
		voc[i] = "...." + s + "....";
	}
	for(int i = 4; i <= 7; i++) {
		for(int j = 4; j <= 7; j++) {
			if(voc[i][j] == '.') {
				emp++;
				continue;
			}
			for(int k = 0; k < 8; k++) {
				cn[0] = cn[1] = cn[2] = 0;
				for(int m = 0; m <= 3; m++) {
					ch = voc[i + dx[k] * m][j + dy[k] * m];
					if(ch == 'X') {
						cn[0]++;
					}
					if(ch == 'O') {
						cn[1]++;
					}
					if(ch == 'T') {
						cn[2]++;
					}
				}
				ch = check(cn);
				if(ch == 'X' || ch == 'O')
					cw.insert(ch);
			}
		}
	}
	if(cw.sz == 2 || (cw.empty() && emp == 0)) {
		puts("Draw");
		return;
	}
	if(cw.empty() && emp > 0) {
		puts("Game has not completed");
	} else {
		if(*cw.begin() == 'X') {
			puts("X won");
		} else {
			puts("O won");
		}
	}
}

vector<long long> pals;

bool ispal(long long n) {
	return true;
}

void init() {
	for(long long i = 1; i <= 10000000; i++) {
		if(ispal(i) && ispal(i * i))
			pals.pb(i);
	}
}
void solveB() {
	int l, r;
}
void OJ() {
    int t = 0;
    //scanf("%d", &t);
	cin >> t;
	//init();
	//cout << pals.sz << endl;
    for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
        solveA();
    }
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    OJ();
    
    return 0;
}