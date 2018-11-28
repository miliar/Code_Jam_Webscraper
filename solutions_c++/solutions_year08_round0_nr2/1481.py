#include<iostream>
#include<string>
#include<fstream>
#include<sstream>
#include<vector>
#include<algorithm>
using namespace std;

void incrementT(string &t, int i) {
	int h=atoi(t.substr(0,2).c_str());
	int m=atoi(t.substr(3,2).c_str());
	m+=i;
	if (m>=60) {
		m-=60;
		h++;
	}
	ostringstream o;
	if (h<10) o << '0';
	o << h << ':';
	if (m<10) o << '0';
	o << m;
	t=o.str();
}

int main() {
	std::freopen("stdout.txt", "w", stdout);
	int totNum;
	ifstream mFile("B-large.in.txt");
	mFile >> totNum;
	for (int i=0;i<totNum;i++) {
		int T, NA, NB;
		string temp1, temp2;
		vector <pair<string, string > > times;

		mFile >> T;
		mFile >> NA >> NB;

		for (int j=0;j<NA;j++) {
			mFile >> temp1 >> temp2;
			times.push_back(make_pair(temp1,"DA"));
			incrementT(temp2, T);
			times.push_back(make_pair(temp2,"AA"));
		}

		for (int j=0;j<NB;j++) {
			mFile >> temp1 >> temp2;
			times.push_back(make_pair(temp1,"DB"));
			incrementT(temp2, T);
			times.push_back(make_pair(temp2,"AB"));
		}

		sort(times.begin(),times.end());

		int ANow, BNow, AStart, BStart;
		
		ANow=0;BNow=0;AStart=0;BStart=0;

		for(int j=0;j<times.size();j++) {
			if (times[j].second[0]=='D') { // Departure
				if (times[j].second[1]=='A') { // From A
					if (ANow==0)
						AStart++;
					else
						ANow--;
				}
				else { // From B
					if (BNow==0)
						BStart++;
					else
						BNow--;
				}
			}
			else { // Arrival
				if (times[j].second[1]=='A') { // From A
					BNow++;
				}
				else { // From B
					ANow++;
				}
			}
		}

		cout << "Case #" << i+1 << ": " << AStart << ' ' << BStart << endl;
	};
	return 0;
};