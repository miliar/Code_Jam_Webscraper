#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
const double EPS = 1e-8;
const int INF = (1<<29);

char st[100][100], s[100][100];
int n,m;

int main(){
  int ca; scanf("%d",&ca);
  for (int tt=1; tt<=ca; tt++){
    scanf("%d%d",&n,&m);
    for (int i=0; i<n; i++) scanf("%s",st[i]);
    memset(s,0,sizeof(s));
    for (int i=0; i<n; i++){
      for (int j=0; j<n; j++) s[i][j]=st[n-j-1][i];
    }
    for (int i=0; i<n; i++){
      for (int t=0; t<n; t++){
        for (int j=0; j<n-1; j++){
          if (s[j+1][i]=='.'){
            s[j+1][i]=s[j][i];
            s[j][i]='.';
          }
        }
      }
    }

    bool bw=false, rw=false;
    for (int i=0; i<n; i++){
      for (int j=0; j<n-m+1; j++){
        bool bb=true, rr=true;
        for (int k=0; k<m; k++){
          if (s[j+k][i]!='B') bb=false;
          if (s[j+k][i]!='R') rr=false;
        }
        if (bb) bw=true;
        if (rr) rw=true;
      }
    }
    for (int i=0; i<n; i++){
      for (int j=0; j<n-m+1; j++){
        bool bb=true, rr=true;
        for (int k=0; k<m; k++){
          if (s[i][j+k]!='B') bb=false;
          if (s[i][j+k]!='R') rr=false;
        }
        if (bb) bw=true;
        if (rr) rw=true;
      }
    }
    for (int i=0; i<n; i++){
      for (int j=0; j<n; j++){
        if (!(i+m-1<n && j+m-1<n)) continue;
        bool bb=true, rr=true;
        for (int k=0; k<m; k++){
          if (s[i+k][j+k]!='B') bb=false;
          if (s[i+k][j+k]!='R') rr=false;
        }
        if (bb) bw=true;
        if (rr) rw=true;
      }
    }
    for (int i=0; i<n; i++){
      for (int j=0; j<n; j++){
        if (!(i>=m-1 && j+m-1<n)) continue;
        bool bb=true, rr=true;
        for (int k=0; k<m; k++){
          if (s[i-k][j+k]!='B') bb=false;
          if (s[i-k][j+k]!='R') rr=false;
        }
        if (bb) bw=true;
        if (rr) rw=true;
      }
    }



    printf("Case #%d: ",tt);
    if (!bw && !rw) printf("Neither\n");
    else if (bw && rw) printf("Both\n");
    else if (bw) printf("Blue\n");
    else if (rw) printf("Red\n");

  }
  return 0;
}
