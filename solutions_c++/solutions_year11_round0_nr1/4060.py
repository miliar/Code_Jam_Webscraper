#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <math.h>

using namespace std;

vector<pair<char,int>> sequence;//desired

int OCurrentPos = 1;
int BCurrentPos = 1;

int PushButton(int& current,int i)
{
	int numOfSec = 1;
	int desired = sequence[i].second;

	numOfSec += abs(desired-current);
	current = desired;
	return numOfSec;
}
void Update(int i,int & current , int numofSec )
{
	int desired = sequence[i].second;
	if (current == desired)
	{
		return;
	}
	if (current != desired)
	{
		int diff = abs(desired - current);
		if (numofSec > diff)
		{
			current = desired;
		}
		else
		{
			if (current > desired)
			{
				current -= numofSec;
			}
			else
				current += numofSec;
		}
	}
}
void ProcessSequence(int num, ofstream& out)
{
	int numOfSec = 0;
	for (int i = 0; i< sequence.size();i++)
	{
		int consume;
		if (sequence[i].first == 'O')
		{
			consume = PushButton(OCurrentPos,i);
			if (i < sequence.size()-1)//update the second
			{
				for (int j = i+1;j<sequence.size(); j++)
				{
					if (sequence[j].first == 'B')
					{
						Update(j,BCurrentPos,consume);
						break;
					}
				}
			}
		}
		else
		{
			consume = PushButton(BCurrentPos,i);
			if (i < sequence.size()-1)//update the second
			{
				for (int j = i+1;j<sequence.size(); j++)
				{
					if (sequence[j].first == 'O')
					{
						Update(j,OCurrentPos,consume);
						break;
					}
				}
			}
		}
		numOfSec += consume;
	}
	out<<"Case #"<<num+1<<": "<<numOfSec<<endl;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream out("outfile.out");

	int numOfTest;
	fin>>numOfTest;

	for (int i =0 ; i < numOfTest; i++)
	{
		int seq;
		fin>>seq;
		sequence.clear();
		OCurrentPos = 1;
		BCurrentPos = 1;
		for (int k = 0 ; k < seq; k++)
		{
			int button;
			char chr;
			fin>>chr;
			fin>>button;
			sequence.push_back(make_pair(chr,button));
		}

		ProcessSequence(i,out);

	}

	return 0;
}