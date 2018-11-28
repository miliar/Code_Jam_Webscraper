#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<map>
#include<set>

using namespace std;

int mat[1100][110];
map<string,int> searche;
char leitor[200];
int n;
int s, q;

int main(){
    int t;
    int i, j;
    int best;
    scanf("%d", &n);
    for (t=0; t<n; t++) {
        scanf("%d\n", &s);
        for (i=0; i<s; i++) {
            gets(leitor);
            string ss(leitor);
            searche[ss] = i;
        }
        for (i=0; i<s; i++) {
            mat[0][i] = 0;
        }
        scanf("%d\n", &q);
        for (j=1; j<=q; j++) {
            best = 100000;
            for (i=0; i<s; i++) {
                best = min(best, mat[j-1][i]+1);
            }
            for (i=0; i<s; i++) {
                mat[j][i] = min(best, mat[j-1][i]);
            }
            gets(leitor);
            string ss(leitor);
            if (searche.count(ss)) {
                mat[j][searche[ss]] = 100000;
            }
        }
        best = 100000;
        for (i=0; i<s; i++) {
            best = min(best, mat[j-1][i]);
        }
        printf("Case #%d: %d\n", t+1, best);
    }
}
