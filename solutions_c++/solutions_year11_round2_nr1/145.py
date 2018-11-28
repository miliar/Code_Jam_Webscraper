#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))

char s[200][200];
double wp[200], owp[200],oowp[200];
double twp[200][200], towp[200][200];
int n;
int main(){
  int tc; scanf("%d",&tc);
  FOE(ca,1,tc){
    scanf("%d",&n);
    FOR(i,0,n) scanf("%s",s[i]);
    FOR(i,0,n){
      int c1=0, c2=0;
      FOR(j,0,n){
        if (s[i][j]=='1') c1++;
        else if (s[i][j]=='0') c2++;
      }
      wp[i] = c1*1./(c1+c2);

      FOR(j,0,n){
        int c1=0, c2=0;
        FOR(k,0,n){
          if (k==j) continue;
          if (s[i][k]=='1') c1++;
          else if (s[i][k]=='0') c2++;
        }
        twp[i][j] = c1*1./(c1+c2);
      }
    }
    FOR(i,0,n){
      int cnt=0;
      owp[i] = 0;
      FOR(j,0,n){
        if (s[i][j]!='.'){ owp[i]+=twp[j][i]; cnt++; }
      }
      owp[i] /= cnt;

/*
      FOR(j,0,n){
        int cnt=0;
        towp[i][j]=0;
        FOR(k,0,n){
          if (j==k) continue;
          if (s[i][k]!='.'){ towp[i][j]+=twp[k][i]; cnt++; }
        }
        towp[i][j] /= cnt;
      }
      */
    }
    FOR(i,0,n){
      int cnt=0;
      oowp[i] = 0;
      FOR(j,0,n){
        if (s[i][j] != '.'){ oowp[i]+=owp[j]; cnt++; }
      }
      oowp[i] /= cnt;
    }
    /*
    FOR(i,0,n) printf("%f ",wp[i]); puts("");
    FOR(i,0,n) printf("%f ",owp[i]); puts("");
    FOR(i,0,n) printf("%f ",oowp[i]); puts("");
    */
    printf("Case #%d:\n",ca);
    FOR(i,0,n){
      double rpi = .25*wp[i] + .5*owp[i] + .25*oowp[i];
      printf("%.8f\n",rpi);
    }
  }
  return 0;
}
