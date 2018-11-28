#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define ll long long
#define INF 1<<30
#define PI 3.1415926535897932
#define EPS 1e-9
#define sqr(x) ((x)*(x))
char a[54][54];
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  int t,n,m;
  cin>>t;
  for(int r=0;r<t;r++)
  {
    cin>>n>>m;
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++)cin>>a[i][j];
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++)
        if (a[i][j]==a[i][j+1] && a[i][j]==a[i+1][j] && a[i][j]==a[i+1][j+1] && a[i][j]=='#')
        {
          a[i][j]='/';
          a[i][j+1]='\\';
          a[i+1][j]='\\';
          a[i+1][j+1]='/';
        }
    bool yes=true;
    for(int i=0;i<n;i++)
      for(int j=0;j<m;j++)
        if (a[i][j]=='#')yes=false;
    cout<<"Case #"<<r+1<<":\n";
    if (!yes)cout<<"Impossible\n";
    else 
      for(int i=0;i<n;i++,cout<<endl)
        for(int j=0;j<m;j++)cout<<a[i][j];
  }
  return 0;
}