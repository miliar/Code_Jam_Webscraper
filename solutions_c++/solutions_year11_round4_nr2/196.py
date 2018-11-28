#include <cstdio>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>


using namespace std;

const int MAX_N=500+20;

int l1[MAX_N][MAX_N];
int l2[MAX_N][MAX_N];

vector<vector<int> > qt;

int SM(int x1,int y1,int x2,int y2){
  return(qt[x2][y2]+qt[x1-1][y1-1]-
	 qt[x2][y1-1]-qt[x1-1][y2]);
}

const double EPS=1e-8;

int main(){
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    int n,m,d;
    cin>>n>>m>>d;
    vector<vector<int> > sum(n+1,vector<int>(m+1));
    vector<vector<int> > num(n+1,vector<int>(m+1));
    for (int i=1;i<=n;i++)
      for (int j=1;j<=m;j++){
	char c;
	cin>>c;
	num[i][j]=c-'0';
      }
    for (int i=1;i<=n;i++)
      for (int j=1;j<=m;j++)
	sum[i][j]=sum[i][j-1]+num[i][j];
    for (int i=1;i<=n;i++)
      for (int j=1;j<=m;j++)
	sum[i][j]+=sum[i-1][j];
    qt=sum;
    int ans=0;
    for (int i=2;i<n;i++)
      for (int j=2;j<m;j++){
	l1[i][j]=num[i][j-1]-num[i][j+1];
	l2[i][j]=num[i-1][j]-num[i+1][j];
	if (l1[i][j] == 0 && l2[i][j] == 0)
	  ans=max(ans,3);
      }
    for (int k=3;k<=n;k++)
      for (int i=1;i+k-1<=n;i++)
	for (int j=1;j+k-1<=m;j++){
	  double x=i+((double)k-1)/2;
	  double y=j+((double)k-1)/2;
	  double sx=0,sy=0;
	  for (int a=1;a<=k;a++)
	    for (int b=1;b<=k;b++){
	      if (a == 1 && b == 1)
		continue;
	      if (a == k && b == k)
		continue;
	      if (a == 1 && b == k)
		continue;
	      if (a == k && b == 1)
		continue;

	      sx+=num[i+a-1][j+b-1]*(x-(i+a-1));
	      sy+=num[i+a-1][j+b-1]*(y-(j+b-1));
	    }
// 	  cout<<i<<' '<<j<<' '<<k<<' '<<sx<<' '<<sy<<' '<<x<<' '<<y<<endl;
	  if (abs(sx) < EPS &&
	      abs(sy) < EPS)
	    ans=max(ans,k);
	}
    if (ans)
      cout<<"Case #"<<ccount<<": "<<ans<<endl;
    else
      cout<<"Case #"<<ccount<<": "<<"IMPOSSIBLE"<<endl;
  }
}
