#include <iostream>
#include <string>
#include <cstdio>
#include <memory.h>
using namespace std;
const string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
const string b = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
const string c = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
const string d = "our language is impossible to understand";
const string e = "there are twenty six factorial possibilities";
const string f = "so it is okay if you want to just give up";
const int N = 27;
int dp[N];

void pre(){
      memset(dp,-1,sizeof(dp));
      int l = a.length();
      for (int i=0;i<l;i++){
            if (a[i] == ' ') continue;
            dp[a[i]-97] = d[i]-97;
      }
      l = b.length();
      for (int i=0;i<l;i++){
            if (b[i] == ' ') continue;
            dp[b[i]-97] = e[i]-97;
      }
      l = c.length();
      for (int i=0;i<l;i++){
            if (c[i]== ' ') continue;
            dp[c[i]-97] = f[i]-97;
      }
      dp['q'-97]='z'-97;
      dp['z'-97]='q'-97;
      return ;
}
int main(){
      pre();
    //  freopen("test.in","r",stdin);
  //    freopen("test.out","w",stdout);
      int T;cin>>T;getchar();
      for (int t=1;t<=T;t++){
            string s;
            getline(cin,s);
            printf("Case #%d: ",t);
            int l = s.length();
            for (int i=0;i<l;i++){
                  if (s[i]==' ') {printf(" "); continue;}
                  char ch = 97+(char)dp[s[i]-97];
                  printf("%c",ch);
            }
            puts("");
      }
      return 0;
}
