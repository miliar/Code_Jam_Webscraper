#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <algorithm>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)

using namespace std;

#define L 19
string welcome = "welcome to code jam";
string str;
char WEL[L+1];
int TAB[L][550];
char STR[550];

int main(){
  strcpy(WEL, welcome.c_str());
  int CN;
  cin >> CN;
  cin.getline(STR,550);

  For1(CI,CN){
    memset(TAB,-1,sizeof(TAB));
    memset(STR,0,sizeof(STR));
    getline(cin,str);
    strcpy(STR,str.c_str());
    int W = strlen(STR);
    For(h, L){
      For(w, W){
        if(WEL[h]==STR[w])
          TAB[h][w]=0;
      } 
    }
    For(w, W){
      if(TAB[L-1][w]==0)
        TAB[L-1][w]=1;
    }
    for(int h=L-2;h>=0;h--){
      int tot=0;
      for(int w=W-1;w>=0;w--){
        if(TAB[h][w]==0){
          TAB[h][w]=tot;
        }
        if(TAB[h+1][w]>0)
          tot=(tot+TAB[h+1][w])%10000;
      }
    }
    int res=0;
    For(w, W){
      if(TAB[0][w]>0)
        res = (res+TAB[0][w])%10000;
    }

    //4 digits!
    cout << "Case #" << CI << ": " << setw(4) << setfill('0') << res << endl;
  }
}

