#include <iostream>
#include <vector>
using namespace std;

bool can(const vector<int> &v, int r) {
	vector<int> skipped;
	int last = v[0];
	int curLen = 1;
	for (int i=1;i<v.size();i++) {
		if (v[i] == last) {
			if (skipped.size() > 0 && skipped[skipped.size() - 1] < v[i] - 1) return false;
			skipped.push_back(v[i]);
		} else if (v[i] == (last + 1)) {
			last = v[i];
			curLen++;
		} else {
			if (curLen < r) return false;			
			curLen = 1;
			last = v[i];
		}
		if (skipped.size() > 0 && curLen >= r) {
			vector<int> v2 = skipped;
			for (int j=i+1;j<v.size();j++)
				v2.push_back(v[j]);
			if (can(v2, r)) return true;
		}
	}
	return curLen >= r && skipped.size() == 0;
}
void tc(int tcn) {
	int n;
	cin>>n;
	if (n==0) {
		cout << "Case #" << tcn << ": " << 0 << endl;
		return;
	}
	vector<int> v(n);
	for (int i=0;i<n;i++)cin>>v[i];
	sort(v.begin(),v.end());
	int m = 1;
	int M = n+1;
	//cout << "*" << can(v, 4)<<endl;
	while (M - m > 1) {
		int mid = m + (M-m)/2;
		if (can(v, mid))
			m = mid;
		else
			M = mid;
	}
	cout << "Case #" << tcn << ": " << m << endl;

}
int main() {
	int n;
	cin >> n;
	for (int i=0;i<n;i++)tc(i+1);
}