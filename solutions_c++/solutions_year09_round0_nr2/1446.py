
//Written by Alex Hamed Ahmadi - alex@hamedahmadi.com

#include <iostream>
#include <cstring>
#include <string>
#include <cassert>
#include <algorithm>

using namespace std;

const int maxn=110;

int m,n;

int a[maxn][maxn];

int id[maxn][maxn];

int nbasin;

int giveid(int i, int j) {
  if (id[i][j]) return id[i][j];
  int lo=a[i][j];
  lo=min(lo, a[i-1][j]);
  lo=min(lo, a[i][j-1]);
  lo=min(lo, a[i][j+1]);
  lo=min(lo, a[i+1][j]);

  if (lo<a[i][j]) {
    if (a[i-1][j]==lo) return id[i][j]=giveid(i-1,j);
    if (a[i][j-1]==lo) return id[i][j]=giveid(i,j-1);
    if (a[i][j+1]==lo) return id[i][j]=giveid(i,j+1);
    if (a[i+1][j]==lo) return id[i][j]=giveid(i+1,j);
    assert(0);
  } else {
    //am sink
    return id[i][j]=++nbasin;
  }
}

int main() {

  int nt;
  cin>>nt;
  for (int T=1;T<=nt;T++) {
    nbasin = 0;

    cin>>m>>n;

    for (int i=0;i<=m+1;i++) for (int j=0;j<=n+1;j++) a[i][j]=99999;

    for (int i=1;i<=m;i++)
      for (int j=1;j<=n;j++)
	cin>>a[i][j];

    memset(id, 0, sizeof id);

    cout<<"Case #"<<T<<":"<<endl;
    for (int i=1;i<=m;i++,cout<<endl)
      for (int j=1;j<=n;j++)
	cout<<char('a'+giveid(i,j)-1)<<" ";
  }

  return 0;
}
