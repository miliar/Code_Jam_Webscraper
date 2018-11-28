#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<bitset>
#include<map>
#include<set>
#include<climits>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cctype>
#include<queue>
#include<sstream>
#include <stack>
#include <list>
#include <numeric>
#define INT_MAX 2147483647
#define INT_MIN -2147483647 //2^31-1
#define pi acos(-1.0)
#define N 1000000
#define LL unsigned long long
#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)
#define assign(x,n) x=(int*)calloc(n,4)
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define SWAP(a,b) a= a^b, b=a^b, a=a^b
typedef  long long int ull;
using namespace std;

int main()
{
//freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);

int t,tc=1;scanf("%d\n",&t);

while(t--){
           int i,j,k,f=0;
           char arr[10][10]={{}};
           char x;
           for(i=0;i<4;i++)gets(arr[i]);
           string s;
           getline(cin,s);
           
           for(i=0;i<4;i++){
                            if(arr[i][0]!='T'){
                                               x=arr[i][0];if(x=='.')continue;
                                               if(arr[i][1]!=x && arr[i][1]!='T')continue;                                       
                                               if(arr[i][2]!=x && arr[i][2]!='T')continue;   
                                               if(arr[i][3]!=x && arr[i][3]!='T')continue;   
                                               printf("Case #%d: %c won\n",tc++,x);f=1;
                                               goto end;
                                               }
                            else{
                                   x=arr[i][1];  if(x=='.')continue;                                
                                  if(arr[i][2]!=x )continue;   
                                  if(arr[i][3]!=x)continue;   
                                  printf("Case #%d: %c won\n",tc++,x);f=1;
                                               goto end;                                 
                                 }
           
                            }
                            
            for(j=0;j<4;j++){
                            if(arr[0][j]!='T'){
                                               x=arr[0][j];if(x=='.')continue;
                                               if(arr[1][j]!=x && arr[1][j]!='T')continue;                                       
                                               if(arr[2][j]!=x && arr[2][j]!='T')continue;   
                                               if(arr[3][j]!=x && arr[3][j]!='T')continue;   
                                               printf("Case #%d: %c won\n",tc++,x);f=1;
                                               goto end;
                                               }
                            else{
                                   x=arr[1][j];  if(x=='.')continue;                                
                                  if(arr[2][j]!=x )continue;   
                                  if(arr[3][j]!=x)continue;   
                                  printf("Case #%d: %c won\n",tc++,x);f=1;
                                               goto end;                                 
                                 }
           
                            }
           
           if(arr[0][0]!='T'){
                              x=arr[0][0];if(x=='.')goto out1;
                              if(arr[1][1]==x || arr[1][1]=='T')if(arr[2][2]==x || arr[2][2]=='T')if(arr[3][3]==x || arr[3][3]=='T'){
                                              printf("Case #%d: %c won\n",tc++,x);f=1;
                                               goto end;}
                              }
           else {
                x=arr[1][1];if(x=='.')goto out1;
                         if(arr[2][2]==x)if(arr[3][3]==x){
                                              printf("Case #%d: %c won\n",tc++,x);f=1;
                                               goto end;}
                }
           
           out1:;
           if(arr[0][3]!='T'){
                              x=arr[0][3];if(x=='.')goto out2;
                              if(arr[1][2]==x || arr[1][2]=='T')if(arr[2][1]==x || arr[2][1]=='T')if(arr[3][0]==x || arr[3][0]=='T'){
                                              printf("Case #%d: %c won\n",tc++,x);f=1;
                                               goto end;}
                              }
           else {
                x=arr[1][2];if(x=='.')goto out2;
                         if(arr[2][1]==x)if(arr[3][0]==x){
                                              printf("Case #%d: %c won\n",tc++,x);f=1;
                                               goto end;}
                }
           out2:;
           if(!f){
                  for(i=0;i<4;i++)
                  for(j=0;j<4;j++)if(arr[i][j]=='.'){
                                                     printf("Case #%d: Game has not completed\n",tc++);f=1;
                                                    goto end;
                                                     }
                  }
            printf("Case #%d: Draw\n",tc++);
            
            end: ;
           }
           
//system("pause");
return 0;
}

