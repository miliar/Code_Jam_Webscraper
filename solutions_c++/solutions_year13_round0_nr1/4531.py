#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<queue>
#include<stack>
#include<deque>
#include<map>
#include<set>
#define Pi 3.14159265358
#define fi first
#define se second
#define pb push_back
#define mp make_pair
using namespace std;
long long n, m, k, p, i, j, x, y, cur, a[10][10];
string s;
int go(int p, int m, int k)
{
    int i;
    int j;
    int x;
    int cur;
    bool bol;
    bol=true;
    for(i=1;i<=4;i++){
    for(j=1;j<=4;j++){ 
                      if(a[i][j]!=5 && a[i][j]!=0){ 
                      bol=true;
                      for(x=1;x<=4;x++){
                                        if(a[i][x]!=a[i][j] && a[i][x]!=5){
                                                                           bol=false;
                                                                           break;
                                                                           }
                                        }
                      if(bol){
                              return a[i][j];
                              }
                      bol=true;
                      for(x=1;x<=4;x++){
                                        if(a[x][j]!=a[i][j] && a[x][j]!=5){
                                                                           bol=false;
                                                                           break;
                                                                           }
                                        }
                      if(bol){
                              return a[i][j];
                              }
                                                   }
                      }
                      }
    bol=true;
    for(i=1;i<=4;i++){
                      if(a[i][i]!=5 && a[i][i]!=0){
                                                   cur=a[i][i];
                                                   break;
                                                   }
                      }
    for(i=1;i<=4;i++){
                      if(a[i][i]!=cur && a[i][i]!=5){
                                                     bol=false;
                                                     break;
                                                     }
                      }
    if(bol){
            return cur;
            }
    bol=true;
    for(i=4,j=1;i>=1,j<=4;i--,j++){
                                   if(a[i][j]!=5 && a[i][j]!=0){
                                                                cur=a[i][j];
                                                                break;
                                                                }
                                   }
    for(i=4,j=1;i>=1,j<=4;i--,j++){
                                   if(a[i][j]!=cur && a[i][j]!=5){
                                                                  bol=false;
                                                                  break;
                                                                  }
                                   }
    if(bol){
            
            return cur;
            }
    if(p+m+k==16){
                  return 10;
                  }
    else return 20;
}
main(){
       freopen("codejamA.in","r",stdin);
       freopen("codejamA.out","w",stdout);
       cin>>n;
       for(i=1;i<=n;i++){
                         m=0;
                         k=0;
                         p=0;
                         for(j=1;j<=4;j++){
                                           cin>>s;
                         for(x=0;x<4;x++){
                                          if(s[x]=='T'){
                                                        a[j][x+1]=5;
                                                        m++;
                                                        }else
                                          if(s[x]=='X'){
                                                        a[j][x+1]=1;
                                                        k++;
                                                        }else
                                          if(s[x]=='O'){
                                                        a[j][x+1]=2;
                                                        p++;
                                                        }
                                          else{
                                               a[j][x+1]=0;
                                               }
                                          }
                                           }
                         cur=go(p,m,k);
                         if(cur==1){
                                    cout<<"Case #"<<i<<": X won";
                                    cout<<endl;
                                    }else
                         if(cur==2){
                                     cout<<"Case #"<<i<<": O won";
                                     cout<<endl;
                                     }else
                         if(cur==10){
                                     cout<<"Case #"<<i<<": Draw";
                                     cout<<endl;
                                     }
                         if(cur==20){
                                     cout<<"Case #"<<i<<": Game has not completed";
                                     cout<<endl;
                                     }
                         }
       }
