#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
using namespace std;

void process()
{
  int n,m,a;
  cin>>n>>m>>a;

  vector<bool> flg(n*m+1,false);
  vector<pair<int,int> > mul(n*m+1);
  for (int i=0;i<=n;i++){
    for (int j=0;j<=m;j++){
      if (!flg[i*j]){
	//cout<<i*j<<endl;
	flg[i*j]=true;
	mul[i*j]=make_pair(i,j);
      }
    }
  }

  for (int x=0;x<=n*m;x++){
    if (!flg[x]) continue;
    int y=x-a;
    if (y>x) continue;
    if (y>n*m||y<0) continue;
    if (a!=abs(x-y)) continue;
    if (!flg[y]) continue;

    cout<<"0 0 ";
    cout<<mul[x].first<<" "<<mul[y].second<<" ";
    cout<<mul[y].first<<" "<<mul[x].second<<endl;

    return;
  }

  cout<<"IMPOSSIBLE"<<endl;
}

int main()
{
  string line;
  getline(cin,line);
  int cases=atoi(line.c_str());
  for (int c=1;c<=cases;c++){
    cout<<"Case #"<<c<<": ";
    process();
  }
}
