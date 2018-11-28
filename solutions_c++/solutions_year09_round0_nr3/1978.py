#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>

using namespace std;

#define FF first
#define SS second
#define LL long long
#define PL pair<long,long>
#define SoF(x) (long)x.size()
#define FOR(x,y,n) for(x=y;x<n;x++)
#define FR(x,n) FOR(x,0,n)
//#define ROF(x,n,y) for(x=n-1;x>=y;x--)
//#define RF(x,n) ROF(x,n,0)


int main(){
   long i,n,tc;
   char c;
   cin>>n;
   cin.get();
   vector<long> count;
   string ws="Xwelcome to code jam";   
   
   FR(tc,n){
      count=vector<long>(22,0);
      count[0]=1;
      c=cin.get();
      while((!cin.eof())&&(c!='\n')){
//         cout<<c<<" ";
         FOR(i,1,20){
            if(ws[i]==c){
               count[i]=(count[i]+count[i-1])%1000;
            }
         }
         cin.get(c);
      }
      cout<<"Case #"<<tc+1<<": "<<setfill('0')<<setw(4)<<count[19]<<endl;
   }
   
   return 0;
}
