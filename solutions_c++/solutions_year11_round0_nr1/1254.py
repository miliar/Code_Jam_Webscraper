#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

#define ABS(x) ((x) > 0 ? (x) : -(x))

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int testCase;
	scanf("%d", &testCase);
	for(int tc = 1; tc <= testCase; ++tc){
		int n;
		char OP[105];
		int button[105];
		scanf("%d", &n);
		for(int i = 0; i < n; ++i){
			//scanf("%c%d", &OP[i], &button[i]);
			cin >> OP[i] >> button[i];
		}
		int opTime = button[0], res = opTime, p[26];
		char preOp = OP[0];
		p['O' - 'A'] = p['B' - 'A'] = 1;
		p[preOp - 'A'] = button[0];
		for(int i = 1; i < n; ++i){
			int dt = ABS(button[i] - p[OP[i] - 'A']) + 1;
			if(preOp != OP[i]){
				if(dt > opTime){
					res += dt - opTime;
					opTime = dt - opTime;
				}
				else{
					res += 1;
					opTime = 1;
				}
				preOp = OP[i];
			}
			else{
				res += dt;
				opTime += dt;
			}
			p[OP[i] - 'A'] = button[i];
		}
		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}
