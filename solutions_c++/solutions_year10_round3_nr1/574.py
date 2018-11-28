#include <fstream>
#include <vector>
#include <utility>
using namespace std;

#define X first
#define Y second

int main() {
  ifstream cin("input.txt");
  ofstream cout("output.txt");
  int t;
  cin >> t;
  for(int tc=1; tc<=t; tc++) {
    int n;
	cin >> n;
	vector<pair<int,int> > a(n);
	for(int i=0; i<n; i++)
	  cin >> a[i].X >> a[i].Y;
	int cnt=0;
    for(int i = 1; i < a.size(); ++i) {
      for(int j = 0; j < i; ++j) {
        if((a[i].X - a[j].X) * (a[i].Y - a[j].Y) < 0) {
          ++cnt;
        }
      }
    }
	

	cout << "Case #" << tc << ": " << cnt << endl;
  }
  return 0;
}