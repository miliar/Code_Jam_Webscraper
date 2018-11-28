#include <iostream>
#include <algorithm>

const int maxp = 10;
const int maxt = 1<<maxp;

int p, n, m;
int miss[maxt];
int price[maxt];
int d[2*maxt][maxp+1];

using namespace std;

const int inf = maxt * 2 * 100000 * 2; 

bool p2(int x) {
  for(int i=0;i<31;i++)
    if(1 << i == x) return true;
  return false;
}

int main() {
  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){
    cin >> p;
    n = 1<<p;
    m = (1<<p)-1;
    for(int i=0;i<n;i++)
      cin >> miss[i];

    for(int l=p-1;l>=0;l--)
      for(int i=(1<<l)-1;i<(1<<(l+1))-1;i++){
	cin >> price[i];
	//cerr << "price[" << i << "]=" << price[i] << '\n';
      }

    for(int i=0;i<n;i++)
      for(int j=0;j<=p;j++)
	if(j<=miss[i]) d[i+m][j] = 0;
	else d[i+m][j] = inf;

    for(int i=m-1;i>=0;i--){
      for(int j=0;j<p;j++){
	d[i][j] = min(d[2*i+1][j] + d[2*i+2][j] + price[i],
		      d[2*i+1][j+1] + d[2*i+2][j+1]);
	d[i][j] = min(d[i][j], inf);
      }
      d[i][p] = d[2*i+1][p] + d[2*i+2][p] + price[i];
      d[i][p] = min(d[i][p], inf);
    }
    /*
    for(int i=0;i<m+n;i++){
      cerr << '(' << price[i] << ':';
      for(int j=0;j<=p;j++)
	cerr << d[i][j] << ' ';
      cerr << ") ";
      if(p2(i+2)) cerr << '\n';
    }
    cerr << '\n';*/
    
    cout << "Case #" << tcase << ": " << d[0][0] << '\n';
  }
}

