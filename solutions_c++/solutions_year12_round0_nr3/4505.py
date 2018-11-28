#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;

#define pb push_back
#define ppb pop_back
#define mp make_pair
#define N 1000
const int INF = ~(1 << 31);
const double EPS = 1e-8;

int str_to_int(string s){
	int ten = 1, res = 0;
	for(int i = s.size() - 1; i >= 0; i--){
		res += (s[i] - '0') * ten;
		ten *= 10;
	}
	return res;
}

string int_to_str(int n){
	string res;
	while(n){
		res += '0' + n % 10;
		n /= 10;
	}
	reverse(res.begin(), res.end());
	return res;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, a, b, cnt;
	cin >> n;
	for(int i = 1; i <= n; i++){
		cin >> a >> b;
		cnt = 0;
		for(int j = a; j <= b; j++){
				string t = int_to_str(j);
				map<int, bool> m;
				m[j] = 1;
				for(int k = 1; k < t.size(); k++){
					rotate(t.begin(), t.begin() + 1, t.end());
					int g = str_to_int(t);
					if(g <= b && g > j && m[g] == 0){
						cnt++;
						m[g] = 1;
					}
				}
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	return 0;
}