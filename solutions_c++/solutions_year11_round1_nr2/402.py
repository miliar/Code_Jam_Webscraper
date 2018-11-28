#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <tr1/unordered_set>
#include <tr1/unordered_map>
#include <gmpxx.h>

using namespace std;
using namespace tr1;

typedef mpz_class number;

int main () {
	int T, t = 1;
	
	cin >> T;
	while (T--) {
		int n, m;
		
		printf("Case #%d:",t++);
		
		cin >> n >> m;
		
		vector <string> D(n);
		
		for (int i=0; i < n; i++) {
			cin >> D[i];
		}
		
		while (m--) {
			string w;
			
			cin >> w;
			
			int ans = -1, best = -1;
			
			for (int k=0; k < n; k++) {
				
				int misses = 0;
				int qtde = D[k].length();
				vector <bool> hidden(qtde, true);
				vector <bool> valid(n);
				
				for (int j=0; j < n; j++) {
					valid[j] = (D[k].length() == D[j].length());
				}
				
				for (int i=0; i < 26; ++i) {
					char c = w[i];
					bool use = false;
					
					for (int j=0; j < n && !use; ++j) {
						
						if (!valid[j]) {
							continue;
						}
						
						for (int p=0; p < D[j].length(); ++p) {
							if (hidden[p] && D[j][p] == c) {
								use = true;
								break;
							}
						}
					}
					
					if (!use) {
						continue;
					}
					
					bool found = false;
					
					for (int p=0; p < D[k].length(); p++) {
						if (D[k][p] == c) {
							found = true;
							hidden[p] = false;
							qtde--;
						}
					}
					
					if (!found) {
						misses++;
					}
					
					for (int j=0; j < n; ++j) {
						
						if (!valid[j]) {
							continue;
						}
						
						for (int p=0; p < D[j].length(); ++p) {
							if (!hidden[p] && D[j][p] != D[k][p]) {
								valid[j] = false;
								break;
							}
							if (hidden[p] && D[j][p] == c) {
								valid[j] = false;
								break;
							}
						}
					}
					
					if (qtde == 0) {
						break;
					}
				}
				
				if (misses > best) {
					best = misses;
					ans = k;
				}
			}
			
			printf(" %s", D[ans].c_str());
		}
		
		puts("");
	}
	
	return 0;
}
