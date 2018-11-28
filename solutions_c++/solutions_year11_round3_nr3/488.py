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
int a[105];
int main()
{
  //freopen("C-small-attempt0.in","r",stdin);
  //freopen("output.txt","w",stdout);
  int t,n,l,r;
  cin>>t;
  for(int e=0;e<t;e++)
  {
    cin>>n>>l>>r;
    cout<<"Case #"<<e+1<<": ";
    bool yes=false;
    for(int i=0;i<n;i++)cin>>a[i];
    for(int h=l;h<=r && !yes;h++)
    {
      yes=true;
      for(int i=0;i<n && yes;i++)
        if (!(a[i]%h==0 || h%a[i]==0))yes=false;
      if (yes)cout<<h<<endl;
    }
    if (!yes)cout<<"NO\n";
  }
  return 0;
}