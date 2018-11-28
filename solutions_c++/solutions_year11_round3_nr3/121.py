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
           int n,l,h;
           cin>>n>>l>>h;
           int a[n];
           int temp;
           int sol=-1;
           f(i,n){
                  cin>>temp;
                  a[i]=temp;
                  }
           for(int i=l;i<=h;i++){
                   bool chk=true;
                   f(j,n){
                          bool ok=false;
                          if(a[j]%i==0||i%a[j]==0) ok=true;
                          chk=chk&ok;
                          }
                    if(chk){ sol=i; break;}
                    }
           if(sol==-1){
                       cout<<"Case #"<<w+1<<':'<<" NO"<<endl;
                       }
           else {
                cout<<"Case #"<<w+1<<": "<<sol<<endl;
                }
                }  
                int tt;
                cin>>tt;
                }                                
