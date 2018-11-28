#include "stdafx.h"
#include <iostream>
#include <string>
#include <set>
using namespace std;

int main(){
	freopen("test.txt", "r", stdin);
	freopen("result.txt", "w", stdout);
	char c[8];
	int T, A, B, result, i, j, k, p, q;
	set<int> t;
	string ss;

	cin>>T;
	for(i = 1; i <= T; i++){
		cin>>A>>B;
		result = 0;
		for(j = A; j < B; j++){
			t.clear();
			sprintf(c, "%d", j);
			ss = c;
			ss = ss + ss;
			for(k = 1; k <= ss.size() / 2 - 1; k++){
				if(ss[k] != '0'){
					q = 0;
					for(p = k; p <= k + ss.size() / 2 - 1; p++){
						q = q * 10 + ss[p] - '0';
					}
					if(q <= B && q > j && t.find(q) == t.end()){
						t.insert(q);
						result++;
					}
				}
			}
		}
		cout<<"Case #"<<i<<": "<<result<<endl;
	}

	return 0;
}
