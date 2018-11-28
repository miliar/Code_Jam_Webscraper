#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int diff(int a, int b){
	return abs(a - b);
}

void solve(int c){
	int op = 1, bp = 1, ot = 0, bt = 0;
	int n;
	scanf("%d", &n);
	while(n--){
		char ri = 0;
		int pi;
		while(ri != 'O' && ri != 'B'){
			scanf("%c", &ri);
		}
		scanf("%d", &pi);
		if(ri == 'O'){
			ot = max(ot + diff(op, pi) + 1, bt + 1);
			op = pi;
		}else{
			bt = max(bt + diff(bp, pi) + 1, ot + 1);
			bp = pi;
		}
	}
	printf("Case #%d: %d\n", c, max(ot, bt));
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		solve(i+1);
	}
	return 0;
}
