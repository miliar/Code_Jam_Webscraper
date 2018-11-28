#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main(){
	int T;
	cin >> T;
	for( int t = 1; t <= T; ++t ){
		char combine[26][26] = {0};
		bool opposed[26][26] = {0};
		
		int C, D, N;
		cin >> C;
		for( int k = 0; k < C; ++k ){
			char i, j, v;
			cin >> i >> j >> v;
			combine[i-'A'][j-'A'] = v;
			combine[j-'A'][i-'A'] = v;
		}
		cin >> D;
		for( int k = 0; k < D; ++k ){
			char i, j;
			cin >> i >> j;
			opposed[i-'A'][j-'A'] = true;
			opposed[j-'A'][i-'A'] = true;
		}
		
		vector<char> L;
		L.reserve(101);
		
		cin >> N;
		for( int k = 0; k < N; ++k ){
			char v;
			cin >> v;
			if (L.size()){
				if(combine[L.back()-'A'][v-'A']){
					L.back() = combine[L.back()-'A'][v-'A'];
					continue;
				}
				else {
					bool found = false;
					for( int i = 0; i < L.size(); ++i ){
						if(opposed[L[i]-'A'][v-'A']){
							L.clear();
							found = true;
							break;
						}
					}
					if (found) continue;
				}
			}
			L.push_back(v);
		}
		printf("Case #%d: [", t);
		for( int i = 0; i < (int)L.size() - 1; ++i ){
			printf("%c, ", L[i]);
		}
		if (L.size()) printf("%c]\n", L.back());
		else printf("]\n");
	}
}
