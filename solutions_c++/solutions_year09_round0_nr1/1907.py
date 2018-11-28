#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <iostream>
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
   long i,n,l,d;
   string w;
   cin>>l>>d>>n;
   vector<string> slovnik;
   vector<string> slova;
   FR(i,d){
      cin>>w;
      slovnik.push_back(w);
   }

   long count,j,pw,ps,lw,match;
   FR(i,n){
      cin>>w;
      count=0;
      lw=SoF(w);
      FR(j,d){
         match=1;
         pw=0;
         ps=0;
         while((pw<lw)&&(match)){
//            cout<<w[pw]<<"   "<<slovnik[j][ps]<<"   ";
            if(w[pw]=='('){
               while((w[pw]!=')')&&(w[pw]!=slovnik[j][ps])){pw++;}
               if(w[pw]==')')match=0;
               else while(w[pw]!=')')pw++;
            }
            else{
               if(w[pw]!=slovnik[j][ps])match=0;
            }
//            cout<<endl;
            ps++;
            pw++;
         }
         if(match)count++;
      }
      cout<<"Case #"<<i+1<<": "<<count<<endl;
   }
   return 0;
}
