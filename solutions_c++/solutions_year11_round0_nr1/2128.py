#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <string>
#include <queue>
#include <cmath>
#include <numeric>
#include <list>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <climits>
#include <set>
#include <memory.h>
#include <memory>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <map>
#include <cassert>
#include <time.h>
#define _USE_MATH_DEFINES
using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef pair<int, P> PP;
typedef pair<string, int > Ps;
typedef vector<int> vec;
typedef vector<vec> mat;
const int INF = 1 << 30;
const double EPS = 1e-9;

bool doit = true;

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T, n, res;
	int pos[2];
	int can_move, button;
	int robo, pre;
	char op;
	cin >>T;
	for(int t = 0; t < T; t++){
		cin >> n;
		res = 0;
		can_move = 0;
		pos[0] = pos[1] = 1;
		pre = 2;
		for(int j = 0; j < n; j++){
			cin >> op >> button;
			if(op == 'B'){
				robo = 0;
			}else {
				robo = 1;
			}
			if(pre != robo){
				int dis = max(0, abs(button - pos[robo]) - can_move);
				res += dis + 1;
				can_move = dis + 1;
				pre = robo;
				pos[robo] = button;
			}else{
				int dis = abs(button - pos[robo]);
				res += dis + 1;
				can_move += dis + 1;
			}
			pre = robo;
			pos[robo] = button;
		}
		cout << "Case #" << t + 1 << ": " << res << endl;
	}
	cin.close();
	cout.close();
	return 0;
}