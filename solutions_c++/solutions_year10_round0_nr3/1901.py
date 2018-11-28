#include <iostream>
#include <string>
#include <assert.h>
using namespace std;
int Rtimes;
long long kCapacity;
int NGroups;
long long groupMembers[1000];
long long EuroMade;

void ProcessCase()
{
	/*
	cari info kapan (di putaran ke berapa) group pertama duduk di paling depan kembali.
	*/
	EuroMade = 0;
	long long totalPassengers;
	int idx = 0;
	int firstidx;
	int r = 0;
	long long tempEuroMade;
	bool siklusBerulang = false;
	while (true)
	{
		firstidx = idx;
		totalPassengers = 0;
		while (true)
		{
			totalPassengers += groupMembers[idx];
			if (totalPassengers > kCapacity)
			{
				totalPassengers -= groupMembers[idx];
				break;	//full, run.
			}
			idx++;
			if (idx == NGroups)
				idx = 0;
			if (idx == firstidx)
				break;	//all people are in, run.
		}
		r++;
		//count Euro made
		EuroMade += totalPassengers;
		if (r == Rtimes)
			return;
		if (idx == 0)
		{
			//siklus akan berulang setiap r putaran
			siklusBerulang = true;
			tempEuroMade = EuroMade;
			break;
		}
	}
	int nSiklus;
	if (siklusBerulang)
	{
		EuroMade = 0;
		// hitung dg perkalian saja.
		nSiklus = Rtimes / r;
		EuroMade += (long long)tempEuroMade * (long long)nSiklus;
		// hitung sisa putaran
		int sisaPutaran = Rtimes % r;
		r = 0;
		while (true)
		{
			if (r == sisaPutaran)
				break;
			firstidx = idx;
			totalPassengers = 0;
			while (true)
			{
				totalPassengers += groupMembers[idx];
				if (totalPassengers > kCapacity)
				{
					totalPassengers -= groupMembers[idx];
					break;	//full, go round.
				}
				idx++;
				if (idx == NGroups)
					idx = 0;
				if (idx == firstidx)
					break;	//go round.
			}
			r++;
			//count Euro made
			EuroMade += totalPassengers;
			if (r == Rtimes)
				return;
		}
	}
	return;
}

int main()
{
#ifdef SN_INPUT_FILE
	string file1;
	string file2;
	//string file1 = "e:\\test_input - GCJ01.txt";
	//file1 = "e:\\test_input1b.txt";
	//file1 = "e:\\A-small-attempt0.in";
	file1 = "e:\\C-small-attempt1.in";
	//file1 = "e:\\C-small-attempt1 - Copy.in";
	FILE * ps;
	freopen_s(&ps, file1.c_str(), "rt", stdin);
	// uncomment for file output:
	//file2 = "e:\\A-small-attempt0.out";
	file2 = "e:\\C-small(siklusBerulang).out";
	freopen_s(&ps, file2.c_str(), "wt", stdout);
#endif
	int nCases;
	int caseNumber;
	cin >> nCases;

	for (int i=0; i<nCases; i++)
	{
		caseNumber = i+1;
		cin >> Rtimes;
		cin >> kCapacity;
		cin >> NGroups;
		for (int j=0; j<NGroups; j++)
		{
			cin >> groupMembers[j];
		}
		ProcessCase();
		cout << "Case #" << caseNumber << ": ";
		cout << EuroMade << endl;
	}
	//cout << "press any key to continue..." << endl; _getch();
	return 0;

}
