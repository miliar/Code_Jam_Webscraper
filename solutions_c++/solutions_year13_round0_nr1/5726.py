#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <cstring>
#include <limits>

using namespace std;

#define FOR(I,A,B) for(int I= (A); I<(B); ++I)
#define REP(I,N) FOR(I,0,N)
#define LL long long
#define S(N) scanf("%d", &N)
#define SL(N) scanf("%lld", &N)
#define PB push_back
#define MP make_pair
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define cell pair<int,int>
#define edge pair<int, cell>
#define clear(x) memset(x,0,sizeof(x))
#define CHECK_BIT(var,pos) ((var) & (1<<(pos))

typedef vector<int> vi;
typedef vector<LL> vii;
cell dir[4]={cell(0,1), cell(1,0), cell(0,-1), cell(-1,0) };


int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t, ctr = 0; 
    S(t);
    while(t--)
    {
              char ch[4][4];
              int i;
              REP(i, 4) scanf("%s", &ch[i]);
              int ans = 0;
              REP(i, 4)
              if( (ch[i][0] == 'X'|| ch[i][0]=='T') && (ch[i][1]=='X'||ch[i][1]=='T') && (ch[i][2] == 'X'||ch[i][2]=='T') && (ch[i][3]=='X'||ch[i][3]=='T') )
              ans = 1;
              REP(i, 4)
              if( (ch[0][i] == 'X'|| ch[0][i]=='T') && (ch[1][i]=='X'||ch[1][i]=='T') && (ch[2][i] == 'X'||ch[3][i]=='T') && (ch[3][i]=='X'||ch[3][i]=='T') )
              ans = 1;
              REP(i, 4)
              if( (ch[0][i] == 'O'||ch[0][i]=='T') && (ch[1][i]=='O'||ch[1][i]=='T') && (ch[2][i] == 'O'||ch[2][i]=='T') && (ch[3][i]=='O'||ch[3][i]=='T') )
              ans = 2;
              REP(i, 4)
              if( (ch[i][0] == 'O'||ch[i][0]=='T') && (ch[i][1]=='O'||ch[i][2]=='T') && (ch[i][2] == 'O'||ch[i][2]=='T') && (ch[i][3]=='O'||ch[i][3]=='T') )
              ans = 2;
              if((ch[0][0] == 'X'|| ch[0][0]=='T') && (ch[1][1]=='X'||ch[1][1]=='T') && (ch[2][2] == 'X'||ch[2][2]=='T') && (ch[3][3]=='X'||ch[3][3]=='T'))
              ans = 1;
              if((ch[0][0] == 'O'|| ch[0][0]=='T') && (ch[1][1]=='O'||ch[1][1]=='T') && (ch[2][2] == 'O'||ch[2][2]=='T') && (ch[3][3]=='O'||ch[3][3]=='T'))
              ans = 2;
              if((ch[0][3] == 'X'|| ch[0][3]=='T') && (ch[1][2]=='X'||ch[1][2]=='T') && (ch[2][1] == 'X'||ch[2][1]=='T') && (ch[3][0]=='X'||ch[3][0]=='T'))
              ans = 1;
              if((ch[0][3] == 'O'|| ch[0][3]=='T') && (ch[1][2]=='O'||ch[1][2]=='T') && (ch[2][1] == 'O'||ch[2][1]=='T') && (ch[3][0]=='O'||ch[3][0]=='T'))
              ans = 2;
              //cout<<ans<<endl<<endl;
              if( ans ==0 )
              {
                  REP(i, 4)
                  {
                     if( ch[i][0] == '.' || ch[i][1]=='.' || ch[i][2]=='.' || ch[i][3] == '.')
                     ans = 3;
                  }
              }
              if( ans == 0)
              printf("Case #%d: Draw\n", ++ctr);
              else if( ans == 1)
              printf("Case #%d: X won\n", ++ctr);
              else if( ans == 2)
              printf("Case #%d: O won\n", ++ctr);
              else if(ans ==3)
              printf("Case #%d: Game has not completed\n", ++ctr);
    }
    return 0;
}
