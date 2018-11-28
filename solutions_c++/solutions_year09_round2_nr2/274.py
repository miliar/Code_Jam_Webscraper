#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>

#define REP(AA,BB) for(AA=0; AA<BB; ++AA)
#define FOR(AA,BB,CC) for(AA=BB; AA<CC; ++AA)
#define FC(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end(); ++BB)

using namespace std;

char c[110];

string last(string a) {
	sort(a.begin(),a.end());
	reverse(a.begin(),a.end());
	return a;
}

string first(string a) {
	sort(a.begin(), a.end());
	return a;
}

string usu(string a, char x) {
	int i;
	REP(i,a.size()) {
		if(a[i]==x)
			return a.substr(0,i)+(i<(int)a.size()-1?a.substr(i+1):"");
	}
	return a;
}

int main(void) {
	int t, T, i, j, k, n; char tmp;
	scanf("%d", &T);
	REP(t,T) {
		printf("Case #%d: ", t+1);
		scanf("%s", c); string S(c);
		if(last(S)==S) {
			string C=first(S);
			REP(i,C.size()) {
				if(C[i]!='0') {
					putchar(C[i]);
					C=C.substr(0,i)+(i<(int)C.size()-1?C.substr(i+1):"");
					break;
				}
			}
			printf("0%s\n", C.c_str());
		}
		else {
			string rem=S;
			REP(i,S.size()) {
				rem=usu(rem, S[i]);
				if((i<(int)S.size()-1?S.substr(i+1):string(""))!=last(rem))
					putchar(S[i]);
				else {
					tmp='9';
					REP(j,rem.size()) {
						if(rem[j]>S[i] && rem[j]<tmp)
							tmp=rem[j];
					}
					printf("%c%s\n", tmp, (first(usu(rem, tmp)+S.substr(i,1))).c_str());
					break;
				}
			}
		}
	}
	return 0;
}
		
