#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
  int NT;
  cin >> NT;
  for (int test=0;test<NT;test++) {
    int N;
    cin >> N;
    vector<int> a(N);
    for (int i=0;i<N;i++)
      cin >> a[i];
    sort(a.begin(), a.end());
    bool fl = false;
    for (int i=0;i<a.size();i++) {
      int cur = a[i];
      int targ = 0;
      for (int j=0;j<a.size();j++) {
	if (j==i) continue;
	targ = targ^a[j];
      }
      if (targ==cur) {
	cout << "Case #" << test+1 << ": ";
	int res=0;
	for (int j=0;j<a.size();j++) {
	  if (i==j) continue;
	  res+=a[j];
	}
	cout << res << endl;
	fl = true;
	break;
      }
    }
    if (!fl) cout << "Case #" << test+1 << ": NO" << endl;
  }
  return 0;
}
