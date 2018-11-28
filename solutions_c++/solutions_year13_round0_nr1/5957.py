#include<stdio.h>
#include<iostream>
#include <string.h>
#include<math.h>
#define R return
#define FR(i,a,b) for(int i=a;i<b;i++)
#define RFR(i,a,b) for(int i=a;i>=b;i--)
#define SC(x) scanf("%d",&x)
#define SSC(x) scanf("%s",x)
#define LSC(x) scanf("%lld",&x)
#include<sstream>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<utility>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#define IN(i,j) a[i][j]
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
#define FUN(x) x==true)?1:0
#define SWAP(x,y,z) {z=x;x=y;y=z;}
#define mod 1000000003
using namespace std;

int main()
{
    int t,counter=1;
    cin>>t;
    while(t--){
               
               char s[4][4],ch[4][4];int a[4][4];
               FR(i,0,4){
                         FR(j,0,4)cin>>s[i][j];
                         }
               bool flag=false;
               int k=0;
               printf("Case #%d: ",counter++);
               FR(i,0,4){
                         k=0;
                         FR(j,0,4)k+=s[i][j]-65;
                         if(k==88 || k==92){
                                            printf("X won\n");
                                            flag=true;
                                            break;
                                            }
                         else if(k==61 || k==56){
                                                 printf("O won\n");
                                                 flag=true;
                                                 break;
                                                 }
                         }
               
               if(!flag){
                         FR(i,0,4){
                                   k=0;
                                   FR(j,0,4)k+=s[j][i]-65;
                                   if(k==88 || k==92){
                                                      printf("X won\n");
                                                      flag=true;
                                                      break;
                                                      }
                                   else if(k==61 || k==56){
                                                    printf("O won\n");
                                                    flag=true;
                                                    break;
                                                    }
                                   }
                         }
               if(!flag){
                         k=0;
                         FR(i,0,4)k+=s[i][i]-65;
                                   if(k==88 || k==92){
                                                      printf("X won\n");
                                                      flag=true;
                                                      }
                                   else if(k==61 || k==56){
                                                           printf("O won\n");
                                                           flag=true;
                                                           }
                         }
               if(!flag){
                         k=0;
                         k=s[0][3]+s[1][2]+s[2][1]+s[3][0]-4*65;
                                   if(k==88 || k==92){
                                                      printf("X won\n");
                                                      flag=true;
                                                      }
                                   else if(k==61 || k==56){
                                                           printf("O won\n");
                                                           flag=true;
                                                           }
                         }
                         
               if(!flag){
                         bool fflag=false;
                         FR(i,0,4){
                                   FR(j,0,4){
                                             if(s[i][j]=='.'){
                                                             printf("Game has not completed\n");
                                                             fflag=true;
                                                             break;
                                                             }
                                             }
                         if(fflag)break;
                                  }
                         if(!fflag)printf("Draw\n");
                         }
               }
        //system("pause");
     R 0;
}    

