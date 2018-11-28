#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>

using namespace std;

const char * w = "welcome to code jam";

int N;

int qt[50][600];
char buffer[600];

int main(void){
	int n;
	scanf("%d\n",&n);
	string s;
	N = strlen(w);

	for(int p = 0; p < n; p++){
		memset(qt,0,sizeof(qt));
		fgets(buffer,sizeof(buffer), stdin);
		s = string(buffer);
		int sz = s.size();

		qt[0][0] = (w[0] == s[0]);

		for(int i = 1; i < sz; i++){
			qt[0][i] = qt[0][i-1] + (w[0] == s[i]);
		}

		for(int i = 1; i < N; i++){
			for(int j = 1; j < sz; j++){
				qt[i][j] = qt[i][j-1];
				if(w[i] == s[j]){
					qt[i][j] += qt[i-1][j-1];

				}
				qt[i][j] = qt[i][j] % 10000;
				//printf("qt[%d][%d] = %d\n", i, j, qt[i][j]);
			}
		}

		printf("Case #%d: %04d\n",p+1, qt[N-1][sz-1] % 10000);
	}
}
