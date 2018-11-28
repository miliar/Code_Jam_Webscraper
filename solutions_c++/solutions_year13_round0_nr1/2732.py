#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
    int t;
    char a[5][5];
    scanf("%d",&t);
    int sum,flag=0,count=0;
    for(int k=0;k<t;k++){
        flag=0;
        count=0;
        for(int p=0;p<4;p++)
            scanf("%s",a[p]);
            
        for(int i=0;i<4;i++){
            sum=0;
            for(int j=0;j<4;j++){
                 //scanf("%c  ",&a[i][j]);
                 sum+=(int)(a[i][j]);
                 if(a[i][j]=='.')
                    count++;
            }
            if(flag==0){
                if(sum ==348 || sum==352){
                    flag=1;
                    printf("Case #%d: X won\n",k+1);
                }
                else if(sum == 321 || sum==316){
                    flag=1;
                    printf("Case #%d: O won\n",k+1);
                }
            }
        }
        int p=0;
        while(flag==0 && p<4){
            int sum_tmp=0;
            sum_tmp=a[0][p]+a[1][p]+a[2][p]+a[3][p];
            if(sum_tmp == 348 || sum_tmp==352){
                flag=1;
                printf("Case #%d: X won\n",k+1);
            } 
            else if(sum_tmp == 321 || sum_tmp==316){
                    flag=1;
                    printf("Case #%d: O won\n",k+1);
            }
            p++;
        }
        int sum2=0;
        if(flag==0){
            sum2=a[0][0]+a[1][1]+a[2][2]+a[3][3];
            if(sum2 == 348 || sum2==352){
                flag=1;
                printf("Case #%d: X won\n",k+1);
            } 
            else if(sum2 == 321 || sum2==316){
                    flag=1;
                    printf("Case #%d: O won\n",k+1);
            }        
        }
        if(flag==0){
            sum2=a[0][3]+a[1][2]+a[2][1]+a[3][0];
            if(sum2 == 348 || sum2==352){
                flag=1;
                printf("Case #%d: X won\n",k+1);
            } 
            else if(sum2 == 321 || sum2==316){
                    flag=1;
                    printf("Case #%d: O won\n",k+1);
            }        
        }
        if(flag==0){
            if(count==0)
                printf("Case #%d: Draw\n",k+1);
            else
                printf("Case #%d: Game has not completed\n",k+1);
            flag=1;
        }
        
    }
return 0;
}