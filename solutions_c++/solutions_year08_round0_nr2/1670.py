#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using std::cin;
using std::cout;
using std::pair;

typedef std::vector<std::pair<int, int> > Schedule;

bool SchedItemGreater(pair<int, int> & item1, pair<int, int> & item2)
{
   return item2.first > item1.first;
}

class CTimeToGoPreg
{
	int mReadyTime;
public:
	CTimeToGoPreg(int ready_time) : mReadyTime(ready_time) {}

	bool operator ()(pair<int, int> & time_slot)
	{
		return mReadyTime <= time_slot.first;
	}
};

void analyze_schedule(Schedule & scha, Schedule & schb, int & nTA, int & nTB)
{
	++nTA;
	int curtime = scha[0].second;
	scha.erase(scha.begin());

	for(;;)
	{
		Schedule::iterator fb = std::find_if(schb.begin(), schb.end(), CTimeToGoPreg(curtime));
		if (fb == schb.end())
			break;
		else
		{
			curtime = fb->second;
			schb.erase(fb);
		}
		Schedule::iterator fa = std::find_if(scha.begin(), scha.end(), CTimeToGoPreg(curtime));
		if (fa == scha.end())
			break;
		else
		{
			curtime = fa->second;
			scha.erase(fa);
		}
	}

	if (scha.empty())
		nTB += schb.size();
	else if (schb.empty())
		nTA += scha.size();
	else
	{
		if (scha[0].first <= schb[0].first)
			analyze_schedule(scha, schb, nTA, nTB);
		else
			analyze_schedule(schb, scha, nTB, nTA);
	}
}

int main()
{
	int nCases = 0;

	cin >> nCases;
	for (int icase = 0; icase < nCases; ++icase)
	{
		int turnt = 0;
		cin >> turnt;

		int nA = 0, nB = 0;
		cin >> nA;
		cin >> nB;

		Schedule scha;
		scha.reserve(nA);
		for (int ia = 0; ia < nA; ++ia)
		{
			int nHours1 = 0, nMinutes1 = 0;
			cin >> nHours1;
			cin.ignore(1);	// skip ':'
			cin >> nMinutes1;


			int nHours2 = 0, nMinutes2 = 0;
			cin >> nHours2;
			cin.ignore(1);	// skip ':'
			cin >> nMinutes2;

			scha.push_back(pair<int, int>(nHours1*60 + nMinutes1, nHours2*60 + nMinutes2 + turnt));
		}
		
		std::sort(scha.begin(), scha.end(), SchedItemGreater);

		Schedule schb;
		scha.reserve(nB);
		for (int ib = 0; ib < nB; ++ib)
		{
			int nHours1 = 0, nMinutes1 = 0;
			cin >> nHours1;
			cin.ignore(1);	// skip ':'
			cin >> nMinutes1;

			int nHours2 = 0, nMinutes2 = 0;
			cin >> nHours2;
			cin.ignore(1);	// skip ':'
			cin >> nMinutes2;

			schb.push_back(pair<int, int>(nHours1*60 + nMinutes1, nHours2*60 + nMinutes2 + turnt));
		}

		std::sort(schb.begin(), schb.end(), SchedItemGreater);

		int nTA = 0, nTB = 0;
		if (scha.size() == 0)
			nTB = schb.size();
		else if (schb.size() == 0)
			nTA = scha.size();
		else
		{
			if (scha[0].first <= schb[0].first)
				analyze_schedule(scha, schb, nTA, nTB);
			else
				analyze_schedule(schb, scha, nTB, nTA);
		}

		cout << "Case #" << (icase+1) << ": " << nTA << " " << nTB << std::endl;
	}

	return 0;
}