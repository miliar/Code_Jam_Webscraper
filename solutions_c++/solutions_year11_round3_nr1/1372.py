#include<iostream>
#include<algorithm>
#include<ctime>
#include<stdio.h>
#include<string.h>
#include<map>
#include<vector>
#include<cmath>
#include<string>
#include<queue>
#include<sstream>
using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    while(cin >> t ){
      for(int cas=1; cas<=t; ++cas){
        int r,c;
        cin >> r >> c;
        string mp[100];
        for(int i=0; i<r; ++i) cin >> mp[i];
        int flag=0;
        if(r<2||c<2){
          for(int i=0; i<r && !flag; ++i)
          for(int j=0; j<c && !flag; ++j){
            if(mp[i][j]=='#') flag=1;
            break;
          }
        }
        for(int i=0; i<r && !flag; ++i)
          for(int j=0; j<c && !flag; ++j){
            if(mp[i][j]=='#'){
//                if(i==0 && j==0){
                  if(j+1<c && i+1<r && mp[i][j+1]=='#' && mp[i+1][j]=='#' && mp[i+1][j+1]=='#'){
                    mp[i][j]='/'; mp[i][j+1]='\\';
                    mp[i+1][j]='\\'; mp[i+1][j+1]='/';
                  }else{
                    flag=1;
                    break;
                  }
//                }else if(i==0){
//                  if( j+1<c && i+1<r && mp[i][j+1]=="#" && mp[i+1][j]=="#" && mp[i+1][j+1]=="#"){
//                    mp[i][j]='/'; mp[i][j+1]='\\';
//                    mp[i+1][j]='\\'; mp[i+1][j+1]='/';
//                  }else{
//                    flag=1;
//                    break;
//                  }
//                }
            }
          }
          cout << "Case #" << cas << ":" << endl;
          if(flag) cout << "Impossible" << endl;
          else {
            for(int i=0; i<r; ++i){
              for(int j=0; j<c; ++j)
              cout << mp[i][j];
              cout << endl;
            }
          }
      }
    }
	return 0;
}

