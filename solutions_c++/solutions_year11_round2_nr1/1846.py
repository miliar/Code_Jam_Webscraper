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
    string str[109];
    int t;
    while(cin >> t ){
      for(int cas=1; cas<=t; ++cas){
        int n;
        cin >> n;
        for(int i=0; i<n; ++i)
        cin >> str[i];
        long  double wp[109],owp[109],oowp[109];
        for(int i=0; i<n; ++i){
          int win=0,sum=0;
          for(int j=0; j<n; ++j){
            if(str[i][j]!='.') sum++;
            if(str[i][j]=='1') win++;
          }
          wp[i]=(win+0.0)/sum;
        }
//        for(int i=0; i<n; ++i) cout << wp[i] << " ";
//        cout << endl;

        for(int i=0; i<n; ++i){
          //cout << "#" << i << endl;
          int sum=0;
          long double win=0;
          for(int j=0; j<n; ++j){
            if(str[i][j]!='.'){
             sum++;
             int a=0,b=0;
             for(int k=0; k<n; ++k){
              if(str[j][k]!='.' && k!=i) b++;
              if(str[j][k]=='1' && k!=i) a++;
             }
             //cout << j << " " << a << " " << b << " " << win << endl;
             win+=(a+0.0)/b;
            }
          }
          if(sum==0) owp[i]=0;
          else owp[i]=(win+0.0)/sum;
        }

//        for(int i=0; i<n; ++i) cout << owp[i] << " ";
//        cout << endl;
        for(int i=0; i<n; ++i){
          int sum=0;
          long double win=0;
          for(int j=0; j<n; ++j){
            if(str[i][j]!='.'){
              sum++;
              win+=owp[j];
            }
          }
          oowp[i]=(win+0.0)/sum;
        }
//        for(int i=0; i<n; ++i) cout << oowp[i] << " ";
//        cout << endl;
        cout << "Case #" << cas << ": " << endl;
        for(int i=0; i<n; ++i){
          cout << 0.25*wp[i]+0.50*owp[i]+0.25*oowp[i] << endl;
        }
      }
    }
	return 0;
}

