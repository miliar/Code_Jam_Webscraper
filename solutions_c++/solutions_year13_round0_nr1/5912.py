#include<iostream>
#include<cstdio>
#include<string>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<climits>
using namespace std; 
#define rep(i,n) for(i=0; i<(n); i++)
#define reph(i,n,m) for(i=(n); i<=(m); i++)//正循环的
#define repd(i,n,m) for(i=(n); i>=(m); i--) //负循环的 
#define fab(a) (a)>0?(a):0-(a)
#define max(a,b) (a)>(b)?(a):(b)
#define min(a,b) (a)<(b)?(a):(b)
#define ll __int64
#define arc(a) (a)*(a)
#define inf 10000000   //最大值的
#define exp 0.0000001     //浮点型的
#define N   5  //记录开的数组
char s[5][5];
int sign;
void fun(int sum)
{
               if(sum%4==0)
				{
                if(sum/4=='O')
                  sign=1;
                if(sum/4=='X')
                  sign=2;//x为2的   
				}
                sum-='T';
                if(sum%3==0)
                {
                if(sum/3=='O')
                  sign=1;
                if(sum/3=='X')
                sign=2;//x为2的  
            }
} 
int main()
{
    int T,i,j;
    scanf("%d",&T);
    int ror;
    reph(ror,1,T)
    {
        reph(i,0,3)
         scanf("%s",s[i]);
        int sum=0;
        sign=0;
        reph(i,0,3)
        {
            sum=0;
            reph(j,0,3) 
                sum+=s[i][j]; 
            fun(sum);
            sum=0;
            reph(j,0,3) 
                sum+=s[j][i]; 
            fun(sum); 
            if(sign!=0)
              break;
        }
        if(sign==0)
        {
            sum=0;
            reph(i,0,3) 
                sum+=s[i][i]; 
            fun(sum);
            sum=0;
            reph(i,0,3)
             sum+=s[i][3-i];
            fun(sum);
        }
        if(sign==0)
        {
            reph(i,0,3)
             reph(j,0,3)
              if(s[i][j]=='.')
               break;
            if(i==4 && j==4)
             sign=3;
        }
        printf("Case #%d: ",ror);
        if(sign==1)
          printf("O won\n");
        if(sign==2)
         printf("X won\n");
         if(sign==3)
          printf("Draw\n");
        if(sign==0)
         printf("Game has not completed\n");
    }
    return 0;
} 
