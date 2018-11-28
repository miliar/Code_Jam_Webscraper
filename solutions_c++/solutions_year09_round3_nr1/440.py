#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <algorithm>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)
#define ll unsigned long long

using namespace std;

char IN[100];
char CK[100];
char SY[100];

int main(){
  int CN;
  cin >> CN;
  For1(CI,CN){
    memset(IN,0,sizeof(IN));
    memset(CK,0,sizeof(CK));
    memset(SY,0,sizeof(SY));
    string s;
    cin >> s;
    strcpy(IN, s.c_str());
    int len=s.size();

    int cnt = 0;
    For(i,len){
      int j=0;
      for(;j<cnt;j++){
        if(IN[i]==CK[j]){
          break;
        }
      }
      if(j>=cnt)
        CK[cnt++]=IN[i];
    }
    if(cnt<2)
      cnt=2;

    ll res;
    if(len==1){
      res = 1;
    }
    else{
      SY[1]=IN[0];
      SY[0]='A';//default just in case
      For(i,len){
        if(IN[i]!=SY[1]){
          SY[0]=IN[i];
          break;
        }
      }
      if(len>2){
        int sc=2;
        For(ii,len){
          int si;
          for(si=0;si<sc;si++){
            if(IN[ii]==SY[si])
              break;
          }
          if(si>=sc){
            SY[sc++]=IN[ii];
          }
        }
      }

      res = 0;
      For(i,len){
        res *= cnt;
        int d;
        for(int si=0;true;si++){
          if(SY[si]==IN[i]){
            d=si;
            break;
          }
        }
        res += d;
      }
    }

    cout << "Case #" << CI << ": " << res << endl;
  }
}
