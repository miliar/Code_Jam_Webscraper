#include <numeric>
#include <cstring>
#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cstdlib>
#include <cctype>
#include <deque>
#include <cmath>
#include <sstream>
#include <string>
using namespace std;
typedef pair<int, int> pii;
#define mp make_pair
#define fst first
#define snd second
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
int a1, a2, b1, b2;
int dp[100][100];

bool win(int a, int b){ // a <= b
	if(a > b) return win(b, a);
	if(b - a *2 >= 0) return true;
	else return !win(a, b - a);
}

int main(){
	int tt;
	cin >> tt;
	for(int casos = 1; casos <= tt; casos++){
			cin >> a1 >> a2 >> b1 >> b2;
			int res = 0;
			for(int a = a1; a <= a2; a++)
			for(int b = b1; b <= b2; b++)
				res += win(a, b);
			cout << "Case #"<<casos<<": "<<res<<endl;
	}
}
