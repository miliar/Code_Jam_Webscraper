#include <iostream>
#include <map>
#include <string>

#define MAXQ 1100
#define MAXN 110
using namespace std;

map<string,int> m;

int n;
int v[MAXQ];
int q;

/*int minimize() {
  int dp[MAXN][MAXQ];
  for (int i=0;i<n;i++)
    dp[i][0]=(v[0]==i?1:0);
  for (int i=1;i<q;i++) {
    for  (int j=0;j<n;j++) {
      int minimo=MAXQ;
      for (int k=0;k<n;k++) {
	if (j==k && v[i]!=j)
	  minimo=min(minimo,dp[i-1][k]);
	if (j==k && v[i]==j)
	  minimo=min(minimo,dp[i-1][k]+2);
	if (j!=k && (v[i]==k || v[i]==j))
	  minimo=min(minimo,dp[i-1][k]+1);
	if (j!=k && v[i]!=k && v[i]!=j)
	  minimo=min(minimo,dp[i-1][k]+1);
      }	
      dp[i][j]=minimo;
      	
    } 
  }
  int minimo=MAXQ;
  for (int i=0;i<n;i++) 
    minimo=min(minimo,dp[q-1][i]);
  return minimo;  
  }*/

int minimize() {
  int dp[MAXQ][MAXN];
  memset(dp,0,sizeof(dp));
  //cout << v[q-1] << endl;
  for (int i=0;i<n;i++)
    dp[q-1][i]=(v[q-1]==i?1:0);
  /*for (int i=0;i<n;i++)
    cout << dp[q-1][i] << endl;*/
  for (int i=q-2;i>=0;i--) {
    for (int j=0;j<n;j++) {
      int minimo=MAXQ;
      for (int k=0;k<n;k++) {
	if (k==v[i])
	  continue;
	if (k==j)
	  minimo=min(minimo,dp[i+1][k]);
	else
	  minimo=min(minimo,dp[i+1][k]+1);
      }
      dp[i][j]=minimo;
    }
  }

  /*for (int i=0;i<n;i++) {
    for (int j=0;j<q;j++)
      cout << dp[j][i] << " ";
    cout << endl;
    }*/

  int minimo=MAXQ;
  for (int i=0;i<n;i++)
    minimo=min(minimo,dp[0][i]);
  return minimo;
}

int main() {
  int nc;
  string temp;
  cin >> nc;
  for (int t=1;t<=nc;t++) {
    cin >> n;
    cin.ignore();
    for (int i=0;i<n;i++) {
      getline(cin,temp);
      m[temp]=i;
    }
    /*for (map<string,int>::iterator it=m.begin();it!=m.end();it++)
      cout << it->first << endl;*/
    cin >> q;
    cin.ignore();
    for (int i=0;i<q;i++) {
      getline(cin,temp);
      v[i]=m[temp];
    }
    /*for (int i=0;i<q;i++)
      cout << v[i] << endl;*/
    cout << "Case #" << t << ": " << minimize() << endl;
  }
  return 0;
}
