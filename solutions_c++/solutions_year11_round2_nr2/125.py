#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
using namespace std;

bool cansolve(vector<int>&pos, vector<int>&cnt, double dist, double time) {
	double mustMoveAtLeastTo = -1e200;
	for (int i=0;i<pos.size();i++) {
///		cout << i << cnt[i] << " " << pos[i] <<endl;
		double span = (cnt[i]-1) * dist;
		double leftmostpossible = pos[i] - time;
		double gotopos = max(mustMoveAtLeastTo, leftmostpossible);
		double rightmostpos = gotopos + span;
	//	cout<< span << " " << leftmostpossible << " " << gotopos << " " << rightmostpos << endl;
		if (rightmostpos > pos[i] + time) return false;
		mustMoveAtLeastTo = rightmostpos+dist;
	}
	return true;
}
void tc(int tcn) {
	int c;
	double d;
	cin >> c >> d;

	vector<int> pos(c);
	vector<int> cnt(c);
	for (int i=0;i<c;i++){cin>>pos[i]>>cnt[i]; }
	double min = 0.0;
	double max = 1e30;
//	cout << cansolve(pos,cnt,d,0.5) << endl;
//cout << endl;
//	cout << cansolve(pos,cnt,d,1.5) << endl;

//	exit(0);	
	while (max - min > 0.0000001) {
		double mid = (max+min)/2;
		if (mid == max || mid == min) break;
		if (cansolve(pos,cnt,d,mid))
			max = mid;
		else
			min = mid;
	}
	cout << setprecision (15);
	cout << "Case #"<<tcn << ": "<<((max+min)/2) << endl;

}
int main() {
	int t;
	cin>>t;
	for (int i=1;i<=t;i++) tc(i);
}
