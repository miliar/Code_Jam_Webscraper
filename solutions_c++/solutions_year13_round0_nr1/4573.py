#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <typeinfo>
#include <set>
#include <cctype>
#include <locale>
#include <utility>
#include <map>
#include <iterator>
#include <valarray>
#include <complex>
#include <sstream>
#include <bitset>
#include <ctime>
#include <list>
#include <numeric>
#include <cstring>
using namespace std;

#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sqr(a) (a)*(a)
#define mp make_pair

typedef long long i64;

//////////////////////////////////////////////////////

const int INF = ~(1 << 31);

double xst = 1, yst = 1;
int n = 2;

double func(double x1, double x2){
	return (x1*x1 - x2)*(x1*x1 - x2) + (x1 - 1)*(x1 - 1);
}

double val(pair<double, double> cur, int i, int j, double len){
	if(i == j){
		if(j == 1) return cur.first + ((sqrt(n + 1.0) + n - 1) / (n * sqrt(2.0)))*len;
		if(j == 2) return cur.second + ((sqrt(n + 1.0) + n - 1) / (n * sqrt(2.0)))*len;
	}else{
		if(j == 1) return cur.first + ((sqrt(n + 1.0) - 1) / (n * sqrt(2.0)))*len;
		if(j == 2) return cur.second + ((sqrt(n + 1.0) - 1) / (n * sqrt(2.0)))*len;
	}
}

bool cmp(pair<double, double> a, pair<double, double> b){
	return func(a.first, a.second) < func(b.first, b.second);
}

int chtoint(char ch){
	if(ch == '.') return 0;
	if(ch == 'X') return 1;
	if(ch == 'O') return 2;
	if(ch == 'T') return 3;
}

int main(){
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	scanf("%d", &tt);
	string tmp;
	for(int t = 1; t <= tt; t++){
		vector<vector<int> > rows(4, vector<int>(4, 0)), cols(4, vector<int>(4, 0));
		vector<int> diag1(4, 0), diag2(4, 0);
		int cnt = 0;
		for(int i = 0; i < 4; i++){
			cin >> tmp;
			for(int j = 0; j < tmp.size(); j++){
				rows[i][chtoint(tmp[j])]++;
				cols[j][chtoint(tmp[j])]++;
				if(i == j){
					diag1[chtoint(tmp[j])]++;
				}
				if(i == 3 - j){
					diag2[chtoint(tmp[j])]++;
				}
				if(tmp[j] == '.') cnt++;
			}
		}
		if(diag1[1] + diag1[3] == 4 || diag2[1] + diag2[3] == 4){
			printf("Case #%d: X won\n", t);
			goto lalala;
		}
		if(diag1[2] + diag1[3] == 4 || diag2[2] + diag2[3] == 4){
			printf("Case #%d: O won\n", t);
			goto lalala;
		}
		for(int i = 0; i < 4; i++){
			if(rows[i][1] + rows[i][3] == 4 || cols[i][1] + cols[i][3] == 4){
				printf("Case #%d: X won\n", t);
				goto lalala;
			}
			if(rows[i][2] + rows[i][3] == 4 || cols[i][2] + cols[i][3] == 4){
				printf("Case #%d: O won\n", t);
				goto lalala;
			}
		}
		if(cnt == 0){
			printf("Case #%d: Draw\n", t);
		}else{
			printf("Case #%d: Game has not completed\n", t);
		}
		lalala:;
	}
	return 0;
}