// timetable.cpp : main project file.

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

string sum_time(string initial, int addition)
{
	int hour = (initial[0] - '0')*10 + (initial[1] - '0');
	int minute = (initial[3] - '0')*10 + (initial[4] - '0');
	minute += addition;
	if (minute >= 60) {
		minute -= 60;
		hour++;
	}
	string result;
	result += hour/10 + '0';
	result += hour%10 + '0'; 
	result += ':';
	result += minute/10 + '0';
	result += minute%10 + '0';
	return result;
}

int main()
{
    ifstream fin ("B-large.in");
	ofstream fout ("file.out");

	enum event_type {AREADY, BREADY, AOUT, BOUT};

	int N;
	fin >> N;
	for (int i = 0; i < N; ++i) {
		int T, NA, NB;
		vector < pair <string, enum event_type> > timetable;
		fin >> T >> NA >> NB;
		for (int j = 0; j < NA; ++j) {
			string departure, arrival;
			fin >> departure >> arrival;
			timetable.push_back(make_pair(departure, AOUT));
			timetable.push_back(make_pair(sum_time(arrival, T), BREADY));
		}
		for (int k = 0; k < NB; ++k) {
			string departure, arrival;
			fin >> departure >> arrival;
			timetable.push_back(make_pair(departure, BOUT));
			timetable.push_back(make_pair(sum_time(arrival, T), AREADY));
		}

		sort(timetable.begin(), timetable.end());

		int acount = 0, bcount = 0;
		int aavail = 0, bavail = 0;
		for (int l = 0; l < timetable.size(); ++l) {
			switch (timetable[l].second) {
				case AREADY: aavail++; break;
				case BREADY: bavail++; break;
				case AOUT: if (aavail) aavail--;
						   else acount++;
						   break;
				case BOUT: if (bavail) bavail--;
						   else bcount++;
						   break;
			}
		}

		fout << "Case #" << i + 1 << ": " << acount << " " << bcount << endl;
	}		

    return 0;
}
