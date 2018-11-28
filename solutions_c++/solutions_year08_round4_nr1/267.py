#include <stdio.h>
#include <stdlib.h>
#define oo 1000000
int tree[10001];
int change[10001];
int max_[10001][2];


int main() {
    int i,j,T,t,m,v;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d", &T); 
    for (t=1;t<=T;t++){
        scanf("%d%d",&m,&v);
        for (i = 1; i <= (m-1)/2; i++){
            scanf("%d%d", tree+i, change+i);
        }    
        for (; i <= m; i++){
            scanf("%d", tree+i);
            max_[i][0] = max_[i][1] = oo;
            max_[i][tree[i]] = 0;
        }    
        for (i = (m-1)/2; i >= 1; i--){
            max_[i][0] = max_[i][1] = oo;
            if (change[i] == 0){
                if (tree[i] == 1){
                    max_[i][0] <?= max_[2*i][1] + max_[2*i+1][0];
                    max_[i][0] <?= max_[2*i][0] + max_[2*i+1][0];
                    max_[i][0] <?= max_[2*i][0] + max_[2*i+1][1];
                    max_[i][1] <?= max_[2*i][1] + max_[2*i+1][1];
                }
                else{
                    max_[i][0] <?= max_[2*i][0] + max_[2*i+1][0];
                    max_[i][1] <?= max_[2*i][1] + max_[2*i+1][0];
                    max_[i][1] <?= max_[2*i][0] + max_[2*i+1][1];
                    max_[i][1] <?= max_[2*i][1] + max_[2*i+1][1];
                }         
            }  
            else{
                if (tree[i] == 1){
                    max_[i][0] <?= max_[2*i][1] + max_[2*i+1][0];
                    max_[i][0] <?= max_[2*i][0] + max_[2*i+1][0];
                    max_[i][0] <?= max_[2*i][0] + max_[2*i+1][1];
                    max_[i][1] <?= max_[2*i][1] + max_[2*i+1][1];
                    
                    max_[i][0] <?= max_[2*i][0] + max_[2*i+1][0] + 1;
                    max_[i][1] <?= max_[2*i][1] + max_[2*i+1][0] + 1;
                    max_[i][1] <?= max_[2*i][0] + max_[2*i+1][1] + 1;
                    max_[i][1] <?= max_[2*i][1] + max_[2*i+1][1] + 1;
                    
                }
                else{
                    max_[i][0] <?= max_[2*i][0] + max_[2*i+1][0];
                    max_[i][1] <?= max_[2*i][1] + max_[2*i+1][0];
                    max_[i][1] <?= max_[2*i][0] + max_[2*i+1][1];
                    max_[i][1] <?= max_[2*i][1] + max_[2*i+1][1];
                    
                    max_[i][0] <?= max_[2*i][1] + max_[2*i+1][0] + 1;
                    max_[i][0] <?= max_[2*i][0] + max_[2*i+1][0] + 1;
                    max_[i][0] <?= max_[2*i][0] + max_[2*i+1][1] + 1;
                    max_[i][1] <?= max_[2*i][1] + max_[2*i+1][1] + 1;
                }   
            }      
        }    
        if (max_[1][v] < oo)
            printf("Case #%d: %d\n",t,max_[1][v] );
        else
            printf("Case #%d: IMPOSSIBLE\n",t);
    }     
    return 0; 
}

