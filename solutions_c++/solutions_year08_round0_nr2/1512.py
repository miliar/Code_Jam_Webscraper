#include<iostream>
#include<vector>
#include<stdlib.h>
#include<algorithm>
#define INVALID 999999
using namespace std;

struct entry
{
	int depart;
	int arrive;
public: 

	
	bool operator < (const entry & e) const
	{
		if(depart < e.depart)
			return true;
		if(depart == e.depart)
		{
			if(arrive <= e.arrive)
				return true;
			else
				return false;
		}
		else
			return false;
	}
	
};

int convertTime(string time)
{
	//cout << "string is " << time << endl;
	int result = 0;
	int hours = atoi(time.data());
	int min = atoi(time.substr(3).data());
	result = hours*60 + min;
	//cout << "result is " << result << endl;
	return result;
}


/*since it will always be sorted, just look for first non-used item*/
int getMin(vector<bool> & usedA)
{
	for(int i = 0; i < usedA.size();i++)
	{
		if(usedA[i] == false)
			return i;
	}
	return -1;
}


void simulate(vector<entry> & stationA, vector<entry> & stationB, vector<bool> & usedA, vector<bool> & usedB, int pos, bool sideA)
{
	//cout << "function called " ;
	if(sideA)
	{
		//cout << "at position " << pos << " on side A " << endl;
		usedA[pos] = true;
		for(int i = 0; i < stationB.size();i++)
		{
			if(usedB[i] == false && stationB[i].depart >= stationA[pos].arrive)
			{
				simulate(stationA, stationB, usedA, usedB, i, false);
				break;
			}
		}
	}
	else
	{
		//cout << "at position " << pos << " on side B " << endl;
		usedB[pos] = true;
		for(int i = 0; i < stationA.size();i++)
		{
			if(usedA[i] == false && stationA[i].depart >= stationB[pos].arrive)
			{
				simulate(stationA, stationB, usedA, usedB, i, true);
				break;
			}
		}
	}
}

int main()
{
	int testCases;
	cin >> testCases;
	for(int test = 0; test < testCases;test++)
	{
		
		int turnAroundTime;
		cin >> turnAroundTime;
		int numA, numB;
		cin >> numA >> numB;
		vector<entry> stationA, stationB;
		vector<bool> usedA;
		vector<bool> usedB;
		for(int i = 0; i < numA;i++)
		{
			string depart, arrive;
			cin >> depart >> arrive;
			int d,a;
			d = convertTime(depart);
			//cout << "d is " << d << endl;
			a = convertTime(arrive) + turnAroundTime;
			entry e;
			e.depart = d;
			e.arrive = a;
			stationA.push_back(e);
			usedA.push_back(false);
		}
		
		for(int i = 0; i < numB;i++)
		{
			string depart, arrive;
			cin >> depart >> arrive;
			int d,a;
			d = convertTime(depart);
			//cout << "d is " << d << endl;
			a = convertTime(arrive) + turnAroundTime;
			entry e;
			e.depart = d;
			e.arrive = a;
			stationB.push_back(e);
			usedB.push_back(false);
		}
		
		sort(stationA.begin(), stationA.end());
		sort(stationB.begin(), stationB.end());
		/*for(int i = 0; i < stationA.size();i++)
		{
			cout << stationA[i].depart << " " << stationA[i].arrive << endl;
		}
		cout << "now b time " << endl;
		for(int i = 0; i < stationB.size();i++)
		{
			cout << stationB[i].depart << " " << stationB[i].arrive << endl;
		}*/
		int aCount = 0;
		int bCount = 0;
		while(1)
		{
			//cout << "top of loop " << endl;
			int aMin = getMin(usedA);
			int bMin = getMin(usedB);
			if((bMin == -1 && aMin != -1) || (aMin != -1 && stationA[aMin] < stationB[bMin]) )
			{
				aCount++;
				simulate(stationA, stationB, usedA, usedB, aMin, true);
			
			}
			else if(bMin != -1)
			{
				//cout << "chose one from b " << endl;
				bCount++;
				simulate(stationA, stationB, usedA, usedB, bMin, false);
			
			}
			else
			{
				break;
			}
			
		}
		
		
		cout << "Case #" << test+1 << ": " << aCount << " " << bCount << endl;
			
	}
		
}























