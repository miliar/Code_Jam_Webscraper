#include <vector>
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
using namespace std; int main(){
      freopen("in1.txt","r",stdin);
	  freopen("out4.txt","w",stdout);
      int loop;
      cin>>loop;
      f(tt,loop){
                 int n;
                 int a1=0;
                 cin>>n;
                 int a[n];
                 int temp;
                 int max1=0;
                 f(i,n) {cin>>temp;a[i]=temp;}
                 a1=1<<n;a1--;
                 //cout<<"for n: "<<n<<" value of a1 is: "<<a1<<endl;
                 fo(i,1,a1){
                        bool first=true;bool sec=true;
                        int right,left,sum1=0,sum2=0;
                        f(j,n){
                               if(i&(1<<j)){
                                            if(first){right=a[j];sum2+=a[j]; first=false;}
                                            else{
                                                 right^=a[j];
                                                 sum2+=a[j];
                                                 }
                                                 }
                               else{
                                    if(sec){
                                            left=a[j];
                                            sum1+=a[j];
                                            sec=false;
                                            }
                                    else{
                                         left^=a[j];
                                         sum1+=a[j];
                                         }
                                         }
                                         }
                         int max2=0;                
                         if(left==right){max2=max(sum1,sum2); max1=max(max2,max1);}
                         }
                         //cout<<"for n: "<<n<<endl;
                         if(max1==0) cout<<"Case #"<<tt+1<<": "<<"NO"<<endl;
                         else cout<<"Case #"<<tt+1<<": "<<max1<<endl;
                         }}                                                           
                                                             
                                                 
