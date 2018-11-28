#include <iostream>
#include <string>
#include <vector>
#define REP(i,n) for (i=0;i<n;++i)
using namespace std;

int l,d,n,i,j,k,p,c;
vector<string> v;
string s,s0;
int dd[5000];
bool o;

main(){
  freopen("alien.in","r",stdin);
  freopen("alien.out","w",stdout);
  cin>>l>>d>>n;
  REP(i,d) { cin>>s; v.push_back(s); }
  REP(i,n) {
    memset(dd,1,sizeof(dd));
    cin>>s;
    p=0;
    o=false;
    s0="";
    REP(j,s.length()){
      switch (s[j]){
        case '(': o=true;  break;
        case ')': o=false; break;
        default: 
          if (o) s0.append(1,s[j]);
          else s0=s[j];
          break;
      }
      if (s[j]==')'||s[j]!='('&&!o){
        /*
        cout << s0 << " " << p << endl;
        */
        REP(k,v.size()) if (s0.find_first_of(v[k][p])!=string::npos) dd[k]&=1; else dd[k]&=0;
        /*
        REP(k,d) cout<<dd[k]<< " ";
        cout << endl;
        */
        s0="";
        ++p;
      }
    }
    c=0;
    REP(j,d) c+=dd[j];
    cout<<"Case #"<<i+1<<": "<<c<<endl;
  }
}
