#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <string>
using namespace std;
char s[1011];
char dic[5005][18];
bool ca[17][255];
int main() {
    int L,D,N;
    freopen("out.txt", "w", stdout);
    scanf("%d%d%d", &L, &D, &N);
    for(int i=0; i<D; i++) {
        scanf("%s", dic[i]);
    }
    for(int v=1; v<=N; v++) {
        scanf("%s", s);
        int st=0;
        memset(ca, 0, sizeof(ca));
        for(int i=0; i<L; i++) {
            bool p = false;
            int k = 0;
            for(int j=st; s[j] != 0; j++) {
                if(s[j] == '(') {
                    p = true;
                }
                else if(s[j] >= 'a' && s[j] <= 'z') {
                    if(!p) {
                        ca[i][s[j]] = true;
                        st = j+1;
                        break;
                    }
                    else {
                        ca[i][s[j]] = true;
                    }
                }
                else if(s[j] == ')') {
                    st = j+1;
                    break;
                }
            }
        }
        int ans = 0;
        for(int t=0; t<D; t++) {
            bool find = true;
            for(int i=0; i<L && find; i++) {
                if(!ca[i][dic[t][i]]) find = false;
            }
            if(find) ans++;
        }
        printf("Case #%d: %d\n", v, ans);
    }
    return 0;
}
