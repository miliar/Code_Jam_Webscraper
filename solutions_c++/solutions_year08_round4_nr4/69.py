#include<iostream>
#include<string.h>

using namespace std;

int flag[100];
int p[100];

int n,k;

char str[100000];
char ss[100000];

int res;

int check()
{
  int i,j,q;

  for (i=0; i<n; i++) {
    j=i%k;
    q=i/k*k;
    ss[i] = str[q+p[j]];
  }

  int r = 0;
  for (i=0; i<n; i++) {
    if (i==0 || ss[i]!=ss[i-1]) r++;
  }

  if (r<res) res=r;

  return 0;
    
}

int dfs(int x)
{
  if (x==k) {
    check();
    return 0;
  }

  int i;
  
  for (i=0; i<k; i++) if (!flag[i]) {
    flag[i]=1;
    p[x] = i;
    dfs(x+1);
    flag[i]=0;
  }
  return 0;
}

int solve()
{
  cin >> k;
  cin >> str;
  n = strlen(str);

  memset(flag, 0, sizeof(flag));
  res=100000000;
  dfs(0);
  
  cout << res << endl;


  return 0;
}

main()
{
  int t, c=0;
  cin >> t;
  while (t--) {
    cout << "Case #" << ++c << ": ";
    solve();
  }
  return 0;
}
