#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <numeric>

using namespace std;

struct timetable
{
	int arr, dep;
	char station;
	bool operator < (timetable t)
	{
		if (dep == t.dep) return arr < t.arr;
		return dep < t.dep;
	}
};

int main()
{
	ifstream fin("b.in");
	ofstream fout("b.out");

	int T, N;

	fin >> N;

	for(T = 1; T <= N; ++T)
	{
		int t, na, nb, i, j;
		fin >> t >> na >> nb;

		fout << "Case #" << T << ": ";
		
		vector <timetable> schedule;

		for(i = 0; i < na; ++i)
		{
			timetable x;
			string temp;
			fin >> temp;
			x.dep = ((temp[0] - '0') * 10 + (temp[1] - '0')) * 60 + ((temp[3] - '0') * 10 + (temp[4] - '0'));
			fin >> temp;
			x.arr = ((temp[0] - '0') * 10 + (temp[1] - '0')) * 60 + ((temp[3] - '0') * 10 + (temp[4] - '0'));
			x.arr += t;
			x.station = 'A';
			schedule.push_back(x);
		}

		for(i = 0; i < nb; ++i)
		{
			timetable x;
			string temp;
			fin >> temp;
			x.dep = ((temp[0] - '0') * 10 + (temp[1] - '0')) * 60 + ((temp[3] - '0') * 10 + (temp[4] - '0'));
			fin >> temp;
			x.arr = ((temp[0] - '0') * 10 + (temp[1] - '0')) * 60 + ((temp[3] - '0') * 10 + (temp[4] - '0'));
			x.arr += t;
			x.station = 'B';
			schedule.push_back(x);
		}

		if (na == 0 || nb == 0)
		{
			fout << na << " " << nb << endl;
			continue;
		}

		sort(schedule.begin(), schedule.end());

		vector <int> sa, sb;
		//set <int>::iterator si;
		int resa = 0, resb = 0;

		for(i = 0; i < na + nb; ++i)
		{
			if (schedule[i].station == 'A')
			{
				bool sw = false;
				for(j = 0; j < sa.size(); ++j)
				{
					if (sa[j] <= schedule[i].dep)
					{
						sw  = true;
						break;
					}
				}
				if (sw) sa.erase(sa.begin() + j);
				else ++resa;
				sb.push_back(schedule[i].arr);
			}
			else if (schedule[i].station == 'B')
			{
				bool sw = false;
				for(j = 0; j < sb.size(); ++j)
				{
					if (sb[j] <= schedule[i].dep)
					{
						sw  = true;
						break;
					}
				}
				if (sw) sb.erase(sb.begin() + j);
				else ++resb;
				sa.push_back(schedule[i].arr);
			}
		}

		fout << resa << " " << resb << endl;
	}
	return 0;
}