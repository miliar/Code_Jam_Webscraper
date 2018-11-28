#include<cassert>
#include<queue>
#include<cstring>
#include<cstdio>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<iostream>
#include<algorithm>
#define eprintf(...) {fprintf(stderr, __VA_ARGS__);fflush(stderr);}

#define eps 1e-12

#define sqr(a) ((a)*(a))
#define mp(a,b) make_pair(a,b) 
#define forn(i,n) for(int i=0;i<(int)n;i++)
#ifdef DEBUG
#define deb(x) cerr<<#x<<'='<<x<<endl
#else
#define deb(x) 
#endif
typedef long long ll;

using namespace std;

char p[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
bool was[26];
char s[1000],t[1000];
int main()         
{
  #ifdef DEBUG
  freopen("in","r",stdin);
  freopen("out","w",stdout);
  #endif
  int n;
  scanf("%d ",&n);
  /*memset(p,-1,sizeof(p));
  forn(i,n){
    gets(s);
    gets(t);
    puts(s);
    puts(t);
    int m = strlen(s);
    forn(j,m)
      if(s[j] != ' '){
        p[s[j]-'a'] = t[j];
        was[t[j]-'a'] = 1;
      }
  }
  forn(i,26)
    printf("\'%c\',",p[i]);
  forn(i,26)
    if(!was[i])
      printf("%c",i + 'a');*/
  forn(i,n){
    gets(s);
    int m = strlen(s);
    printf("Case #%d: ",i+1);
    forn(j,m)
      printf("%c",isalpha(s[j])?p[s[j]-'a']:s[j]);
    puts("");
  }
  return 0;
}

