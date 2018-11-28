#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

const char base[9] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F', 0};
char comb['Z'+1]['Z'+1];
bool opos['Z'+1]['Z'+1];
char x[200];

int main(void) {
	int t;
	scanf("%d",&t);
	vector<char> lst;
	lst.push_back(0);
	lst.reserve(101);
	for (int tc=1; tc<=t; ++tc) {
					for (int a='A'; a<='Z'; ++a) for (int b='A'; b<='Z'; ++b) comb[a][b] = 0;
					for (int a='A'; a<='Z'; ++a) for (int b='A'; b<='Z'; ++b) opos[a][b] = false;
					
					lst.resize(1);
					int c;
					scanf("%d",&c);
					while (c--) {
									scanf("%s",x);
									comb[(int)x[0]][(int)x[1]] = comb[(int)x[1]][(int)x[0]] = x[2];
					}
					scanf("%d",&c);
					while (c--) {
									scanf("%s",x);
									opos[(int)x[0]][(int)x[1]] = opos[(int)x[1]][(int)x[0]] = true;
					}
					scanf("%d%s",&c,x);
					for (int i=0; i<c; ++i) {
									char t = comb[(int)lst.back()][(int)x[i]];
									if (t) {
													lst.back() = t;
									} else {
												 lst.push_back(x[i]);
												 for (int oi=0; oi<8; ++oi) {
																if (opos[(int)base[oi]][(int)x[i]] && find(lst.begin(),lst.end(),base[oi]) != lst.end()) {
																				lst.resize(1);
																				break;
																}
												 }
									}
					}
					printf("Case #%d: [",tc);
					for (int i=1; i<(int)lst.size()-1; ++i) {
									printf("%c, ",lst[i]);
					}
					if (lst.back()) {
									printf("%c",lst.back());
					}
					printf("]\n");
	}
	return 0;
}
