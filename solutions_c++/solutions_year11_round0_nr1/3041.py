
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <cassert>
#include <map>
#include <stack>

#define FOR(I,A,B) for(int I=(A);I<(B);I++)
#define REP(I,N) FOR(I,0,N)
#define ALL(A) (A).begin(),(A).end()

#define SQR(x) ((x)*(x))
#define PB(x) push_back(x)

#define PI (acos(-1.0))

using namespace std;

typedef vector<int> VI;
typedef vector< vector<int> > VVI;

// this solution's order is O(number of buttons * N)

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int testcase;
	cin >> testcase;
	for(int tc=1;tc<=testcase;tc++) {
		int n;
		int now=0;
		int nowtime = 0;
		cin >> n;
		VI robot[2],buttons;
		int whererobot[2] = {1,1};
		int idx[2] = {0,0};
		REP(i,n) {
			string name;
			int button;
			cin >> name >> button;
			if(name=="O") {
				robot[0].push_back(button);
				buttons.push_back(0);
			}
			if(name=="B") {
				robot[1].push_back(button);
				buttons.push_back(1);
			}
		}

		while(now < n) {
			bool pressed = false;
			for(int j=0;j<2;j++) {
				if(idx[j] >= robot[j].size()) continue;
				if(whererobot[j] < robot[j][idx[j]]) {
					whererobot[j] ++;
				}
				else if(whererobot[j] > robot[j][idx[j]]) {
					whererobot[j] --;
				}
				else if(buttons[now] == j) {
					pressed = true;
					idx[j]++;
				}
			}
			if(pressed) now++;
			nowtime++;
		}
		printf("Case #%d: %d\n",tc,nowtime);

	}
}
