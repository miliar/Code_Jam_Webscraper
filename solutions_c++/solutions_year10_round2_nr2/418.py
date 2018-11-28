#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <sstream>
#include <cmath>
#include <map>

using namespace std;

typedef long long int lli;

int main(void){
	int C, K, N, B, T;
	cin >> C;
	for(int cas = 1; cas <= C; cas++){

		cin >> N >> K >> B >> T;
		vector<lli> v = vector<lli>(N);
		vector<lli> p = vector<lli>(N);

		for(int i = 0; i < N; i++) cin >> p[i];
		for(int i = 0; i < N; i++) cin >> v[i];

		int qt = 0;
		int res = 0;
		for(int i = N-1; i >= 0; i--){
			if(qt == K) break;
			if(p[i]+v[i]*T >= (lli)B){
				qt++;
			}
			else{
				res+=K-qt;
			}
		}
		printf("Case #%d: ", cas);
		if(qt != K) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);


	}

	return 0;
}
