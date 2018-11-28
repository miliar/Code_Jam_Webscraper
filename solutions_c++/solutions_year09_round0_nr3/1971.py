#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;
string pattern="welcome to code jam";
int patternLen = pattern.length();
char str[502];
int M[502][50];
int strLen;
int solve(int s, int p) {
  if(p==patternLen) return 1;
  if(s==strLen || p==patternLen) return 0;
  int &ret = M[s][p];
  if(ret!=-1) return ret;
  ret=0;
  if(pattern[p]==str[s]) ret = solve(s+1,p+1);
  ret += solve(s+1,p);
  return ret%10000;
}

int main() {
 int T;
 scanf("%d",&T);
 gets(str);
 for(int i=1;i<=T;i++) {
   gets(str);
   strLen = strlen(str);
   memset(M,-1,sizeof(M));
   printf("Case #%d: %04d\n", i, solve(0,0)%10000);
 }
}