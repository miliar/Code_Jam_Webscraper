#define maxl 16
#define maxd 5010
#define maxn 510
#define lts 26
#include <iostream>
using namespace std;
int L, D, N;
char dict[maxd][maxl];
char s[maxl*lts];
int point[maxd];

void init(){
    scanf("%d%d%d",&L,&D,&N);
    for (int i=0;i<D;i++) scanf("%s",dict[i]);
}

void process(int x){
    int i, j;
    memset(point, 0, sizeof point);
    scanf("%s",s);
    int len = strlen(s), pos = 0;
    for (i=0;i<len;i++){
        if (s[i] == '(') {
            for (j=i+1;s[j]!=')';j++)
                for (int k=0;k<D;k++) if (dict[k][pos]==s[j]) point[k]++;
            i = j;
        } else  for (int k=0;k<D;k++) if (dict[k][pos]==s[i]) point[k]++;
        pos++;
    }
    int ans=0;
    for (int i=0;i<D;i++) if (point[i] == L) ans++;
    printf("Case #%d: %d\n",x,ans);
}

int main(){
    init();
    for (int i=0;i<N;i++) process(i+1);
}
