#include <iostream>
#include <set>
#include <map>
using namespace std;

int c;

int a[500][500],u[500][500];
int n,m;

int dfs(int i, int j)
{
 //u[i][j]=c;
// cout << i << j << endl;
 if(a[i-1][j]<=a[i][j-1]&&a[i-1][j]<=a[i+1][j]&&a[i-1][j]<=a[i][j+1]&&a[i-1][j]<a[i][j])u[i][j]=dfs(i-1,j);else
 if(a[i][j-1]<=a[i-1][j]&&a[i][j-1]<=a[i+1][j]&&a[i][j-1]<=a[i][j+1]&&a[i][j-1]<a[i][j])u[i][j]=dfs(i,j-1);else
 if(a[i][j+1]<=a[i-1][j]&&a[i][j+1]<=a[i+1][j]&&a[i][j+1]<=a[i][j-1]&&a[i][j+1]<a[i][j])u[i][j]=dfs(i,j+1);else
 if(a[i+1][j]<=a[i][j-1]&&a[i+1][j]<=a[i-1][j]&&a[i+1][j]<=a[i][j+1]&&a[i+1][j]<a[i][j])u[i][j]=dfs(i+1,j);else
 {if(u[i][j]==0)u[i][j]=++c; return u[i][j];}
// cout << u[i][j] << endl;
}


int main()
{
 int z;
 cin >> z;
 freopen("out","w",stdout);
 for(int _=0; _<z; _++)
 {
  cout << "Case #" << _+1 << ":";
  cin >> n >> m;
  set<pair <int,pair<int,int> > > s;
  for(int i=0; i<=n+1; i++)for(int j=0; j<=m+1; j++){a[i][j]=420000;u[i][j]=0;}
  for(int i=1; i<=n; i++)for(int j=1; j<=m; j++)
  {
   cin >> a[i][j];
   s.insert(make_pair(-a[i][j],make_pair(i,j)));
  }
  c=0;
  while(!s.empty())
  {

   if(!u[s.begin()->second.first][s.begin()->second.second])
   {
 //   c++;
    dfs(s.begin()->second.first,s.begin()->second.second);
    s.erase(s.begin());
    //cout << c << endl;
   }else s.erase(s.begin());

  }
  cout << endl;
  map<int,char> mm;
  char aa='a';
  for(int i=1; i<=n; i++)
  {
   for(int j=1; j<=m; j++)
   {
    if(mm[u[i][j]]==0)mm[u[i][j]]=aa++;
    cout << mm[u[i][j]] << " ";
   }
   cout << endl;
  }
 }
}
