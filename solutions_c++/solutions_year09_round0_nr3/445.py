#include <iostream>
using namespace std;
char line[1000];
char match[1000]="welcome to code jam";
int ans[1000][19];
int main() {
    int t = 0;
    int T; scanf("%d",&T); gets(line); while (T--) {t++;
        memset(ans,0,sizeof(ans));
        gets(line);
        // let ans[i][j] = number of ways 
        int N = strlen(line);
        for (int i=N-1; i>=0; i--) {
            for (int j=0; j<19; j++) {
                ans[i][j]=(i==N-1?0:ans[i+1][j]);
                // looking for letter match[j]
                if (match[j]==line[i]) {
                    ans[i][j] = (ans[i][j]+(j==18?1:(i==N-1?0:ans[i+1][j+1])))%10000;
                }
            }
        }
        printf("Case #%d: %04d\n",t,ans[0][0]);
    }
}
