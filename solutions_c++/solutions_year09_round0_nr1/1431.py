#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <deque>
#include <set>
#include <algorithm>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>

using namespace std;

int main() {
	char *line;
	line = (char *) malloc(sizeof(char) * 1000);
	int i, j, k, l, m, n, o, p, t, q, s, r, v;
	char words[5005][20];
	set<int> conj[20][30];
		
	scanf(" %d %d %d ", &l, &m, &n);
	for (i = 0; i < 20; i++) {
		for (j = 0; j < 30; j++){
			conj[i][j].clear();	
		}
	}
	for (i = 0; i < m; i++) {
		scanf(" %s ", words[i]);
		s = strlen(words[i]);
		for (j = 0; j < s; j++) {
			conj[j][words[i][j]-'a'].insert(i);
		}
	}
	
	for (o = 1; o <= n; o++) {
		scanf(" %s ", line);
		s = strlen(line);
		i = 0;
		j = 0;
		set<int> resp;
		resp.clear();
		for (k = 0; k < m; k++) {
			resp.insert(k);	
		}
		while(i < s) {
			k = 0;
			set<int> resp2;
			resp2.clear();
			for (k = 0; k < m; k++) {
				resp2.insert(k);	
			}
			
			if (line[i] == '(') {
				i++;
				while (line[i] != ')') {
					if (!conj[j][line[i]-'a'].empty()) {
						for (set<int>::iterator it = conj[j][line[i]-'a'].begin(); it != conj[j][line[i]-'a'].end(); it++) {
							if (resp2.find(*it) != resp2.end()) {
								resp2.erase(*it);
							}
						}
					}
					i++;				
				}	
			} else {
				if (!conj[j][line[i]-'a'].empty()) {
					for (set<int>::iterator it = conj[j][line[i]-'a'].begin(); it != conj[j][line[i]-'a'].end(); it++) {
						if (resp2.find(*it) != resp2.end()) {
							resp2.erase(*it);
						}
					}
				}
			}
			i++;
			j++;
			
			for (set<int>::iterator it = resp2.begin(); it != resp2.end(); it++) {
				resp.erase(*it);
			}
			
			if (resp.size() == 0) {
				break;	
			}
		}
			printf("Case #%d: %d\n", o, resp.size());
	} 
	return 0;	
}
