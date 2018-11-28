#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

typedef long long ll;

int main()
{
  int cases; cin>>cases;
  for (int c=1; c<=cases; c++){
    int h, w, f; cin>>h>>w>>f;
    vector<string> bd(h);
    for (int i=0;i<h;i++)
      cin>>bd[i];

    vector<ll> nbd(h, 0);
    for (int i=0;i<h;i++){
      for (int j=0;j<w;j++){
	if (bd[i][j]=='#')
	  nbd[i]|=1ll<<j;
      }
    }

    typedef pair<pair<int, int>, pair<ll, ll> > node;
#define mknode(aa, bb, cc, dd) make_pair(make_pair(aa, bb), make_pair(cc, dd))

    multimap<int, node> mm;
    mm.insert(make_pair(0, mknode(0, 0, nbd[0], nbd[1])));

    set<node> close;
    int ans=-1;

    while(!mm.empty()){
      node cur=mm.begin()->second;

      int dist=mm.begin()->first;
      int x=mm.begin()->second.first.first;
      int y=mm.begin()->second.first.second;
      int curl=mm.begin()->second.second.first;
      int nexl=mm.begin()->second.second.second;

      //cout<<x<<", "<<y<<endl;

      mm.erase(mm.begin());

      if (y==h-1){
	ans=dist;
	break;
      }

      close.insert(cur);

      int bkup_curl=nbd[y];
      int bkup_nexl=nbd[y+1];

      nbd[y]=curl;
      nbd[y+1]=nexl;

      if (x>=1 && !(nbd[y]&(1<<(x-1)))){
	int fall=0;
	while(y+fall+1<h && !(nbd[y+fall+1]&(1<<(x-1)))) fall++;
	if (fall<=f){
	  node nn=mknode(x-1, y+fall, nbd[y+fall], nbd[y+fall+1]);
	  if (close.count(nn)==0)
	    mm.insert(make_pair(dist, nn));
	}
      }
      if (x+1<w && !(nbd[y]&(1<<(x+1)))){
	int fall=0;
	while(y+fall+1<h && !(nbd[y+fall+1]&(1<<(x+1)))) fall++;
	if (fall<=f){
	  node nn=mknode(x+1, y+fall, nbd[y+fall], nbd[y+fall+1]);
	  if (close.count(nn)==0)
	    mm.insert(make_pair(dist, nn));
	}
      }
      if (x-1>=0 && !(nbd[y]&(1<<(x-1))) && (nbd[y+1]&(1<<(x-1)))){
	node nn=mknode(x, y, curl, nexl&~(1<<(x-1)));
	if (close.count(nn)==0)
	  mm.insert(make_pair(dist+1, nn));
      }
      if (x+1<w && !(nbd[y]&(1<<(x+1))) && (nbd[y+1]&(1<<(x+1)))){
	node nn=mknode(x, y, curl, nexl&~(1<<(x+1)));
	if (close.count(nn)==0)
	  mm.insert(make_pair(dist+1, nn));
      }

      nbd[y]=bkup_curl;
      nbd[y+1]=bkup_nexl;
    }

    if (ans>=0)
      cout<<"Case #"<<c<<": Yes "<<ans<<endl;
    else
      cout<<"Case #"<<c<<": No"<<endl;
  }
  return 0;
}
