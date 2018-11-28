#include <iostream>
#include <map>

using namespace std;

const int maxn = 500;
const int modu = 100003;

int choose[maxn+1][maxn+1];
int d[maxn+1][maxn];

int main() {
  int t;
  cin >> t;
  for(int i=0;i<=maxn;i++)
    for(int j=0;j<=maxn;j++)
      if(j>i) choose[i][j] = 0;
      else if(j==0) choose[i][j] = 1;
      else choose[i][j] = (choose[i-1][j]+choose[i-1][j-1])%modu;
  
  for(int i=2;i<=maxn;i++){
    d[i][1] = 1;
    for(int j=2;j<i;j++){
      d[i][j] = 0;
      for(int k=1;k<j;k++)
	d[i][j] = (d[i][j] + d[j][k] * choose[i-j-1][j-k-1])%modu;
    }
  }


  for(int tcase=1;tcase<=t;tcase++){
    int n;
    cin >> n;

    //    for(int i=2;i<=n;i++,cerr<<'\n')
    //for(int j=1;j<i;j++) cerr << d[i][j] << ' ';

    int res = 0;
    for(int j=1;j<n;j++)
      res = (res + d[n][j]) % modu;

    cout << "Case #" << tcase << ": " << res << '\n';
  }
}
