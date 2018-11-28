#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>

using namespace std;

char map[6001][6001];
int ex[6001][6001];
int ey[6001][6001];
int nx[6001];
int ny[6001];

int solve()
{
  int r,x,y,p,i,m,l;
  char str[100];

  cin >> r;
  cerr << r << " ";
  memset(map, 0, sizeof(map));
  memset(nx, 0, sizeof(nx));
  memset(ny, 0, sizeof(ny));

  x=y=3000;
  p = 0;
  while (r--) {
    cin >> str >> l;
    m = strlen(str);
    while (l--) {
      for (i=0; i<m; i++) {
	if (str[i]=='L') p=(p+3)%4;
	if (str[i]=='R') p=(p+1)%4;
	if (str[i]=='F') {
	  if (p==0) ey[y][ny[y]++]=x, y++;
	  if (p==1) ex[x][nx[x]++]=y, x++;
	  if (p==2) y--, ey[y][ny[y]++]=x;
	  if (p==3) x--, ex[x][nx[x]++]=y;
	}
	if (x<0 || x>6000 || y<0 || y>6000) cerr << "@" << endl;
      }
    }
  }

  if (x!=3000 || y!=3000) cerr << "@" << endl;

  int ans = 0, ch=0;
  for (x=0; x<=6000; x++) if (nx[x]>3) {
    sort(ex[x], ex[x]+nx[x]);
    //ch+=nx[x];
    //if (nx[x]%2==1) cerr << "@" << endl;
    for (y=1; y<nx[x]-1; y+=2) {
      //ch+=ex[x][y]+ex[x][y+1];
      for (i=ex[x][y]; i<ex[x][y+1]; i++)
	map[x][i]=1, ans++;//, cout << x-3000 << " " << y-3000 << endl;
    }
  }
  for (y=0; y<=6000; y++) if (ny[y]>3) {
    //ch+=ny[y];
    //if (ny[y]%2==1) cerr << "@" << endl;
    sort(ey[y], ey[y]+ny[y]);
    for (x=1; x<ny[y]-1; x+=2) {
      //ch+=ey[y][x];
      for (i=ey[y][x]; i<ey[y][x+1]; i++)
	if (!map[i][y]) ans++;
    }
  }
  cerr << ans << " ";
/*
  ans=0;
  for (x=0; x<=6000; x++)
    for (y=0; y<=6000; y++)
      ans+=map[x][y];
*/
  cout << ans << endl;

  cerr << ch << endl;

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
