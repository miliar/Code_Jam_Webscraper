#include<iostream>
#include<complex>
#include<vector>
#include<string>
#include<map>
using namespace std;
#define SZ(X) ((int)X.size())
#define REP(I,N) for(int I=0;I<(N);I++)


template<class T> inline string stringify(T x,int p=9){ostringstream o;o.precision(p);o<<x;o.flush();return o.str();}

string i1="our language is impossible to understand";
string i2="there are twenty six factorial possibilities";
string i3="so it is okay if you want to just give up";
string i4="aozq";
string o1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
string o2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string o3="de kr kd eoya kw aej tysr re ujdr lkgc jv";
string o4="yeqz";

map<char,char> m;
//map<char,char> m_r;

int main(){
  m.clear();
  REP(i,SZ(i1)) m[o1[i]]=i1[i];
  REP(i,SZ(i2)) m[o2[i]]=i2[i];
  REP(i,SZ(i3)) m[o3[i]]=i3[i];
  REP(i,SZ(i4)) m[o4[i]]=i4[i];
//  FOREACH(I, m) m_r[I->SE]=I->FI;
//  FOREACH(I, m) cout<<I->FI<<" "<<I->SE<<endl;
  int T;
  cin>>T;
  int t=1;
  string kurwa;
  getline(cin,kurwa);
  while(t<=T){
    string g;
    getline(cin,g);
    string out="";
    REP(i,SZ(g)) out+=m[g[i]];
    cout<<"Case #"<<stringify(t)<<": "<<out<<endl;
    t++;
  }
  return 0;
}
