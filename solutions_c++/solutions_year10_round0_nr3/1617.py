#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

typedef long long lli;

lli calc(int turns,int cap,vector<int>& group)
{
  lli rv=0;
  int tused,n=group.size();
  vector<lli> lastrv(n,-1);
  vector<int> lastt(n,-1);
  bool pdone=false;
  int cur=0,s;
  lli total=0;
  for(cur=0;cur<n;++cur) total+=group[cur];
  cur=0;
  // go till cycle
  for(tused=0;tused<turns;++tused)
  { if(!pdone&&lastrv[cur]>=0) 
    { lli perrv=lastrv[cur]-rv;
      int pert=lastt[cur]-tused;
      int left=(turns-tused)/pert;
      rv+=perrv*left; tused+=pert*left;
      pdone=true;
    }
    if(tused==turns) break;
    lastrv[cur]=rv; lastt[cur]=tused;
    if(group[cur]>cap) return rv; // they will never go through
    for(s=0;s+group[cur]<=cap&&s<total;s+=group[cur], cur=(cur+1)%n);
    rv+=s;
  }
  return rv;
}

int main()
{
  int ci,cn,i,n,r,k;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { cin>>r>>k>>n;
    vector<int> group(n);
    for(i=0;i<n;++i) cin>>group[i];
    cout<<"Case #"<<ci<<": "<<calc(r,k,group)<<endl;
  }
}
