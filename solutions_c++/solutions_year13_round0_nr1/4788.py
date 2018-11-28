#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <queue>
using namespace std;
#define rep(i,k) for(int i=0;i<(int)(k);i++)
#define foreach(i,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define forinc(i,a,b) for(int i=(a);i<(int)(b);i++)
#define fordec(i,a,b) for(int i=(a);i>(int)(b);i--)

typedef long long llint;

const int INF = (1<<29);
const llint LINF = (1LL<<61);
const double DINF = (1e100);

int judge(char s[][11])
{

    rep(i,4) if(s[i][0]==s[i][1]&&s[i][1]==s[i][2]&&s[i][2]==s[i][3]&&s[i][0]!='.') return s[i][0]=='X'?1:2;
    rep(i,4) if(s[0][i]==s[1][i]&&s[1][i]==s[2][i]&&s[2][i]==s[3][i]&&s[0][i]!='.') return s[0][i]=='X'?1:2;

    if(s[0][0]==s[1][1]&&s[1][1]==s[2][2]&&s[2][2]==s[3][3]&&s[0][0]!='.') return s[0][0]=='X'?1:2;
    if(s[0][3]==s[1][2]&&s[1][2]==s[2][1]&&s[2][1]==s[3][0]&&s[0][3]!='.') return s[0][3]=='X'?1:2;

    rep(i,4) rep(j,4) if(s[i][j]=='.') return 4;
    return 3;

}
int main(int argc, char *argv[]) {
  // freopen("A-small-attempt0.in", "r", stdin);
//   freopen("A-small-attempt1.in", "r", stdin);
//   freopen("A-small-attempt2.in", "r", stdin);
   freopen("A-large.in", "r", stdin);
   freopen("out.txt", "w", stdout);

   int ncase; scanf("%d",&ncase);
   rep(icase, ncase) {
       char s[11][11];
       string answer="";
       rep(i,4) scanf("%s",s[i]);
       int posTi=-1,posTj=-1;
       rep(i,4) rep(j,4) if(s[i][j]=='T') posTi=i,posTj=j;
       if(posTi==-1)
       {
           int res=judge(s);
           if(res==1) answer="X won";
           else if(res==2) answer="O won";
           else if(res==3) answer="Draw";
           else if(res==4) answer="Game has not completed";
       }
       else
       {
           // printf("dsafasdf\n");
           s[posTi][posTj]='X';
           int res1=judge(s);
          //  printf("dsafasdf\n");
           s[posTi][posTj]='O';
           int res2=judge(s);
          //  printf("dsafasdf %d %d\n", res1,res2);
           if(res1==1||res2==1) answer="X won";
           else if(res1==2||res2==2) answer="O won";
           else if(res1==3) answer="Draw";
           else if(res1==4) answer="Game has not completed";
       }
       //printf("aa");
      // cout <<answer<<"aa"<<endl;
       printf("Case #%d: %s\n", icase+1, answer.c_str());
       //printf("bb");
   }

   return 0;
}
