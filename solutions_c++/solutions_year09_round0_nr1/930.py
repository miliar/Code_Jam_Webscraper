#include<cstdio>
#include<string>
#include<iostream>
#include<vector>

using namespace std;

int L, D, N;
vector<string> V;
char str[1000];
int flag[20][26];
int main() {
	int cases = 1;
	while( cin >> L >> D >> N ) {
		V.clear();
		int i, j;
		for(i=0;i<D;i++) {
			scanf("%s", str);
			string s = str;
			V.push_back(s);
		}
		for(cases=1;cases<=N;cases++) {
			scanf("%s", str);
			string s = str;
			for(i=0;i<L;i++)
			 for(j=0;j<26;j++)
			  flag[i][j] = 0;

			j = 0;
			for(i=0;i<L;i++) {
              if( s[j] == '(') {
				 j++;
				 for(; s[j]!=')'; j++)
				   flag[i][ s[j] - 'a'] = 1;
			  }
			  else {
				 flag[i][ s[j] - 'a'] = 1;
			  }
			  j++;
			}
			int res = 0;
			for(i=0;i<D;i++) {
			  for(j=0;j<L;j++)
			    if( flag[j][ V[i][j] - 'a'] == 0 ) break;
			  if( j == L ) res++;
			}
			printf("Case #%d: %d\n", cases, res);
		}
	}
}