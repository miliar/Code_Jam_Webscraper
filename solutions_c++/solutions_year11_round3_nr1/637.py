#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int n, R,C;
int Case = 1;
int main() {
	scanf("%d", &n);
	while(n--) {
		scanf("%d %d", &R, &C);

        char M[R][C+5];

        for(int i = 0; i < R; ++i) {
            scanf("%s\n", M[i]);
        }

        bool imp = false;
        for(int i = 0; i < C - 1; ++i) {
            for(int j = 0; j < R - 1; ++j) {
                if(M[j][i] == '#') {
                    if(M[j+1][i] != '#' || M[j][i+1] != '#' || M[j+1][i+1] != '#') {
                        imp = true;
                        break;
                    }
                    M[j][i] = '/';
                    M[j+1][i] = '\\';
                    M[j][i+1] = '\\';
                    M[j+1][i+1] = '/';
                }
            }
            if(imp) break;
        }

        for(int i = 0; i < R; ++i) {
            for(int j = 0; j < C; ++j) {
                if(M[i][j] == '#') {
                    imp = true;
                    break;
                }
            }
            if(imp) break;
        }


        printf("Case #%d:\n", Case++);
        if(imp) {
            printf("Impossible\n");   
        } else {
            for(int i = 0; i < R; ++i) {
                printf("%s\n", M[i]);
            }
        }


	}
	return 0;
}
