#include <fstream>
#include <vector>
using namespace std;

int main() {
  ifstream cin("input.txt");
  ofstream cout("output.txt");

  int nt;
  cin >> nt;
  for(int tc=1; tc<=nt; tc++) {
    int n,k,t,b;
    cin >> n >> k >> b >> t;
    vector<int> v(n),x(n);
    vector<int> can;

    for(int i=0;i<n;i++)
      cin >> x[i];
    for(int i=0;i<n;i++)
      cin >> v[i];

    for(int i=v.size()-1;i>=0 && can.size()<k; i--)
      if((b - x[i]) <= t * v[i])
      can.push_back(v.size() - i - 1);

    if(can.size()<k) {
	  cout << "Case #" << tc << ": IMPOSSIBLE" << endl; 
      continue;
    }
    int res = 0;
    for(int i=0;i<can.size();i++)
      res += can[i] - i;
    cout << "Case #" << tc << ": " << res << endl;
  }
return 0;
}
