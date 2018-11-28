#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#define REP(i,n) for(i=0;i<n;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
using namespace std;
int t,tt,pt;
int i,j,u,v,cmp;
string s;
char ch,chmin;
char cs[30];
int dc[10];
int main(){
  freopen("1bb.in","r",stdin);
  freopen("1bb.out","w",stdout);
  cin >> t;
  REP(tt,t){
    cin >> s;
    for (i=s.length()-2;i>=0;--i){
      chmin=100;
      cmp=-1;
      for (j=i+1;j<s.length();++j){
        if (s[i]<s[j] && s[j]<chmin){
          chmin=s[j];
          cmp=j;
        }
      }
      if (cmp!=-1){
        j=cmp;
        ch=s[i];s[i]=s[j];s[j]=ch;
        strcpy(cs,s.c_str());
        
        sort(cs+i+1,cs+s.length());
        /*
        FOR(u,j+1,s.length()-2){
          FOR(v,u+1,s.length()-1){
            if (s[u]>s[v]){
              ch=s[u];s[u]=s[v];s[v]=ch;
            }
          }
        }
        */
        s = string(cs);
        break;
      }
    }
    if (i<0){
      cout << "Case #" << tt+1 << ": ";
      memset(dc,0,sizeof(dc));
      REP(j,s.length()){
        ++dc[s[j]-48];
      }
      ++dc[0];
      pt=0;
      FOR(j,1,9){
        if (dc[j]){
          s[++pt]=char(j+48);
          cout << char(j+48);
          --dc[j];
          break;
        }
      }
      REP(j,10){
        while (dc[j]>0) { s[++pt]=char(j+48); cout << char(j+48); --dc[j]; }
      }
      cout << endl;
    }
    else{
      cout << "Case #" << tt+1 << ": " << s << endl;
    }
  }
}
