#include <iostream>
#include <cstdio>

using namespace std;

const int N = 50;
int n, k;
int state[N], plug[N];

void init(){
    scanf("%d%d",&n, &k);     
}

void run(){
    memset(state, 0, sizeof(state));
    memset(plug, 0, sizeof(plug));
    plug[0] = 1;
    for (int i = 0; i < k; ++i){
        for (int j = 0; j < n; ++j){
            if (plug[j]){
               state[j] = 1 - state[j];
            }
            else{
               break;  
            }
        }
        int p = -1;
        //printf("%d %d\n",plug[0], state[0]);
        for (int j = 0; j < n - 1; ++j)
            if (plug[j] && state[j]) plug[j + 1] = 1;
            else{
                 if (plug[j] == 0){
                    p = j;
                    break;
                 }else{
                    p = j + 1;
                    break;   
                 }
            }
        if (p != -1){
           if (p == 0) p = 1;   
           for (int j = p; j < n; ++j) plug[j] = 0;
        }
        //printf("T = %d\n",i + 1);
        //for (int j = 0; j < n; ++j) printf("%d",state[j]);
        //puts("");
        //for (int j = 0; j < n; ++j) printf("%d",plug[j]);
        //puts("");
        //puts("");
    }
    
    if (state[n - 1] && plug[n - 1]) puts("ON");
    else puts("OFF"); 
}

void run2(){
    int maxn = (1 << n) - 1;
    if (k < maxn){
       puts("OFF");
    } 
    else if ((k - maxn) % (maxn + 1) == 0){
       puts("ON");  
    }
    else puts("OFF");
}

int main(){
    int t;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for (int i = 0; i < t; ++i){
        printf("Case #%d: ",i + 1);
        init();
        //run();
        run2();
    }
    return 0;
}
