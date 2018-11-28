#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
#include<queue>
#include<set>
#include<memory.h>
#include<cstdlib>
using namespace std;
#define pb push_back
#define ins insert
#define front(i) ((1<<(i))-1)
// 13C

#define rep(n)  for(int               repp = 0; repp <    (n); ++repp)
#define repc(n) for(int repp_b = (n), repp = 0; repp < repp_b; ++repp)
#define rst(a, v) memset(a, v, sizeof a)
#define cpy(a, b) memcpy(a, b, sizeof a)
#define rstn(a, v, n) memset(a, v, (n)*sizeof((a)[0]))
#define cpyn(a, b, n) memcpy(a, b, (n)*sizeof((a)[0]))
#define ast(b) if(DBG && !(b)) { printf("!! %d\n", __LINE__); while(1) getchar(); }
#define dout DBG && cout << ">>| "
#define pr(x) #x"=" << (x) << " | "
#define mk(x) DBG && cout << "**| "#x << endl
#define pra(arr, a, b) if(DBG) { \
    dout<<#arr"[] | "; \
    forlec(i, a, b) cout<<"["<<i<<"]="<<arr[i]<<" |"<<((i-(a)+1)%13?" ":"\n"); \
    if(((b)-(a)+1)%13) puts(""); \
  }
#define rd(type, x) type x; cin >> x
inline int     rdi() { int d; scanf("%d", &d); return d; }
inline char    rdc() { scanf(" "); return getchar(); }
inline string  rds() { rd(string, s); return s; }
inline double rddb() { double d; scanf("%lf", &d); return d; }
template<class T> inline bool updateMin(T& a, T b) { return a>b? a=b, true: false; }
template<class T> inline bool updateMax(T& a, T b) { return a<b? a=b, true: false; }

int i,j;
char map[7][7];
char ans[6][30]{"cc","X won","O won","Draw","Game has not completed"};
int cc(){
    int sumo,sumx,sum;
    sumo=sumx=0;
    for(i=0;i<4;i++){
        for(sumx=sumo=j=0;j<4;j++){
            if(map[i][j]=='X'||map[i][j]=='T')sumx++;
            if(map[i][j]=='O'||map[i][j]=='T')sumo++;
        }
        if(sumx==4)return 1;
        else if(sumo==4)return 2;
        for(sumx=sumo=j=0;j<4;j++){
            if(map[j][i]=='X'||map[j][i]=='T')sumx++;
            if(map[j][i]=='O'||map[j][i]=='T')sumo++;
        }
        if(sumx==4)return 1;
        else if(sumo==4)return 2;
    }
    //puts("ii");
    for(sumo=sumx=i=0;i<4;i++){
        if(map[i][i]=='X'||map[i][i]=='T')sumx++;
        if(map[i][i]=='O'||map[i][i]=='T')sumo++;
    }if(sumo==4)return 2;else if(sumx==4)return 1;
    sumo=sumx=0;
    for(i=3;i>=0;i--){
        if(map[3-i][i]=='X'||map[3-i][i]=='T')sumx++;
        if(map[3-i][i]=='O'||map[3-i][i]=='T')sumo++;
    }if(sumo==4)return 2;else if(sumx==4)return 1;
    for(sum=i=0;i<4;i++)for(j=0;j<4;j++)if(map[i][j]=='.')return 4;
    return 3;
}

int main(){
  int test;
  int cas=0;
  //freopen("A-large.in","r",stdin);
  //freopen("ou.txt","w",stdout);
  scanf("%d ",&test);
  while(test--){
     for(int i=0;i<4;i++){
         scanf("%s",map[i]);
     }
     printf("Case #%d: ",++cas);
     //cout<<cc()<<endl;
     puts(ans[cc()]);
  }
  //system("pause");
  return 0;
}
