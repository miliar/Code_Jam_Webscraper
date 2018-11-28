#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<set>
#include<list>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<functional>
using namespace std;
typedef long double LD;
typedef long long LLI;

int main() {
  int NT;
  cin >> NT;
  for (int test=1;test<=NT;test++) {
    int n;
    cin >> n;
    vector<vector<int> > teams;
    teams.resize(n, vector<int>(n,-1));
    for (int i=0;i<n;i++) 
      for (int j=0;j<n;j++) {
	char c;
	cin >> c;
	if (c=='1' || c=='0') teams[i][j] = c-'0';
      }
    vector<LD> WP(n,0), OWP(n,0), OOWP(n,0);
    vector<int> WP_all(n), WP_win(n);
    for (int i=0;i<n;i++) {
      int all=0,win=0;
      for (int j=0;j<n;j++) {
	if (teams[i][j]==1) {
	  all++;
	  win++;
	} else if (teams[i][j]==0) {
	  all++;
	}
      }
      WP[i] = (LD)win/(LD)all;
      WP_win[i] = win;
      WP_all[i] = all;
    }
    for (int i=0;i<n;i++) {
      LD sum = 0, num=0;
      for (int j=0;j<n;j++) {
	if (j==i) continue;
	if (teams[i][j] == 0)
	  sum+=(LD)(WP_win[j] - 1)/(LD)(WP_all[j] - 1),num++;
	else if (teams[i][j] == 1)
	  sum+=(LD)(WP_win[j])/(LD)(WP_all[j] - 1),num++;
	/*	  else
		  sum+=WP[j];*/
      }
      OWP[i] = sum/(LD)num;
    }

    for (int i=0;i<n;i++) {
      LD sum=0;
      int num=0;
      for (int j=0;j<n;j++) {
	if (teams[i][j]==0 || teams[i][j]==1) {
	  sum+=OWP[j];
	  num++;
	}
      }
      OOWP[i] = sum/num;
    }

    /*    for (int i=0;i<n;i++)
      cout << "WP[" << i << "]=" << WP[i] << endl;
    for (int i=0;i<n;i++)
      cout << "OWP[" << i << "]=" << OWP[i] << endl;
    for (int i=0;i<n;i++)
    cout << "OOWP[" << i << "]=" << OOWP[i] << endl;*/


    cout << "Case #" << test << ":" << endl;
    for (int i=0;i<n;i++)
      cout << 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i] << endl;
  }
  return 0;
}
