#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

typedef long long T;
T N,M;

vector<int> doit(int a, int b)
{
   vector<int> ret;ret.clear();
   if(a<=N&&b<=M) {
      ret.push_back(0);ret.push_back(0);
      ret.push_back(b);ret.push_back(0);
      ret.push_back(0);ret.push_back(a);
   }
   return ret;
}
int main()
{
   freopen("B-small-attempt1.in","r",stdin);
   freopen("test.out","w",stdout);
   int C;
   cin>>C;
   for(int tc=1;tc<=C;tc++) {
      T A;
      cin>>N>>M>>A;

      vector<T> ret;ret.clear();
      int x=0,y=0;
      for(T xb=0;xb<=N;xb++) for(T yb=0;yb<=M;yb++) for(T xc=0;xc<=N;xc++) for(T yc=0;yc<=M;yc++) {
         T res=abs(xb*yc-xc*yb);
         if(res==A) {
            ret.push_back(0);ret.push_back(0);
            ret.push_back(xb);ret.push_back(yb);
            ret.push_back(xc);ret.push_back(yc);
            xb=N+1;yb=M+1;xc=N+1;yc=M+1;
            break;
         }
      }
     cout<<"Case #"<<tc<<": ";


      if(ret.size()==0) {
         cout<<"IMPOSSIBLE"<<endl;
      }
      else {
         for(int i=0;i<ret.size();i++) {
            if(i==0)cout<<ret[i];
            else cout<<" "<<ret[i];
         }
         cout<<endl;
      }
   }
   return 0;
}
