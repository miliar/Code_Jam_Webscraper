#include<iostream>
#include<complex>
#include<vector>
#include<string>
#include<map>

#include<cstdio>
#include<cctype>
#include<cstring>
#include<cstdlib>
#include<cmath>

using namespace std;
#define SZ(X) ((int)X.size())
#define REP(I,N) for(int I=0;I<(N);I++)
#define PB push_back
typedef vector<int> VI;
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define MIN(A,B) (((A)<(B))?(A):(B))
template<class T> inline string stringify(T x,int p=9){ostringstream o;o.precision(p);o<<x;o.flush();return o.str();}

inline VI parsei(string s,char ch=' '){string a="";VI wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(atoi(a.c_str()));a="";} if(!a.empty()) wyn.PB(atoi(a.c_str()));return wyn;}

int main(){
  int T;
  cin>>T;
  int t=1;
  string kurwa;
  getline(cin,kurwa);
  while(t<=T){
    string g;
    getline(cin,g);
    VI inp=parsei(g);
    int s=inp[1], p=inp[2];
    int k1=0, k2=0;
    int out=0;
    FOR(i,3,SZ(inp)-1){
      int r=inp[i]/3;
      int rev=r*3;
      int rem=inp[i]-rev;
      if(rem==0){
        if(r>=p) k1++; else if(r>0&&r+1>=p) k2++;
      } else if(rem==2){
        if(r+1>=p) k1++; else if(r+2>=p) k2++;
      } else {
        if(r+1>=p) k1++;
      }
    }
    out=k1+MIN(s,k2);
    cout<<"Case #"<<stringify(t)<<": "<<stringify(out)<<endl;
    t++;
  }
  return 0;
}
