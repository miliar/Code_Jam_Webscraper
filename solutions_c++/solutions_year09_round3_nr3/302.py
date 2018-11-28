#include <iostream>
using namespace std;
int p,q;
int list[10];
bool used[120];
int jc[6] = {0,1,2,6,24,120};

int getans(){
    memset(used, 0 , sizeof used);
    int ret = 0;
    for (int i=0;i<q;i++){
        used[list[i]] = true;
        for (int j=list[i]-1;j>=1;j--){
            if (used[j]) break;
            ret++;
        }
        for (int j=list[i]+1;j<=p;j++){
            if (used[j]) break;
            ret++;
        }
    }
    return ret;
}

int main(){
    int test;
    scanf("%d",&test);
    for (int c=1;c<=test;c++){
        scanf("%d%d",&p,&q);
        for (int i=0;i<q;i++) scanf("%d",&list[i]);
        int ans = 999999999;
        for (int i=0;i<jc[q];i++){
            next_permutation(list,list+q);
            int tmp = getans();
            if (tmp < ans) ans = tmp;
        }
        printf("Case #%d: %d\n",c,ans);
    }
}
