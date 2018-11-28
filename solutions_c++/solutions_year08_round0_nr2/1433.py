#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct trip
{
	int dep;
	int arr;
	
	const bool operator<(const trip &t) const
	{
		if(dep < t.dep) return true;
		if(dep > t.dep) return false;

		return false;
	}
};



int main()
{
	int ncases;
	cin >> ncases;
	for(int count = 0; count < ncases; ++count) {
		int time;
		cin >> time;
		int na, nb;
		vector<trip> Atrip;
		vector<trip> Btrip;

		cin >> na >> nb;
		for(int i = 0; i < na; ++i) {
			string dep;

			cin >> dep;
			int b = dep.find_first_of(":");
			trip t;
			t.dep = atoi(dep.substr(0, b).c_str())*60;
			t.dep += atoi(dep.substr(b+1).c_str());

			cin >> dep;
			b = dep.find_first_of(":");
			t.arr = atoi(dep.substr(0, b).c_str())*60;
			t.arr += atoi(dep.substr(b+1).c_str());

			Atrip.push_back(t);
		}
		for(int i = 0; i < nb; ++i) {
			string dep;

			cin >> dep;
			int b = dep.find_first_of(":");
			trip t;
			t.dep = atoi(dep.substr(0, b).c_str())*60;
			t.dep += atoi(dep.substr(b+1).c_str());

			cin >> dep;
			b = dep.find_first_of(":");
			t.arr = atoi(dep.substr(0, b).c_str())*60;
			t.arr += atoi(dep.substr(b+1).c_str());

			Btrip.push_back(t);
		}
		sort(Atrip.begin(), Atrip.end());
		sort(Btrip.begin(), Btrip.end());
		
		int train[2];
		train[0] = train[1] = 0;

		int firstArr = 0;
		char firstSrc;
		char fTrain;

		bool newTrain = true;

		if(newTrain) {
			if(Atrip[0] < Btrip[0]) {
				firstSrc = 'A';
				fTrain = 'A';
			}
			else {
				firstSrc = 'B';
				fTrain = 'B';
			}
			firstArr = 0;
			newTrain = false;
		}

		while(
			((!Btrip.empty())&&(firstSrc == 'B'))&&(!newTrain)||
			((!Atrip.empty())&&(firstSrc == 'A'))&&(!newTrain)||
			((!Btrip.empty())&&(!Atrip.empty()))
			)
		{
			if(newTrain) {
				if(Atrip[0] < Btrip[0]) {
					firstSrc = 'A';
					fTrain = 'A';
				}
				else {
					firstSrc = 'B';
					fTrain = 'B';
				}
				firstArr = 0;
				newTrain = false;
			}			

			if(firstSrc == 'A') {
				for(int i = 0; i < Btrip.size(); ++i) {
					if(Atrip[firstArr].arr+time <= Btrip[i].dep) {

						Atrip.erase(Atrip.begin()+firstArr);
						firstSrc = 'B';
						firstArr = i;
						break;
					}
				}
				if(firstSrc != 'B') {
					Atrip.erase(Atrip.begin()+firstArr);
					++train[fTrain - 'A'];
					newTrain = true;
				}
			}
			else {
				for(int i = 0; i < Atrip.size(); ++i) {
					if(Btrip[firstArr].arr+time <= Atrip[i].dep) {

						Btrip.erase(Btrip.begin()+firstArr);
						firstSrc = 'A';
						firstArr = i;
						break;
					}
				}
				if(firstSrc != 'A') {
					Btrip.erase(Btrip.begin()+firstArr);
					++train[fTrain - 'A'];
					newTrain = true;
				}
			}
		}
		if(!Atrip.empty()) train[0] += Atrip.size();
		if(!Btrip.empty()) train[1] += Btrip.size();

		cout << "Case #" << count+1 << ": " << train[0] << " " << train[1] << endl;
	}
	return 0;
}