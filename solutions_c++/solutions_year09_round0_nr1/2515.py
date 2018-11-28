#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>

using namespace std;

int main(){

	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int l, d, n;
	scanf("%i%i%i", &l, &d, &n);
	vector<string> alphabet;
	for(int i=0; i<d; i++){
		string s;
		cin >> s;
		alphabet.push_back(s);
	}

	vector<vector<vector<char>>> patterns;

	for(int i=0; i<n; i++){
		string tmp;
		cin >> tmp;
		vector<vector<char>> pattern;
		pattern.resize(50);
		int k = 0;
		bool inbraket = false;
		for(int j=0; j<tmp.size(); j++){
			char ch;
			ch = tmp[j];			

			if(ch == '('){
				inbraket = true;
				continue;
			}else{
				if(ch == ')'){
					k++;
					inbraket = false;
				}else{
					pattern[k].push_back(ch);
					if(inbraket == false){
						k++;
					}
				}
			}					
		}

		patterns.push_back(pattern);
	}

	int ans[501];
	for(int i=0; i<n; i++){
		ans[i] = 0;
	}

	for(int i=0; i<d; i++){
		bool mask[501];
		for(int z=0; z < n; z++){
			mask[z] = true;
		}
		for(int j = 0; j<alphabet[i].size(); j++){
			for(int z = 0; z < n; z++){
				vector<char> check = patterns[z][j];
				bool t = false;
				for(int w = 0; w < check.size(); w++){
					if(check[w] == alphabet[i][j]){
						t = true;
						break;
					}
				}
				if(t == false){
					mask[z] = false;
				}
			}
		}
		for(int q = 0; q < n; q++){
			if(mask[q]){
				ans[q]++;
			}
		}
	}

	for(int i = 0; i < n; i++){
		printf("Case #%i: %i\n", i+1, ans[i]);
	}

	return 0;
}