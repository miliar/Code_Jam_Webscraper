#include <stdio.h>

int main(){
    char arr[7][7];
    int ans[7][7],sum[12];
    char trash,m;
    int a,marka,markb,state;
    freopen("A-small-attempt3.in","r",stdin);
    freopen("res.out","w",stdout);
    scanf("%d",&a);
    for(int u = 1; u <= a;u++){
        state = 1;
        scanf("%c",&trash);
        for(int i = 0; i < 4;i++){
            for(int j = 0; j < 4;j++){
                scanf("%c",&arr[i][j]);
                if(arr[i][j] == 'T'){
                     marka = i;
                     markb = j;
                     ans[i][j] = 0;
                }
                else if( arr[i][j] == 'O') ans[i][j] = 1;
                else if( arr[i][j] == 'X') ans[i][j] = -1;
                else {
                    ans[i][j] = 0;
                    state = 0;
                }
            }
            scanf("%c",&trash);
        }
        
        for(int i = 0; i < 4;i++){
            for(int j = 0; j < 4;j++){
                printf("%c",arr[i][j]);
            }    
            printf("\n");
        }
        printf("\n");
        int ct = 0;
        int k;
        for(int i = 0; i < 4; i++){
            sum[ct] = 0;
            k = 0;
            for(int j = 0; j < 4;j++){
                if(i == marka && j == markb){
                k = 1;
                }   
                sum[ct] = sum[ct] + ans[i][j];   
            }
            if( k == 1){
                if(sum[ct] == 3) sum[ct]++;
                else if(sum[ct] == -3) sum[ct]--;
            }
            ct++;
        }
        for(int j = 0; j < 4; j++){
            sum[ct] = 0;
            k = 0;
            for(int i = 0; i < 4;i++){
                if(i == marka && j == markb){
                    k = 1;
                }
                sum[ct] = sum[ct] + ans[i][j];
                
                
            }
            if( k == 1){
                    if(sum[ct] == 3) sum[ct]++;
                    else if(sum[ct] == -3) sum[ct]--;
                }
            
            ct++;
        }
        sum[ct] = 0;
        k = 0;
        for(int i = 0; i < 4; i++){
            if(i == marka && i == markb){
                    k = 1;
            }
            sum[ct] = sum[ct] + ans[i][i];
        }
        if( k == 1){
            if(sum[ct] == 3) sum[ct]++;
            else if(sum[ct] == -3) sum[ct]--;
        }
        ct++;
        sum[ct] = 0;
        k = 0;
        for(int i = 3,j=0; i >= 0; i--,j++){
            if(i == marka && j == markb){
                    k = 1;
            }
            sum[ct] = sum[ct] + ans[i][j];
            
        }
        if( k == 1){
                    if(sum[ct] == 3) sum[ct]++;
                    else if(sum[ct] == -3) sum[ct]--;
        }
        int r = 1;
        //for(int i = 0; i < 10; i++) printf("%d\n",sum[i]);
        printf("Case #%d: ",u);
        for(int i = 0; i < 10;i++){
            if(sum[i] == 4){
                 printf("O won\n");
                 r = 0;
                 break;
            }
            else if(sum[i] == -4){
                 printf("X won\n");
                 r = 0;
                 break;
            }
        }
        
        if( r == 1){
           if( state == 0){
                 printf("Game has not completed\n");
            }
            else{
                 printf("Draw\n");
            }
        }
        
    }
    
    return 0;
}
