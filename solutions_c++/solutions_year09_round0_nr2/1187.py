#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

#define MAX 105
#define INF 1<<29
using namespace std;

int h, w;

int m[MAX][MAX];
int f[MAX][MAX];
char conv[27];

int di[]={-1, 0, 0, 1};
int dj[]={0, -1, 1, 0};
int cnt;

pair<int, int> goingTo(int ii, int jj) {
  int bsofar=m[ii][jj];
  int bi = ii;
  int bj = jj;
  for (int k=0;k<4;k++)
    if (m[ii+di[k]][jj+dj[k]] < bsofar) {
      bsofar = m[ii+di[k]][jj+dj[k]];
      bi = ii+di[k];
      bj = jj+dj[k];
    }
  return make_pair(bi, bj);
}

void flood(int ii, int jj, int color) {
  f[ii][jj]=color;
  for (int k=0;k<4;k++)
    if (f[ii+di[k]][jj+dj[k]]<0 && 
        goingTo(ii+di[k], jj+dj[k]).first == ii && 
	goingTo(ii+di[k], jj+dj[k]).second == jj)
      flood(ii+di[k], jj+dj[k], color);     
}

int main() {
  int t;
  cin >> t;
  memset(m, 0, sizeof(m));
  for (int tt=1;tt<=t;tt++) {
    cin >> h >> w;
    for (int i=1;i<=h;i++)
      for (int j=1;j<=w;j++)
	cin >> m[i][j];
    
    for (int i=0;i<=h+1;i++) {
      m[i][0]=m[i][w+1]=INF;
      f[i][0] = f[i][w+1] = 0;
    }
    for (int i=0;i<=w+1;i++) {
      m[0][i]=m[h+1][i]=INF;
      f[0][i] = f[h+1][i] = 0;
    }
    
    memset(f, 0xFF, sizeof(f));
    cnt=0;

    for (int i=1;i<=h;i++)
      for (int j=1;j<=w;j++) {
	bool sink=true;
	for (int k=0;k<4;k++)
	  if (m[i][j]>m[i+di[k]][j+dj[k]])
	    sink=false;
	if (sink)
	  flood(i, j, ++cnt);
      }
    
    memset(conv, 0, sizeof(conv));
    char next='a';
    for (int i=1;i<=h;i++)
      for (int j=1;j<=w;j++)
	if (!conv[f[i][j]])
	  conv[f[i][j]]=next++;

    cout << "Case #" << tt << ":\n";
    for (int i=1;i<=h;i++) 
      for (int j=1;j<=w;j++)
	cout << conv[f[i][j]] << (j!=w?' ':'\n');
      
  }
  return 0;
}
