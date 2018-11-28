#include <iostream>
#include <cassert>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>

using namespace std;

char transf[255][255];
bool oposed[255][255];
int main () {
	int T;
	scanf("%d", &T);
	for(int caso = 0; caso < T; caso++) {
		memset(transf,0,sizeof(transf));
		memset(oposed,0,sizeof(oposed));
		int C,O;
		scanf("%d", &C);
		for(int i = 0; i < C; i++) {
			char c1,c2,c3;
			scanf(" %c%c%c ", &c1, &c2, &c3);
			transf[c1][c2]=transf[c2][c1]=c3;
		}
		scanf("%d", &O);
		for(int i = 0; i < O; i++) {
			char c1,c2;
			scanf(" %c%c ", &c1, &c2);
			oposed[c1][c2]=oposed[c2][c1]=true;
		}
		int N;
		string str,res;
		scanf("%d", &N);
		cin >> str;
		for(int i = 0; i < str.size(); i++) {
			res.push_back(str[i]);
			bool changed = true;
			while(res.size()>=2 and changed) {
				changed = false;
				char tr = transf[res[res.size()-1]][res[res.size()-2]];
				if(isalpha(tr)) {
					res.erase(res.begin()+res.size()-1);
					res.erase(res.begin()+res.size()-1);
					res.push_back(tr);
					changed = true;
				} else {
					for(int j = 0; j < int(res.size())-1; j++){
						if(oposed[res[j]][res[int(res.size())-1]]) {
							res.clear();
							changed = true;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: ", caso+1);
		if(res.size()) {
			printf("[%c", res[0]);
			for(int i = 1; i < res.size(); i++) {
				printf(", %c",res[i]);
				assert(res[i]>='A' and res[i]<='Z');
			}
			printf("]\n");
		} else printf("[]\n");
	}
	return 0;
}

