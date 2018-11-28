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
           int r,c;
           cin>>r>>c;
           char ori[r][c];
           char temp;
           f(i,r){
                  f(j,c){
                         cin>>temp;
                         ori[i][j]=temp;
                         }}
           int a[r][c];
           f(i,r){
                  f(j,c){
                         if(ori[i][j]=='.') a[i][j]=-1;
                         else if(ori[i][j]=='#') a[i][j]=0;
                         }}
           int final[r][c];
           f(i,r){
                  f(j,c){
                         if(a[i][j]==-1) final[i][j]=0;
                         else if(a[i][j]==0){
                              if(j>0&&a[i][j-1]==0&&i>0&&a[i-1][j]==0&&a[i-1][j-1]==0){
                                                  if(final[i-1][j-1]!=2&&final[i-1][j]!=2&&final[i][j-1]!=2) final[i][j]=2;
                                                  else final[i][j]=1;   }                                  
                             //  final[i][j]=2;
                              else final[i][j]=1;
                              }
                              }}
           int ones=0,twos=0;
           f(i,r){
                  f(j,c){
                         if(final[i][j]==1) ones++;
                         else if(final[i][j]==2) twos++;
                         }}
           if(twos*3==ones) {
                            char sol[r][c];
                            f(i,r){
                                   f(j,c){
                                          if(final[i][j]==2){
                                                             sol[i][j]='/';
                                                             sol[i][j-1]='\\';
                                                             sol[i-1][j-1]='/';
                                                             sol[i-1][j]='\\';
                                                             }
                                          else if(final[i][j]==0) sol[i][j]='.';
                                          }}
                             cout<<"Case #"<<w+1<<':'<<endl;             
                             f(i,r){
                                    f(j,c){
                                           cout<<sol[i][j];
                                           }
                                           cout<<endl;
                                           }  }                              
             else{ cout<<"Case #"<<w+1<<':'<<endl;
             cout<<"Impossible"<<endl;}
             }int tt;cin>>tt;}                                                                                          
