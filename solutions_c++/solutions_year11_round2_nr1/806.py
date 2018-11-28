#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const int MAXN = 110;

int played[MAXN];
int won[MAXN];
double owp[MAXN];
double oowp[MAXN];
double rpi[MAXN];

int qwer(char x){
  if(x == '0')
    return 1;
  if(x == '1')
    return 0;
  return 0;
}

int main(){
  //freopen("rpi.in", "r", stdin);
  //freopen("x.out", "w", stdout);
  
  
  int testcases;
  scanf("%d", &testcases);
  string s[110];
  
  for(int test = 0; test < testcases; test++){
    fill(played, played + MAXN, 0);
    fill(won, won + MAXN, 0);
    fill(owp, owp + MAXN, 0);
    fill(oowp, oowp + MAXN, 0);
    
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++)
      cin >> s[i];
    
    for(int i = 0; i < n; i++){
      for(int j = 0; j < n; j++){
	  if(s[i][j] == '0')
	    played[i]++;
	  if(s[i][j] == '1'){
	    played[i]++;
	    won[i]++;
	  }
      }
    }
    
    //for(int i = 0; i < n; i++)
    //  cout << won[i] << " " << played[i] << endl;
     
    for(int i = 0; i < n; i++){
      for(int j = 0; j < n; j++)
	if(s[i][j] != '.')
	  owp[i] += double((double) (won[j] - qwer(s[i][j]) ) / (played[j]-1) );
      owp[i] /= played[i];
      //cout << owp[i] << endl;
    }
    
    for(int i = 0; i < n; i++){
      for(int j = 0; j < n; j++)
	if(s[i][j] != '.')
	  oowp[i] += owp[j];
      oowp[i] /= played[i];
      //cout << oowp[i] << endl;
    }
    
    printf("Case #%d:\n", test+1);
    for(int i = 0; i < n; i++){
     //cout << won[i]/played[i] << endl;
     cout << ((double)(  0.25 * ((double)won[i]/played[i]) + 0.50 * owp[i] + 0.25 * oowp[i] ) ) << endl;
    }
    
  }
  return 0;
}