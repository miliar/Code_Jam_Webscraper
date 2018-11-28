
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <iostream>
#include <algorithm>
#include <conio.h>
using namespace std;

int aUsed;
int bUsed;
int aLeft;
int bLeft;
list<int> listAB;
list<int> listBA;

vector<int> timePoint;

struct beginEnd
{
	int begin;
	int end;
};

beginEnd aList[100];
beginEnd bList[100];
int aIndex;
int bIndex;

int T;
int NA, NB;

int GetTime(string str)
{
	int hour, minute;
	char t;
	stringstream ss(str);
	ss >> hour >> t >> minute;
	return hour * 60 + minute;
}

void main()
{
	ifstream inf("B-large.in");
	ofstream outf("B-large.out");

	int i;
	int N;
	inf >> N;
	int time;
	for (time=0; time <N; time++)
	{
		timePoint.clear();
		listAB.clear();
		listBA.clear();

		inf >> T;
		inf >> NA >> NB;
		for (i=0; i<NA; i++)
		{
			string tStr;
			inf >> tStr;
			aList[i].begin = GetTime(tStr);
			inf >> tStr;
			aList[i].end = GetTime(tStr) + T;

			timePoint.push_back(aList[i].begin);
		}
		for (i=0; i<NB; i++)
		{
			string tStr;
			inf >> tStr;
			bList[i].begin = GetTime(tStr);
			inf >> tStr;
			bList[i].end = GetTime(tStr) + T;

			timePoint.push_back(bList[i].begin);
		}
		sort(timePoint.begin(), timePoint.end());
		vector<int>::iterator timeEnd;
		timeEnd = unique(timePoint.begin(), timePoint.end());

// 		vector<int>::iterator ttt;
// 		for (ttt=timePoint.begin(); ttt != timeEnd; ttt++)
// 		{
// 			cout << *ttt << "  ";
// 		}
// 		cout << endl;

		//ÅÅÐò
		int j;
		for (i=0; i<NA; i++)
		{
			for (j=i+1; j<NA; j++)
			{
				if (aList[i].begin > aList[j].begin)
				{
					beginEnd tbe;
					tbe = aList[i];
					aList[i] = aList[j];
					aList[j] = tbe;
				}
			}
		}
		for (i=0; i<NB; i++)
		{
			for (j=i+1; j<NB; j++)
			{
				if (bList[i].begin > bList[j].begin)
				{
					beginEnd tbe;
					tbe = bList[i];
					bList[i] = bList[j];
					bList[j] = tbe;
				}
			}
		}

		aUsed = 0;
		bUsed = 0;
		aLeft = 0;
		bLeft = 0;

		aIndex = 0;
		bIndex = 0;

		int nowTime = 0;
		vector<int>::iterator ti;
		for (ti=timePoint.begin(); ti!=timeEnd; ti++)
		{
			nowTime = *ti;
			list<int>::iterator li;
			li = listAB.begin();
			while (li != listAB.end())
			{
				if (*li <= nowTime)
				{
					bLeft++;
					listAB.erase(li++);
				}
				else
				{
					li++;
				}
			}
			li = listBA.begin();
			while (li != listBA.end())
			{
				if (*li <= nowTime)
				{
					aLeft++;
					listBA.erase(li++);
				}
				else
				{
					li++;
				}
			}

			while (aIndex < NA && aList[aIndex].begin == nowTime)
			{
				if (aLeft > 0)
				{
					aLeft--;
				}
				else
				{
					aUsed++;
				}
				listAB.push_back(aList[aIndex].end);
// 				cout << "*" << aIndex << endl;
				aIndex++;
			}
			while (bIndex < NB && bList[bIndex].begin == nowTime)
			{
				if (bLeft > 0)
				{
					bLeft--;
				}
				else
				{
					bUsed++;
				}
				listBA.push_back(bList[bIndex].end);
// 				cout << "&" << bIndex << endl;
				bIndex++;
			}
		}

// 		cout << "---------------" << endl;

		outf << "Case #" << time+1 << ": " << aUsed << " " << bUsed << endl;
	}

	inf.close();
	outf.close();
	getch();
}
