#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;

struct TData {
	int startTime;
	int endTime;
	bool isFromA;
};

bool comp(const TData& d1, const TData& d2) {
	return d1.startTime < d2.startTime;
}

int s2i(const string& s) {
	return ((s[0] - '0')*10 + (s[1] - '0'))*60 + (s[3] - '0')*10 + (s[4] - '0'); 
}

int main() {
	
	ifstream fin("B-small.in");
	ofstream fout("B-small.out");
	
	int n;
	fin >> n;	
	for (int i = 0; i < n; ++i) {
		int dt, na, nb;
		fin >> dt;		
		fin >> na >> nb;
		int resa = 0; int resb = 0;
		
		priority_queue<int, vector<int>, greater<int> > qA;
		priority_queue<int, vector<int>, greater<int> > qB;
		vector <TData> data;
		for (int j = 0; j < na; ++j) {
			string s1, s2; TData d;
			fin >> s1 >> s2;
			d.startTime = s2i(s1);
			d.endTime  = s2i(s2);
			d.isFromA = true;	
			data.push_back(d);
		}
		
		for (int j = 0; j < nb; ++j) {
			string s1, s2; TData d;
			fin >> s1 >> s2;
			d.startTime = s2i(s1);
			d.endTime   = s2i(s2);
			d.isFromA   = false;
			data.push_back(d);
		}
		
		sort(data.begin(), data.end(), comp);		
		
		for (int j = 0; j < (int)data.size(); ++j) {
			if (data[j].isFromA) {
				if (qA.empty() || qA.top() > data[j].startTime) {
					//add new train to a;
					resa++;					
				} else {
					//go with existing train 
					qA.pop();					
				}
				qB.push(data[j].endTime + dt);
			} else {
				if (qB.empty() || qB.top() > data[j].startTime) {
					//add new train to b;
					resb++;					
				} else {
					//go with existing train 
					qB.pop();					
				}
				qA.push(data[j].endTime + dt);
			}
		}		
		fout << "Case #" << i + 1 << ": " << resa << " " << resb << endl;  
	}	
	
	fout.close();
	fin.close();
	return 0;
}