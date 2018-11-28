#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
using namespace std;
char in[10][10];
int main(){
    
    int n,m,i,j,k,stat,sum,check;
    
    
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    
    scanf("%d",&n);
    for(k=1;k<=n;k++)
       {
        stat = 0;
        
        
        for(i=1;i<=4;i++)
           {
            scanf("%s",&in[i][1]);
           }
        //printf("case %d \n",k);
        /*for(i=1;i<=4;i++)
           {
            printf("%s\n",in[i]);
           }*/
        
        printf("Case #%d: ",k);
        /// X won 1  -- O won 2 -- draw 3 ///
        sum = 0;
        check = 0;
        stat = 0;
        for(i=1;i<=4;i++)
           {
            sum = 0;
            for(j=1;j<=4;j++)
                if(in[i][j] == 'X' || in[i][j] == 'T') sum++;
            if(sum == 4)
                stat = 1;
           }   
        for(j=1;j<=4;j++)
           {
            sum = 0;
            for(i=1;i<=4;i++)
                if(in[i][j] == 'X' || in[i][j] == 'T') sum++;
            if(sum == 4)
                stat = 1;
           }
        sum = 0;
        for(i=1;i<=4;i++)
           if(in[i][i] == 'X' || in[i][i] == 'T') sum++;
        if(sum == 4)
            stat = 1;
    
        sum = 0;
        for(i=1;i<=4;i++)
           if(in[4-i+1][i] == 'X' || in[4-i+1][i] == 'T') sum++;
        if(sum == 4)
            stat = 1;
        
        if(stat == 1)
           {
            printf("X won\n");
            continue;
           }
        
        //////// O /////////
        for(i=1;i<=4;i++)
           {
            sum = 0;
            for(j=1;j<=4;j++)
                if(in[i][j] == 'O' || in[i][j] == 'T') sum++;
            if(sum == 4)
                stat = 2;
           }
        if(check)continue;
        
        for(j=1;j<=4;j++)
           {
            sum = 0;
            for(i=1;i<=4;i++)
                if(in[i][j] == 'O' || in[i][j] == 'T') sum++;
            if(sum == 4)
                stat = 2;
           }
        sum = 0;
        for(i=1;i<=4;i++)
           if(in[i][i] == 'O' || in[i][i] == 'T') sum++;
        if(sum == 4)
            stat = 2;
        
        sum = 0;
        for(i=1;i<=4;i++)
           if(in[4-i+1][i] == 'O' || in[4-i+1][i] == 'T') sum++;
        if(sum == 4)
            stat = 2;
        
        if(stat == 2)
           {
            printf("O won\n");
            continue;
           }
        
        ////////////////
        check = 1;
        for(i=1;i<=4;i++)
           {
            for(j=1;j<=4;j++)
               {
                if(in[i][j] == '.')
                   {check = 0;
                    break;
                   }
               }
           }

        if(check) printf("Draw\n");
        else printf("Game has not completed\n");
        
        
       }
    
    
 scanf(" ");
 return 0;
}
