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

const int MAX_N=500+20,INF=1<<25;

int dist[MAX_N][MAX_N];
bool e[MAX_N][MAX_N];
int n,ans;

vector<int> all;

template<class t>
ostream & operator << (ostream & tout,const vector<t> &s){
  tout<<'[';
  for (int i=0;i<s.size();i++)
    if (i+1 == s.size())
      tout<<s[i];
    else
      tout<<s[i]<<',';
  tout<<']';
  return(tout);
}


void bt(int s){
  if (dist[s][1] > dist[2][1])
    return;
//   cout<<s<<' '<<all<<endl;
  if (s == 2){
    int count=0;
    for (int i=1;i<=n;i++){
      bool bad=false;
      for (int j=0;j<all.size();j++)
	if (e[i][all[j]])
	  bad=true;
      if (bad)
	count++;
    }
    ans=max(ans,count);
    return;
  }
  all.push_back(s);
  for (int i=1;i<=n;i++)
    if (dist[s][i] == 1)
      bt(i);
  all.pop_back();
}

int main(){
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    int m;
    cin>>n>>m;
    for (int i=1;i<=n;i++)
      for (int j=1;j<=n;j++)
	if (i==j)
	  dist[i][j] = 0;
	else
	  dist[i][j]=INF;
	       
    for (int i=1;i<=m;i++){
      int a,b;
      char c;
      cin>>a>>c>>b;
      a++;
      b++;
      dist[a][b]=dist[b][a]=1;
    }
    for (int i=1;i<=n;i++)
      for (int j=1;j<=n;j++)
	if (dist[i][j] == 1)
	  e[i][j]=true;
	else
	  e[i][j]=false;
    for (int i=1;i<=n;i++)
      for (int j=1;j<=n;j++)
	for (int k=1;k<=n;k++)
	  dist[j][k]=min(dist[j][k],dist[j][i]+dist[i][k]);
    for (int i=1;i<=n;i++)
      for (int j=1;j<=n;j++)
	if (dist[1][i]+dist[i][j]+dist[j][2] != dist[1][2])
	  dist[i][j]=INF;
//     for (int i=1;i<=n;i++,cout<<endl)
//       for (int j=1;j<=n;j++)
// 	cout<<dist[i][j]<<' ';
//     cout<<endl;
				    
    ans=-1;
    bt(1);
    int q=0;
    if (dist[1][2] == 1)
      q=dist[1][2]-1;
    else
      q=dist[1][2];
    cout<<"Case #"<<ccount<<": "<<dist[1][2]-1<<' '<<ans-q<<endl;
  }
}
