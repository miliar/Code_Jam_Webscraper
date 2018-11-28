#include <iostream>
#include <iomanip>
#include <cstring>
#include <string>
using namespace std;

int main(){
  int a[200][200];
  double wp[200];
  double wpd[200];
  double owp[200];
  double oowp[200];
  double ans[200];
  int t;
  cin >> t;
  for (int xx=1;xx<=t;++xx){
    memset(a,0,sizeof a);
    memset(wp,0,sizeof wp);
    memset(wpd,0,sizeof wpd);
    memset(owp,0,sizeof owp);
    memset(oowp,0,sizeof oowp);
    memset(ans,0,sizeof ans);
    cout <<"Case #"<< xx<<":"<<endl;
    int n;
    cin >>n;
    string s;
    for (int i = 0; i < n;++i){
      cin >> s ;
      for (int j = 0; j< n; ++ j){
	if (s[j]=='1')
	  a[i][j] = 1;
	else 
	  if(s[j]=='.')
	    a[i][j] = 2;
	  else
	    a[i][j] = 0;
      }
    }
    for (int i = 0;i <n;++i){
      for (int j = 0;j<n;++j){
	if (a[i][j]==1){
	  wp[i]++;
	}
	if (a[i][j]==0||a[i][j]==1)
	  wpd[i]++;
      }
    }

    double towp = 0;
    for (int i = 0; i< n;++i){
      for (int j = 0;j<n;++j)
        if (a[j][i]!=2)
	  {
	    owp[i]+=(wp[j]-a[j][i])/(wpd[j]-1);
	  }
      owp[i]/=wpd[i];
    }
    for (int i = 0; i < n; ++i){
      for (int j = 0; j < n;++j)
	if (a[i][j]!=2){
	  oowp[i]+=owp[j];
	}
      oowp[i]/=wpd[i];
    }

    for (int i = 0; i < n; ++i){
      ans[i]=0.25*wp[i]/wpd[i]+0.5*owp[i]+0.25*oowp[i];
      cout <<setprecision(10)<< ans[i] << endl;
    }    
  }
}
