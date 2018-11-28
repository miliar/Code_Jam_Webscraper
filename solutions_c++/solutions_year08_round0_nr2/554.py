#include <iostream>
#include <vector>
#include <string>

using namespace std;

int cts(string t){
	int minutes = (t[0] - '0') * 60 * 10;
	minutes += (t[1] - '0') * 60;
	minutes += (t[3] - '0') * 10;
	minutes += (t[4] - '0');
	return minutes;
}

int main(){
	int ntc; cin >> ntc;
	
	for (int tc = 1; tc <= ntc; tc++) {
		int turn; cin >> turn;
		int nab; cin >> nab;
		int nba; cin >> nba;
		
		vector<int> starts_ab;
		vector<int> ends_ab;
		vector<int> starts_ba;
		vector<int> ends_ba;
		
		for (int t = 0; t < nab; t++) {
			string stime, etime;
			cin >> stime >> etime;
			int sint = cts(stime);
			int eint = cts(etime) + turn;
			starts_ab.push_back(sint);
			ends_ab.push_back(eint);
		}

		for (int t = 0; t < nba; t++) {
			string stime, etime;
			cin >> stime >> etime;
			int sint = cts(stime);
			int eint = cts(etime) + turn;
			starts_ba.push_back(sint);
			ends_ba.push_back(eint);
		}
		
		sort(starts_ab.begin(), starts_ab.end(), greater<int>());
		sort(ends_ab.begin(), ends_ab.end());
		sort(starts_ba.begin(), starts_ba.end(), greater<int>());
		sort(ends_ba.begin(), ends_ba.end());
		
		int ap_ab = 0;
		while (true) {
			if (ends_ab.size()==0) break;
			if (ap_ab > ends_ab.size() - 1 || starts_ba.size() == 0 || ends_ab[ap_ab] > starts_ba[0]) break;
			unsigned int i;
			for (i = 0; i < starts_ba.size(); i++) {
				if (i == starts_ba.size() || starts_ba[i] < ends_ab[ap_ab]) break;
			}
			vector<int>::iterator it = starts_ba.begin(); while(i>1) {it++;i--;}
			starts_ba.erase(it); nba--;
			ap_ab++;
		}

		int ap_ba = 0;
		while (true) {
			if (ends_ba.size()==0) break;
			if (ap_ba > ends_ba.size() - 1 || starts_ab.size() == 0 || ends_ba[ap_ba] > starts_ab[0]) break;
			unsigned int i;
			for (i = 0; i < starts_ab.size(); i++) {
				if (i == starts_ab.size() || starts_ab[i] < ends_ba[ap_ba]) break;
			}
			vector<int>::iterator it = starts_ab.begin(); while(i>1) {it++;i--;}
			starts_ab.erase(it); nab--;
			ap_ba++;
		}

		
		cout << "Case #" << tc << ": " << nab << ' ' << nba << endl;
	}
	
	return 0;
}