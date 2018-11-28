#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#define rep(i,n) for(int i=0;i<n;i++)
#define fr(i,c) for(__typeof (c.begin()) i=c.begin(); i!=c.end(); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
using namespace std;

typedef vector<int> vi;
typedef long long ll;

int main(){
  int t; cin>>t;
  rep(it,t){
    cerr<<"case "<<it+1<<endl;
    char co[256][256]={};
    bool op[256][256]={};
    
    int c,d,n;
    cin>>c;
    rep(i,c){
      string s; cin>>s;
      co[s[0]][s[1]]=co[s[1]][s[0]]=s[2];
    }
    cin>>d;
    rep(i,d){
      string s; cin>>s;
      op[s[0]][s[1]]=op[s[1]][s[0]]=1;
    }
    cin>>n;
    string in; cin>>in;

    char stk[999]={}; int sz=0, cnt[256]={};
    rep(i,n){
      cnt[in[i]]++;
      stk[sz++]=in[i];
      while(sz>1&&co[stk[sz-1]][stk[sz-2]]){
        cnt[stk[sz-1]]--; cnt[stk[sz-2]]--;
        stk[sz-2]=co[stk[sz-1]][stk[sz-2]];
        cnt[stk[sz-2]]++;
        sz--;
      }

      rep(j,26)rep(k,26)if(cnt['A'+j]>0&&cnt['A'+k]>0&&op['A'+j]['A'+k]){
        rep(l,26)cnt['A'+l]=0;
        sz=0; goto NEXT;
      }
    NEXT:;
    }
    cout<<"Case #"<<it+1<<": [";
    rep(i,sz)cout<<(i?", ":"")<<stk[i];
    cout<<"]"<<endl;
  }
  return 0;
}
