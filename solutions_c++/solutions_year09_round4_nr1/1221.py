#include <iostream>
#include <algorithm>
#include <hash_map>
#include <queue>
using namespace std;
using namespace stdext;
const int N = 10;
int last[N], index[N];

bool isOK(int n){
	for(int i = 0; i < n; ++i)
		if(last[index[i]] > i) return false;
	return true;
}
int main(){
	//freopen("ip.in", "r", stdin);
	//freopen("op.out", "w", stdout);
	
	int cas;
	scanf("%d", &cas);
	for(int cs = 1; cs <= cas; ++cs){
		int n;
		char str[N];
		scanf("%d", &n);
		int code = 0, ten = 1;
		for(int i = 0; i < n; ++i){
			scanf("%s", str);
			for(last[i] = n - 1; last[i] >= 0; --last[i])
				if(str[last[i]] == '1') break;
			code += ten * i;
			ten *= 10;
		}
		hash_map<int, int> M;
		M[code] = 1;
		queue<int> Q;
		Q.push(code);
		int res = -1;
		while(!Q.empty() && res < 0){
			code = Q.front();
			Q.pop();
			int code_ = code;
			int cost = M[code];
			for(int i = 0; i < n; ++i){
				index[i] = code % 10;
				code /= 10;
			}
			if(isOK(n)){
				res = cost - 1;
				break;
			}
			for(int i = 0; i < n - 1; ++i){
				swap(index[i], index[i + 1]);
				int code2 = 0, ten = 1;
				for(int k = 0; k < n; ++k){
					code2 += index[k] * ten;
					ten *= 10;
				}
				if(!M[code2]){
					M[code2] = cost + 1;
					Q.push(code2);
				}
				swap(index[i], index[i + 1]);
			}

		}
		printf("Case #%d: %d\n", cs, res);
	}
	return 0;
}