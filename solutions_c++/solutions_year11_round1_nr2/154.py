#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<deque>
#include<set>
using namespace std;
#define ll long long
#define VI vector<int>
#define VS vector<string>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back

int main() {
 int T;cin>>T;
     for (int t=0;t<T;t++) {
              cout<<"Case #"<<(t+1)<<":";
              int N,M;
              cin>>N>>M;
              VS d=VS(N,"");
              for (int i=0;i<N;i++) cin>>d[i];
              string m;
              for (int j=0;j<M;j++) {
                  cin>>m;
                  int res=-1;
                  string ret="";
                  for (int k=0;k<N;k++) {
                      int score=0;
                      int mind=0;
                      do {                  
                      bool ok=false;
                      for (int i=0;i<N;i++) if (d[i].size()==d[k].size()){
                          bool okej=true;
                          for (int u=0;u<mind;u++) {
                              for (int v=0;v<d[i].size();v++) 
                                if ((d[k][v]==m[u]&&d[i][v]!=m[u])||(d[k][v]!=m[u]&&d[i][v]==m[u])) okej=false;
                          }
                          bool cont=false;
                          for (int v=0;v<d[i].size();v++) if (d[i][v]==m[mind]) cont=true;
                          if (!cont) okej=false;
                          if (okej) ok=true;
                      }
                      if (!ok) { mind++; continue;}
                      bool cont=false;
                      for (int i=0;i<d[k].size();i++) if (d[k][i]==m[mind]) cont=true;
                      if (!cont) score++;
                      mind++;
                      } while (mind<m.size());    
                      if (score>res) {res=score; ret=d[k];}
                  }
                  cout<<" "<<ret;
              } cout<<endl;
     }
}
