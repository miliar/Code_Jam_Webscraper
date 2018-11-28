#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <complex>
#include <cmath>
#include <cstdlib>
using namespace std;

typedef long long ll;
typedef complex<double> pt;

typedef vector<pair<int,int> > stat;

int find(int *p, int i)
{
  if (p[i]==i) return i;
  return p[i]=find(p, p[i]);
}

void conn(int *p, int i, int j)
{
  p[find(p, i)]=find(p, j);
}

bool isconn(const stat &st)
{
  int n=st.size();
  int p[5]={0,1,2,3,4};
  for (int i=0;i<n;i++)
    for (int j=i+1;j<n;j++)
      if ((st[i].first==st[j].first && abs(st[i].second-st[j].second)==1) ||
          (st[i].second==st[j].second && abs(st[i].first-st[j].first)==1))
        conn(p, i, j);
  int q=find(p, 0);
  for (int i=1;i<n;i++)
    if (find(p, i)!=q)
      return false;
  return true;
}

int main()
{
  int cases; cin>>cases;
  for (int c=1; c<=cases; c++){
    int h, w; cin>>h>>w;
    vector<string> bd(h);
    for (int i=0;i<h;i++) cin>>bd[i];

    stat st, ed;
    for (int y=0;y<h;y++){
      for (int x=0;x<w;x++){
        if (bd[y][x]=='o'||bd[y][x]=='w'){
          st.push_back(make_pair(x, y));
        }
        if (bd[y][x]=='x'||bd[y][x]=='w'){
          ed.push_back(make_pair(x, y));
        }
        if (bd[y][x]!='#')
          bd[y][x]='.';
      }
    }
    sort(st.begin(), st.end());
    sort(ed.begin(), ed.end());

    queue<pair<int, stat> > q;
    set<stat> close;

    q.push(make_pair(0, st));
    close.insert(st);

    int ans=-1;
    int n=st.size();

    int cnt=0;
    while(!q.empty()){
      cnt++;
      int dep=q.front().first;
      stat cur=q.front().second;
      q.pop();

      /*
      for (int i=0;i<n;i++)
        cout<<"("<<cur[i].first<<", "<<cur[i].second<<") ";
      cout<<endl;
       */
      
      if (cur==ed){
        ans=dep;
        break;
      }

      bool dang=!isconn(cur);

      for (int i=0;i<n;i++)
        bd[cur[i].second][cur[i].first]='o';

      for (int i=0;i<n;i++){
        int x=cur[i].first;
        int y=cur[i].second;
        static const int vect[8]={0,1,1,0,0,-1,-1,0};
        for (int d=0;d<8;d+=2){
          int dx=vect[d];
          int dy=vect[d+1];

          int nx=x+dx, ny=y+dy;
          int bx=x-dx, by=y-dy;

          if (nx<0||nx>=w||ny<0||ny>=h) continue;
          if (bx<0||bx>=w||by<0||by>=h) continue;

          if (bd[by][bx]=='.'&&bd[ny][nx]=='.'){
            stat nst=cur;
            nst[i]=make_pair(nx, ny);
            if (dang && !isconn(nst)) continue;
            sort(nst.begin(), nst.end());
            if (close.count(nst)>0) continue;
            close.insert(nst);
            q.push(make_pair(dep+1, nst));
          }
        }
      }

      for (int i=0;i<n;i++)
        bd[cur[i].second][cur[i].first]='.';
    }
    //cout<<cnt<<endl;

    cout<<"Case #"<<c<<": "<<ans<<endl;
  }
  return 0;
}
