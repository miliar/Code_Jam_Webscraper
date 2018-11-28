#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long T;
const int MAXL=2000;
int P,K,L;

vector<T>  Letter;


T solve()
{
   sort(Letter.begin(),Letter.end(),greater<T>());
   
   if(((int)Letter.size())>K*P) {
      return -1;
   }
   T ret=0;
   T pressCount=1;
   while(Letter.size()>0) {
      vector<T> newLetter;
      newLetter.clear();
      for(int i=0;i<min(K,(int)Letter.size());i++) {
         ret+=Letter[i]*pressCount;
      }
      for(int i=min(K,(int)Letter.size());i<(int)Letter.size();i++) {
         newLetter.push_back(Letter[i]);
      }
      Letter=newLetter;
      pressCount++;
   }
   return ret;
   
}
int main()
{
   freopen("C:\\Downloads\\A-large(1).in","r",stdin);
   freopen("test.out","w",stdout);
   int N;
   cin>>N;
   for(int tc=1;tc<=N;tc++) {
      
      cin>>P>>K>>L;
      Letter.clear();
      for(int i=0;i<L;i++){
         T val=0;
          cin>>val;
          Letter.push_back(val);
         }
      
      cout<<"Case #" << tc<<": ";
      T ret=solve();
      cout<<ret<<endl;
   }
}
