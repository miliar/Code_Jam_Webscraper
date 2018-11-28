#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<sstream>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<cassert>
using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int,int> pi;

#define INF 1000000000
#define y0 yy
#define y1 yyy

double x , y,  x1 , yyy;
double x0;
double yy;


double area()
{
  double r1 , r0;
 
  r0 = sqrt( (x0-x)*(x0-x) + (y0-y)*(y0-y) );
  r1 = sqrt( (x-x1)*(x-x1) + (y-y1)*(y-y1) );
  
  
  double c = sqrt( (x0-x1)*(x0-x1) + (y0-y1)*(y0-y1) );
  
  //cout<<r0<<'\t'<<r1<<'\t'<<c<<endl;
  double a1 = ( r1*r1 + c*c - r0*r0 ) / (2*r1*c);
  a1 = acos(a1);
  a1*=2;
  double a2 = ( - r1*r1 + c*c + r0*r0 ) / (2*r0*c);
  a2 = acos(a2);
  a2*=2;
  
  double ret = 0;
  ret = r1*r1*a1 + r0*r0*a2;
  ret -= r1*r1*sin(a1);
  ret -= r0*r0*sin(a2);
  
  ret/=2;
  return ret;
}

int main()
{
  int t;
  scanf("%d",&t);
  for(int cas = 1 ; cas <= t ; cas++)
  {
    int n , m;
    cin>>n>>m;

    cin>>x0;
    cin>>yy;
    cin>>x1;
    cin>>yyy;
    printf("Case #%d: ",cas);
    for(int i = 1 ; i <= m - 1 ; i++)
    {
      cin>>x>>y;
      printf("%.6lf ",area());
    }
    cin>>x>>y;
    printf("%.6lf",area());
    cout<<endl;    
  }
  return 0;  
}