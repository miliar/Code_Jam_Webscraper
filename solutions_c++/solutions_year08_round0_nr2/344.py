#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int,int> PII;

int main() {
	int N, nn = 0, TA, NA, NB, h, m;
	char time[10];
	cin >> N;
	vector<pair<PII,int> > trA, trB;
	while(nn < N) {
		cin >> TA >> NA >> NB;
		trA.clear(), trB.clear();
		for(int i = 0; i < NA; i++) {
			cin >> time;
			time[2] = 0;
			h = atoi(time);
			m = atoi(time + 3);
			trA.push_back(make_pair(make_pair(h,m),1));

			cin >> time;
			time[2] = 0;
			h = atoi(time);
			m = atoi(time + 3);
			m += TA;
			h += (m / 60);
			m %= 60;
			trB.push_back(make_pair(make_pair(h,m),-1));
		}
		for(int i = 0; i < NB; i++) {
			cin >> time;
			time[2] = 0;
			h = atoi(time);
			m = atoi(time + 3);
			trB.push_back(make_pair(make_pair(h,m),1));

			cin >> time;
			time[2] = 0;
			h = atoi(time);
			m = atoi(time + 3);
			m += TA;
			h += (m / 60);
			m %= 60;
			trA.push_back(make_pair(make_pair(h,m),-1));
		}
		sort(trA.begin(), trA.end());
		sort(trB.begin(), trB.end());
		int numA = 0, numB = 0;
		int sumA = 0, sumB = 0;
		for(vector<pair<PII,int> >::iterator it =  trA.begin(); it != trA.end(); it++) {
			sumA += it->second;
			numA = (numA < sumA)? sumA : numA;
		}
		for(vector<pair<PII,int> >::iterator it =  trB.begin(); it != trB.end(); it++) {
			sumB += it->second;
			numB = (numB < sumB)? sumB : numB;
		}
		cout << "Case #" << ++nn << ": " << numA << " " << numB << endl;
	}
	return 0;
}
