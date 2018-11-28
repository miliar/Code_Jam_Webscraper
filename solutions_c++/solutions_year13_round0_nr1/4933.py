#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#define PB push_back
#define MP make_pair
#define BG begin()
#define ED end()
#define SZ(x) ((int)((x).size()))
#define FF first
#define SS second
#define foreach(i,x) for (__typeof((x).begin()) i=(x).begin();i!=(x).end();i++)
#define FOR(i,l,r) for (int i=(l);i<=(r);i++)
#define ROF(i,r,l) for (int i=(r);i>=(l);i--)
using namespace std;

char a[6][6];

int cmp(char a,char b) {return (a==b || a=='T');}

void check() {
  int p3=0;
  FOR(i,0,3) {
    int p1=0,p2=0;
    FOR(j,0,3)
      if (a[i][j]=='X') p1++;
      else if (a[i][j]=='O') p2++;
      else if (a[i][j]=='T') p1++,p2++;
      else if (a[i][j]=='.') p3++;
    if (p1==4) {
      cout<<"X won"<<endl;
      return;
    }
    if (p2==4) {
      cout<<"O won"<<endl;
      return;
    }
    p1=0,p2=0;
    FOR(j,0,3)
      if (a[j][i]=='X') p1++;
      else if (a[j][i]=='O') p2++;
      else if (a[j][i]=='T') p1++,p2++;
    if (p1==4) {
      cout<<"X won"<<endl;
      return;
    }
    if (p2==4) {
      cout<<"O won"<<endl;
      return;
    }
  }
  if (cmp(a[0][0],'X')+cmp(a[1][1],'X')+cmp(a[2][2],'X')+cmp(a[3][3],'X')==4) {
    cout<<"X won"<<endl;
    return;
  }
  if (cmp(a[1][1],'O')+cmp(a[2][2],'O')+cmp(a[3][3],'O')+cmp(a[0][0],'O')==4) {
    cout<<"O won"<<endl;
    return;
  }if (cmp(a[0][3],'X')+cmp(a[1][2],'X')+cmp(a[2][1],'X')+cmp(a[3][0],'X')==4) {
    cout<<"X won"<<endl;
    return;
  }
  if (cmp(a[0][3],'O')+cmp(a[1][2],'O')+cmp(a[2][1],'O')+cmp(a[3][0],'O')==4) {
    cout<<"O won"<<endl;
    return;
  }
  if (p3!=0) {
    cout<<"Game has not completed"<<endl;
    return;
  }
  cout<<"Draw"<<endl;
}


int main()
{
 // freopen("c.in","r",stdin);
 // freopen("c.out","w",stdout);
  int T;
  scanf("%d ",&T);
  FOR(tt,1,T) {
    printf("Case #%d: ",tt);
    FOR(i,0,3) FOR(j,0,3) 
      scanf("%c ",&a[i][j]);
    check();
  }
}
