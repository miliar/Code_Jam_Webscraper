#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define f(i,x) for(int i=0;i<x;i++)
#define fo(i,x,y) for(int i=x;i<y;i++)
#define pb push_back
#define vi vector<int>
#define all(x) x.begin(),x.end()
#define vs vector<string>
#define ss stringstream
#define ll long long
using namespace std; 
int main(){
       freopen("in1.txt","r",stdin);
      freopen("out4.txt","w",stdout);
    int t;
    cin>>t;
    f(w,t){
           int n;
           cin>>n;
           char a[n][n];
           char temp;
           f(i,n){
                  f(j,n){
                         cin>>temp;
                         a[i][j]=temp;
                         }}
           double wp[n];
           double owp[n];
           double oowp[n];
           double rpi[n];
           double zero=0,one=0;
           double zeros[n],ones[n];
           f(i,n){
                  double count=0;
                  zero=0,one=0;
                  f(j,n){
                         if(a[i][j]!='.'&&i!=j){count++;
                                          if(a[i][j]=='0'){
                                                           zero++;
                                                           }
                                          else one++;
                                         }
                                         }
                  zeros[i]=zero;
                  ones[i]=one;                       
                  wp[i]=one/(zero+one);
                  }
           //cout<<"zeros and ones value"<<endl;
          // f(i,n) cout<<zeros[i]<<' '<<ones[i]<<endl;
           //cout<<"wp of :"<<endl;
           //f(i,n) cout<<wp[i]<<' ';
           
                  
           f(i,n){
                    double count=0;
                    double sum=0;
                  f(j,n){
                       
                         if(a[i][j]!='.'&&i!=j){
                                              count++;
                                              if(a[i][j]=='0'){sum+=((ones[j]-1)/(ones[j]+zeros[j]-1));}
                                              else sum+=((ones[j])/(ones[j]+zeros[j]-1));
                                              }
                                              }
                  owp[i]=sum/count;                                              
                  }
            // cout<<"owp values"<<endl;     
            //f(i,n) cout<<owp[i]<<' ';      
           f(i,n){
                  double count=0;
                  double sum=0;
                  f(j,n){
                         if(a[i][j]!='.'&&i!=j){
                                                count++;
                                                sum+=owp[j];                                   
                                                }
                                                }
                  oowp[i]=sum/count;
                  }
          //cout<<"oowp values"<<endl;
         // f(i,n) cout<<oowp[i]<<' ';
                  
          f(i,n){
                 rpi[i]=(0.25*wp[i])+(0.5*owp[i])+(0.25*oowp[i]);
                 }
          cout<<"Case #"<<w+1<<':'<<endl;       
          f(i,n) cout<<rpi[i]<<endl;          
          }
          int tt;cin>>tt;
          }                                   
                                                               
                                                              
                                                                                                                      
                                                           
                                                     
                         
