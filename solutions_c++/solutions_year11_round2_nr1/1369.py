#include<iostream>
using namespace std;

char s[100][100];
int n;

double wp(int x,int d){
  int win=0,game=0;
  for(int i=0;i<n;i++){
    if(i!=d){
      if(s[x][i]=='1'){
	win++;
	game++;
      }else if(s[x][i]=='0')game++;
    }
  }
  return (double)win/game;
}

double owp(int x,int d){
  double w,ans=0;
  int game=0;
  for(int i=0;i<n;i++){
    w = 0;
    if(i!=d){
      if(s[x][i]!='.'){
	w = wp(i,x);
	game++;
      }
    }
    ans += w;
  }
  return ans/game;
}

double oowp(int x){
  double ow,ans=0;
  int game=0;
  for(int i=0;i<n;i++){
    ow = 0;
    if(s[x][i]!='.'){
      ow = owp(i,n);
      game++;
    }
    ans += ow;
  }
  return ans/game;
}

int main(){
  int t;

  cin >> t;
  for(int i=0;i<t;i++){
    cin >> n;
    for(int j=0;j<n;j++){
      for(int k=0;k<n;k++){
	cin >> s[j][k];
      }
    }
    cout << "Case #" << i+1 << ':' << endl;
    for(int j=0;j<n;j++){
      cout << 0.25*wp(j,n) + 0.50*owp(j,n) + 0.25*oowp(j) << endl;
    }
  }
}
