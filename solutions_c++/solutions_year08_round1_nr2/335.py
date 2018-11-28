#include<iostream>
#include<vector>
#include<set>
using namespace std;

int flavn,custn;
typedef set<pair<int,bool> > sett;
vector<sett> pref;

bool calc(int& rv)
{
  int i;
  for(rv=0;rv<(1<<flavn);++rv)
  { for(i=0;i<custn;++i)
    { sett::iterator it;
      for(it=pref[i].begin();it!=pref[i].end();++it)
      { if(bool(rv&(1<<it->first))==it->second) break;
      }
      if(it==pref[i].end()) break;
    }
    if(i==custn) return true;
  }
  return false;
}
int main()
{
  int ci,cn,t,i,j,x,y;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { cin>>flavn>>custn;
    pref.assign(custn,sett());
    for(i=0;i<custn;++i)
    { cin>>t;
      for(j=0;j<t;++j)
      { cin>>x>>y; --x;
        pref[i].insert(make_pair(x,y));
      }
    }
    int res;
    if(calc(res))
    { cout<<"Case #"<<ci<<':';
      for(i=0;i<flavn;++i) cout<<' '<<((res&(1<<i))?1:0);
      cout<<endl;
    }else cout<<"Case #"<<ci<<": IMPOSSIBLE"<<endl;
  }
}
