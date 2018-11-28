#include<algorithm>
#include<cstdio>
#include<vector>
#include<cmath>
#include<cstring>
#define INF 2000000000
#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define FORD(i, a, b) for(int i = (a); i >= (b); i--)
#define PI pair<int, int>
#define ST first
#define ND second
#define CLR(a, b) memset(a, b, sizeof(a))
#ifdef DEBUG
  #define DBG printf
#else
  #define DBG
#endif
using namespace std;

char tr[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main(){
  char s[200];
  int t;
  scanf("%d",&t);
  getchar();
  int casenum = 0;
  while(t--){
    casenum++;
    printf("Case #%d: ", casenum);
    gets(s);
    int len = strlen(s);
    REP(i, len){
      if( s[i] == ' ') printf(" ");
      else printf("%c",tr[ s[i]-'a' ]);
    }
    printf("\n");
  }
  return 0;
}
