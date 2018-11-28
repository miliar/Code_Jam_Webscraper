#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <fstream>
#include <map>
#include <set>
using namespace std;

struct Inf
{
	Inf(int tim, char station): tim(tim), station(station){}
	int tim;
	int station;

	bool operator < (const Inf& other) const { return tim < other.tim;	}
};

int readtime()
{
	int hours;
	int mins;
	char c;
	
	cin >> hours;
	cin >> c;
	cin >> mins;

	if (c != ':')
	{
		cout << "AAAAAAAAAAAAA!!!!!!!!!!!!!!";
		exit(1);
	}

	return hours*60+mins;
}

int main()
{
	int N;
	cin >> N;

	for(int i = 1; i <= N; ++i)
	{
		int T;
		cin >> T;
		int NA;
		cin >> NA;
		int NB;
		cin >> NB;

		vector<Inf> deps;
		vector<Inf> arrs;

		for(int j = 0; j < NA; ++ j)
		{
			int dep = readtime();
			int arr = readtime()+T;
			
			deps.push_back(Inf(dep, 'A'));
			arrs.push_back(Inf(arr, 'B'));
		}

		for(int j = 0; j < NB; ++ j)
		{
			int dep = readtime();
			int arr = readtime()+T;
			
			deps.push_back(Inf(dep, 'B'));
			arrs.push_back(Inf(arr, 'A'));
		}

		int waitA = 0;
		int waitB = 0;
		int resA = 0;
		int resB = 0;

		sort(arrs.begin(), arrs.end());
		sort(deps.begin(), deps.end());

		vector<Inf>::iterator depIter = deps.begin();
		vector<Inf>::iterator arrIter = arrs.begin();

		while(depIter != deps.end())
		{
			while(arrIter->tim <= depIter->tim)
			{
				if (arrIter->station == 'A')
					++waitA;
				else
					++waitB;

				++arrIter;
			}

			if (depIter->station == 'A')
			{
				if (waitA == 0)
					++resA;
				else
					--waitA;
			}
			else
			{
				if (waitB == 0)
					++resB;
				else
					--waitB;
			}

			++depIter;
		}

		cout << "Case #" << i << ": " << resA << ' ' << resB << endl;

	}

	return 0;
}