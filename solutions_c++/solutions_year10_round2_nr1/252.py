#include<cstdio>
#include<cstring>

using namespace std;

const int MAXL = 500000;
const int MAXB = 255;

int tot,ans;
bool g[MAXL];
int trie[MAXL][MAXB];
char str[MAXL];

void init() {
    tot = 0;
    ans = 0;
    /*for(int i = 0 ; i < MAXL ; i++) {
        for(int j = 0 ; j < MAXB ; j++) {
            trie[i][j] = -1;
        }
    }*/
    //memset(trie,-1,sizeof(trie));
    for(int j = 0 ; j < MAXB ; j++) {
        trie[tot][j] = -1;
    }
    g[tot] = false;
    tot++;
}

void insert(bool flag) {
    int len = strlen(str);
    bool isCre = true;
    int k = 0;
    str[len] = '/';
    len++;
    str[len] = '\0';
    for(int i = 0 ; i < len ; i++) {
        int tmp = trie[k][int(str[i])];
        //printf("%d\n",k);
        if (tmp == -1) {
            //if (str[i] != '/') isCre = false;
            for(int j = 0 ; j < MAXB ; j++) {
                trie[tot][j] = -1;
            }
            trie[k][int(str[i])] = tot;
            g[tot] = false;
            tot++;
        }
        k = trie[k][int(str[i])]; 
        if (str[i] == '/' && flag && !g[k] && i != 0) {
            //printf("%s\n",str);
            ans++;
        } 
        g[k] = true;
    }
    //if (flag && !g[k]) {
        //g[k] = true;
        //ans++;
    //}
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t = 0 ; t < T ; t++) {
        int N,K;
        scanf("%d%d",&K,&N);
        init();
        for(int i = 0 ; i < K ; i++) {
            scanf("%s",str);
            insert(false);
        }
        for(int i = 0 ; i < N ; i++) {
            scanf("%s",str);
            insert(true);
        }
        printf("Case #%d: %d\n",t + 1 ,ans);
    }
    
    return 0;
}
