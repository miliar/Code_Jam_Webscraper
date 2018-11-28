#include <stdio.h>
#include <string.h>
#include <vector>
int combine[256][256];
int oppose[256][256];
char change[10];
char target[110];
using namespace std;
vector <char> vec;
vector <char>::iterator last;
int main () {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,cs,C,D,N,i,j;
    scanf("%d",&T);
    for (cs = 1; cs <= T; cs++) {
        scanf("%d",&C);
        vec.clear();
        memset(combine,0,sizeof(combine));
        memset(oppose,0,sizeof(oppose));
        for (i = 0; i < C; i++) {
            scanf("%s",change);
            combine[change[0]][change[1]] = combine[change[1]][change[0]] = change[2];
        }
        scanf("%d",&D);
        for (i = 0; i < D; i++) {
            scanf("%s",change);
            oppose[change[0]][change[1]] = oppose[change[1]][change[0]] = 1;
        }
        scanf("%d",&N);
        scanf("%s",target);
        for (i = 0; i < N; i++) {
            char ch = target[i];
            if (vec.empty()) {
                vec.push_back(ch);
            } else {
                char nch = combine[ch][*(vec.end() - 1)];
                if (nch) {
                    vec.erase(vec.end() - 1);
                    vec.push_back(nch);
                } else {
                    vec.push_back(ch);
                    for (j = 0; j < vec.size() - 1; j++) {
                        if (oppose[vec[j]][ch]) {
                            vec.clear();
                            break;
                        }
                    }
                }
            }
        }
        printf("Case #%d: [",cs);
        int size = vec.size();
        for (int i = 0; i < size; i++) {
            printf("%c",vec[i]);
            if (i < size - 1) {
                printf(", ");
            }
        }
        puts("]");
    }
    return 0;
}
