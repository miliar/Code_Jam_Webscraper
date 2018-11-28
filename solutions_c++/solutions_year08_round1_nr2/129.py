#include<iostream>

using namespace std;

int n, m;
int t[2000];
int e[2000][3000][2];

int res[2000];
int output[2000];

int solve0()
{
  int i,j,k,a,ans,N;
  cin >> n >> m;
  for (i=0; i<m; i++) {
    cin >> t[i];
    for (j=0; j<t[i]; j++) {
      cin >> e[i][j][0] >> e[i][j][1];
      e[i][j][0]--;
    }
    for (j=0; j<t[i]; j++)
      for (k=j+1; k<t[i]; k++)
	if (e[i][j][0]==e[i][k][0]) {
	  cerr << "err!" << endl;
	}
  }

  ans = n+1;
  N=1<<n;
  for (i=0; i<N; i++) {
    a=0;
    for (j=0; j<n; j++) res[j] = (((1<<j)&i)>0), a+=res[j];
    for (j=0; j<m; j++) {
      for (k=0; k<t[j]; k++) if (res[e[j][k][0]]==e[j][k][1]) break;
      if (k==t[j]) break;
    }
    if (j==m) {
      if (a<ans) {
	ans=a;
	memmove(output, res, sizeof(res));
      }
    }
  }

  if (ans==n+1) cout << " IMPOSSIBLE" << endl;
  else {
    for (i=0; i<n; i++) cout << " " << output[i];
    cout << endl;
  }

  return 0;
}

int solve()
{
  int i,j,k,a,ans;
  cin >> n >> m;
  for (i=0; i<m; i++) {
    cin >> t[i];
    for (j=0; j<t[i]; j++) {
      cin >> e[i][j][0] >> e[i][j][1];
      e[i][j][0]--;
    }
    for (j=0; j<t[i]; j++)
      for (k=j+1; k<t[i]; k++)
	if (e[i][j][0]==e[i][k][0]) {
	  cerr << "err!" << endl;
	}
  }

  for (i=0; i<n; i++) res[i]=0;

  while (1) {
    a=0;
    for (i=0; i<m; i++) {
      for (j=0; j<t[i]; j++)
	if (res[e[i][j][0]] == e[i][j][1]) break;
      if (j<t[i]) a++;
      else {
	for (j=0; j<t[i]; j++) if (e[i][j][1]==1) break;
	if (j==t[i]) {
	  cout << " IMPOSSIBLE" << endl;
	  return 0;
	}
	res[e[i][j][0]]=1;
      }
    }
    if (a==m) break;
  }

  for (i=0; i<n; i++) cout << " " << res[i];
  cout << endl;

  return 0;
}

int main()
{
  int c=0, t;
  cin >> t;
  while (t--) {
    cout << "Case #" << ++c << ":";
    solve();
  }
  return 0;
}
