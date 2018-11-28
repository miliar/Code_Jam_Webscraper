#include <iostream>
#include <cstdio>

using namespace std;

const int N = 100;
int n, k, tr, tb;
char s[N][N], w[N][N];


void init(){
    scanf("%d%d",&n, &k);
    for (int i = 0; i < n; ++i){
        scanf("%s",s[i]);
    } 
}

void run(){
    //printf("%d %d\n",n ,k ); 
    tr = 0;
    tb = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) 
            w[j][n - i - 1] = s[i][j];
    for (int j = 0; j < n; ++j){
        string tmp = ""; 
        for (int i = n - 1; i >= 0; --i){
            if (w[i][j] != '.') tmp += w[i][j];
        } 
        for (int i = n - 1; i >= 0; --i) w[i][j] = '.';
        int now = n - 1;
        for (int i = 0; i < tmp.size(); ++i){
            w[now][j] = tmp[i];
            now--;
        }
    }
    
    for (int i = 0; i < n; ++i){
        int tot = 0;
        for (int j = 0; j < n; ++j){
            if (w[i][j] == 'R'){
               tot++;
               if (tot >= k) tr++;
            }
            else tot = 0;
        }
    }
    
    for (int i = 0; i < n; ++i){
        int tot = 0;
        for (int j = 0; j < n; ++j){
            if (w[i][j] == 'B'){
               tot++;
               if (tot >= k) tb++;
            }
            else tot = 0;
        }
    }
    //printf("%d %d\n",tr, tb);
    
    
    for (int j = 0; j < n; ++j){
        int tot = 0;
        for (int i = 0; i < n; ++i){
            if (w[i][j] == 'R'){
               tot++;
               if (tot >= k) tr++;
            }
            else tot = 0;
        }
    }
    
    for (int j = 0; j < n; ++j){
        int tot = 0;
        for (int i = 0; i < n; ++i){
            if (w[i][j] == 'B'){
               tot++;
               if (tot >= k) tb++;
            }
            else tot = 0;
        }
    }
    
    //printf("%d %d\n",tr, tb);
    
    
    for (int i = 0; i <= n - 1; ++i){
        int tot = 0;
        for (int j = 0; j <= i; ++j){
            if (w[j][i - j] == 'R'){
               tot++;
               if (tot >= k) tr++;
            }
            else tot = 0;
        }
    }
    for (int i = n; i <= 2 * (n - 1); ++i){
        int tot = 0;
        for (int j = n - 1; j >= i - n - 1; --j){
            if (w[j][i - j] == 'R'){
               tot++;
               if (tot >= k) tr++;
            }
            else tot = 0;
        }
    }
    
    for (int i = 0; i <= n - 1; ++i){
        int tot = 0;
        for (int j = 0; j <= i; ++j){
            if (w[j][i - j] == 'B'){
               tot++;
               if (tot >= k) tb++;
            }
            else tot = 0;
        }
    }
    for (int i = n; i <= 2 * (n - 1); ++i){
        int tot = 0;
        for (int j = n - 1; j >= i - n - 1; --j){
            if (w[j][i - j] == 'B'){
               tot++;
               if (tot >= k) tb++;
            }
            else tot = 0;
        }
    }
    
    for (int i = 0; i < n; ++i){
        int tot = 0;
        int now = i;
        for (int j = 0; j < n - i; ++j){
            if (w[now][j] == 'R'){
                tot++;
                if (tot >= k) tr++;
            }
            else tot = 0;
            now++;
        }
    }
    for (int i = 0; i < n; ++i){
        int tot = 0;
        int now = n - 1 - i;
        for (int j = 0; j <= i; ++j){
            if (w[j][now] == 'R'){
               tot++;
               if (tot >= k) tr++;
            }
            else tot = 0;
            now++;
        }
    }
    
    for (int i = 0; i < n; ++i){
        int tot = 0;
        int now = i;
        for (int j = 0; j < n - i; ++j){
            if (w[now][j] == 'B'){
                tot++;
                if (tot >= k) tb++;
            }
            else tot = 0;
            now++;
        }
    }
    for (int i = 0; i < n; ++i){
        int tot = 0;
        int now = n - 1 - i;
        for (int j = 0; j <= i; ++j){
            if (w[j][now] == 'B'){
               tot++;
               if (tot >= k) tb++;
            }
            else tot = 0;
            now++;
        }
    }
    
    //printf("%d %d\n",tr, tb);
    
    
    if (tb > 0 && tr > 0){
         puts("Both");
    }
    else if (tb == 0 && tr == 0){
         puts("Neither");
    }
    else if (tb > 0){
         puts("Blue");
    }
    else puts("Red");
}

int main(){
    int t;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for (int i = 1; i <= t; ++i){
        printf("Case #%d: ",i);
        init();
        run();
    }
    return 0;
}
