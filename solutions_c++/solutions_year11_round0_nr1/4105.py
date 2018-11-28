#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int tc, n;
int A[105];
char t[105];
int f[105][105];

int main(){
    freopen("A.txt","r",stdin);
    freopen("Aans.txt","w",stdout);
    cin >> tc;
    for (int TC = 1; TC <= tc; TC++){
        cin >> n;
        memset(f, 0x77, sizeof f);
        for (int i = 1; i <= n; i++){
            scanf(" %c %d ", &t[i], &A[i]);
        }
        t[0] = 'O';
        f[0][1] = 0;
        A[0] = 1;
        for (int i = 1; i <= n; i++){
            //position of O & B depends on sequence
            if (t[i] == 'O'){
               for (int j = 1; j <= 100; j++){
                   for (int k = 1; k <= 100; k++){
                       if (t[i-1] == 'O')
                          f[i][j] = min(f[i][j], f[i-1][k] + max(abs(A[i]-A[i-1])+1,abs(j-k)));
                       else{
                          f[i][j] = min(f[i][j], f[i-1][k] + max(abs(A[i]-k)+1, abs(A[i-1] - j)));
                       }
                   }
                   //cout << "O i " << i << " j " << j << " f " << f[i][j] << endl;
               }
            }else{
               for (int j = 1; j <= 100; j++){
                   for (int k = 1; k <= 100; k++){
                       if (t[i-1] == 'O'){
                          f[i][j] = min(f[i][j], f[i-1][k] + max(abs(j-A[i-1]),abs(A[i]-k)+1));
                       }else{
                          f[i][j] = min(f[i][j], f[i-1][k] + max(abs(j-k), abs(A[i]-A[i-1])+1));
                       }
                   }
                   //cout << "B i " << i << " j " << j << " f " << f[i][j] << endl;
               }
            }
        }
        int mint = 0x77777777;
        for (int i = 1; i <= 100; i++) mint = min(mint, f[n][i]);
        printf("Case #%d: %d\n", TC, mint);
    }
    return 0;
}
