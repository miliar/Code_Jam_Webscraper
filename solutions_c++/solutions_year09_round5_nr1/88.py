#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
typedef vector<int> vi;
typedef long long int64;

string s[20];
bool a[20][20];
int r,c,dx[4]={-1,0,1,0},dy[4]={0,-1,0,1};
vector<short int> start,end;
map<vector<short int>,int> seen;
vector< vector<short int> > q;
int p[100];
int find(int x){return p[x]==x?x:p[x]=find(p[x]);}
inline bool obok(int x1,int y1,int x2,int y2){
  return abs(x1-x2)+abs(y1-y2)==1;
}
inline bool connected(const vector<short int> &t){
  FOR(i,t.size())p[i]=i;
  FOR(i,t.size())FOR(j,i)if(obok(t[i]/c,t[i]%c,t[j]/c,t[j]%c))p[find(i)]=find(j);
  FOR(i,t.size())if(find(i)!=find(0))return false;
  return true;
}
int nr[1000],next_nr;
inline bool avail(int x,int y){
  //cout<<x*c+y<<endl;
  return x>=0&&y>=0&&x<r&&y<c&&a[x][y]&&nr[x*c+y]!=next_nr;
}
int main() {
  int n;cin>>n;
  for(int t=1;t<=n;t++){
    cin>>r>>c;
    FOR(i,r)cin>>s[i];
    FOR(i,r)FOR(j,c)a[i][j]=s[i][j]!='#';
    start.clear();
    end.clear();
    FOR(i,r)FOR(j,c)if(s[i][j]=='o'||s[i][j]=='w')start.push_back(i*c+j);
    FOR(i,r)FOR(j,c)if(s[i][j]=='x'||s[i][j]=='w')end.push_back(i*c+j);
    seen.clear();
    q.clear();
    seen[start]=0;
    q.push_back(start);
    int ans=-1;
    FOR(i,q.size()){
      vector<short int> cur=q[i],next;
      int dist=seen[cur];
      if(cur==end){ans=seen[cur];break;}
      bool prev_connected=connected(cur);
      next_nr++;
      FOR(i,cur.size())nr[cur[i]]=next_nr;
      FOR(i,cur.size()){
        int x=cur[i]/c,y=cur[i]%c;
        FOR(k,4)if(avail(x+dx[k],y+dy[k])&&avail(x+dx[(k+2)%4],y+dy[(k+2)%4])){
          next=cur;
          next[i]+=dx[k]*c+dy[k];
          sort(next.begin(),next.end());
          if((prev_connected||connected(next))&&!seen.count(next)){
            seen[next]=dist+1;
            q.push_back(next);
          }
        }
      }
    }
    cout<<"Case #"<<t<<": "<<ans<<endl;
  }
  return 0;
}
