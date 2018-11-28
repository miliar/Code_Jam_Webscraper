#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <queue>

using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");

bool my_less(const pair<int,pair<int,int>>& a, const pair<int,pair<int,int>>& b)
{
	return true;
}

int main()
{
	int C_TESTS = 0;
	fin >> C_TESTS;
	for (int test = 1; test<=C_TESTS; test++) {
		int T,NA,NB;
		fin >> T >> NA >> NB;
		priority_queue<
			pair<int,pair<int,int>>> aq,bq;
		for (int i=0; i<NA; i++) {
			int mins_s = 0, mins_f = 0;
			char tmp;
			fin >> tmp; mins_s += 10 * 60 * (int(tmp)-int('0'));
			fin >> tmp; mins_s += 60 * (int(tmp)-int('0'));
			fin >> tmp;
			fin >> tmp; mins_s += 10 * (int(tmp)-int('0'));
			fin >> tmp; mins_s += (int(tmp)-int('0'));
			
			fin >> tmp; mins_f += 10 * 60 * (int(tmp)-int('0'));
			fin >> tmp; mins_f += 60 * (int(tmp)-int('0'));
			fin >> tmp;
			fin >> tmp; mins_f += 10 * (int(tmp)-int('0'));
			fin >> tmp; mins_f += (int(tmp)-int('0'));
			aq.push(pair<int,pair<int,int>>(-mins_s,pair<int,int>(0,mins_f+T)));
		}
		for (int i=0; i<NB; i++) {
			int mins_s = 0, mins_f = 0;
			char tmp;
			fin >> tmp; mins_s += 10 * 60 * (int(tmp)-int('0'));
			fin >> tmp; mins_s += 60 * (int(tmp)-int('0'));
			fin >> tmp;
			fin >> tmp; mins_s += 10 * (int(tmp)-int('0'));
			fin >> tmp; mins_s += (int(tmp)-int('0'));
			
			fin >> tmp; mins_f += 10 * 60 * (int(tmp)-int('0'));
			fin >> tmp; mins_f += 60 * (int(tmp)-int('0'));
			fin >> tmp;
			fin >> tmp; mins_f += 10 * (int(tmp)-int('0'));
			fin >> tmp; mins_f += (int(tmp)-int('0'));
			bq.push(pair<int,pair<int,int>>(-mins_s,pair<int,int>(0,mins_f+T)));
		}
		int a = 0, b = 0;
		int free_a = 0, free_b = 0;
		while (!aq.empty() || !bq.empty()) {
			if (!aq.empty() && (bq.empty() || aq.top().first > bq.top().first)) {
				int st = -aq.top().first;
				int free = aq.top().second.first;
				int fn = aq.top().second.second;
				aq.pop();
				if (fn>=1440) 
					continue;
				if (free > 0)
					free_a += free;
				else {
					if (free_a > 0)
						free_a--;
					else
						a++;
					bq.push(pair<int,pair<int,int>>(-fn,pair<int,int>(1,0)));
				}
			} 
			else {
				int st = -bq.top().first;
				int free = bq.top().second.first;
				int fn = bq.top().second.second;
				bq.pop();
				if (fn>=1440) 
					continue;
				if (free > 0)
					free_b += free;
				else {
					if (free_b > 0)
						free_b--;
					else
						b++;
					aq.push(pair<int,pair<int,int>>(-fn,pair<int,int>(1,0)));
				}
			}
		}
		fout << "Case #" << test << ": " << a << ' ' << b << endl;
	}
	return 0;
}