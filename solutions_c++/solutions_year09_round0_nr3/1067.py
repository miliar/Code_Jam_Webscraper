#include <iostream>
#include <string>
using namespace std;
int main(){
  int n;
  string sstr = "welcome to code jam";
  string istr;
  int g[600][20];
  cin >> n;
  getline(cin,istr);

  for (int i=0;i<n;++i){
    getline(cin,istr);
    memset(g,0,sizeof(g));
    g[0][0] = 1;

    for (int j=0;j<istr.length();++j){
      g[j+1][0] = 1;
      for (int k=0;k<sstr.length();++k)
	g[j+1][k+1] = (g[j][k+1] + ((istr[j] == sstr[k]) ? g[j][k] : 0)) % 10000;
    }

    cout<< "Case #" <<i+1<<": ";
    int ans = g[istr.length()][sstr.length()];
    cout<< ans / 1000 << ans % 1000 / 100 << ans % 100 / 10 << ans % 10 << endl;
  }
}
      
