#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define SZ 25*60

pair<int, int> Solve(vector<pair<int, int> > & ATable ,
 vector<pair<int, int> > & BTable)
{
	sort(ATable.begin(), ATable.end());
	sort(BTable.begin(), BTable.end());
	
	vector<int> tA(SZ, 0);
	vector<int> tB(SZ, 0);
	pair<int, int> res = make_pair(0, 0);
	
	size_t curA(0), curB(0);
	
	while (curA < ATable.size() || curB < BTable.size())
	{
		bool bA;
		if (curA == ATable.size())
			bA = false;
		else if (curB == BTable.size())
			bA = true;
		else  
		{
			bA = ATable[curA].first < BTable[curB].first;
		}
		
		if (bA)
		{
			if (tA[ATable[curA].first] == 0)
				res.first++;
			else
			{
				for (int mt = ATable[curA].first; mt <= SZ; ++mt)
					tA[mt]--;
			}
			for (int mt = ATable[curA].second; mt <= SZ; ++mt)
				tB[mt]++;
			curA++;
		}
		else
		{
			if (tB[BTable[curB].first] == 0)
				res.second++;
			else
			{
				for (int mt = BTable[curB].first; mt <= SZ; ++mt)
					tB[mt]--;
			}
			for (int mt = BTable[curB].second; mt <= SZ; ++mt)
				tA[mt]++;
			curB++;
		}
	} 
	return res;
}


int main()
{
	ifstream fin("/home/1.txt");
	ofstream fout("/home/2.txt");
	string s;
	getline(fin, s);
	int tests;
	istringstream is(s);
	is >> tests;
	for (int test = 0; test < tests; ++test)
	{
		getline(fin, s);
		int T;
		{
			istringstream is(s);
			is >> T;
		}
		
		int ACount, BCount;
		getline(fin, s);
		{
			istringstream is(s);
			is >> ACount >> BCount;
		}
		
		vector<pair<int, int> > ATable;
		 vector<pair<int, int> > BTable;
		
		for (int i = 0; i< ACount; i++)
		{
			getline(fin, s);
			int hS,mS,hF,mF;
			char c;
			istringstream is(s);
			is >> hS >> c >> mS >> hF >> c >> mF;
			ATable.push_back(make_pair(hS*60 + mS, hF*60 + mF + T));
		}
		for (int i = 0; i< BCount; i++)
		{
			getline(fin, s);
			int hS,mS,hF,mF; 
			char c;
			istringstream is(s);
			is >> hS >> c >> mS >> hF >> c >> mF;
			BTable.push_back(make_pair(hS*60 + mS, hF*60 + mF + T));
		}
		
		pair<int, int> hh = Solve(ATable, BTable);
		
		fout << "Case #" << test+1  << ": " << hh.first << " "<< hh.second  << endl;
	}
}
