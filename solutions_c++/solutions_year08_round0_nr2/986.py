#include<fstream>
#include<vector>
#include<stdio.h>
#include<map>
#include<sstream>

using namespace std;

int main(int argc, char* argv[])
{
	if(argc < 2)return 0;
	ifstream is(argv[1]);
	ofstream os("B.out");
	int n;
	is>>n;
	for(int casenum = 0; casenum < n; ++casenum)
	{
		int t,na,nb;
		is>>t>>na>>nb;
		char temp[6];
		int hour,minute;
		map<int,int> timetableA;
		map<int,int> timetableB;
		for(int ia = 0; ia < na; ++ia)
		{
			is>>temp;
			temp[2] = 0;
			temp[5] = 0;
			stringstream ss;
			ss<<temp<<" "<<temp+3;
			ss>>hour>>minute;
			ss.clear();
			if(timetableA.find(hour*60 + minute) == timetableA.end())
			{
				timetableA[hour*60 + minute] = -1;
			}
			else
			{
				timetableA[hour*60 + minute] += -1;
			}
			
			is>>temp;
			temp[2] = 0;
			temp[5] = 0;
			ss<<temp<<" "<<temp+3;
			ss>>hour>>minute;

			if(timetableB.find(hour*60 + minute + t) == timetableB.end())
			{
				timetableB[hour*60 + minute + t] = 1;
			}
			else
			{
				timetableB[hour*60 + minute + t] += 1;
			}
		}
		for(int ib = 0; ib < nb; ++ib)
		{
			is>>temp;
			temp[2] = 0;
			temp[5] = 0;
			stringstream ss;
			ss<<temp<<" "<<temp+3;
			ss>>hour>>minute;
			ss.clear();
			if(timetableB.find(hour*60 + minute) == timetableB.end())
			{
				timetableB[hour*60 + minute] = -1;
			}
			else
			{
				timetableB[hour*60 + minute] += -1;
			}
			is>>temp;
			temp[2] = 0;
			temp[5] = 0;
			ss<<temp<<" "<<temp+3;
			ss>>hour>>minute;

			if(timetableA.find(hour*60 + minute + t) == timetableA.end())
			{
				timetableA[hour*60 + minute + t] = 1;
			}
			else
			{
				timetableA[hour*60 + minute + t] += 1;
			}
		}

		int sumA = 0;
		int sumB = 0;
		int current = 0;
		for(map<int,int>::iterator it = timetableA.begin(); it != timetableA.end(); ++it)
		{
			if(it->second < 0)
			{
				if(current == 0) sumA -= it->second;
				else if(current > -it->second)
				{
					current += it->second;
				}
				else
				{
					sumA -= (it->second + current);
					current = 0;
				}
			}
			else
			{
				current += it->second;
			}
		}
		current = 0;
		for(map<int,int>::iterator it = timetableB.begin(); it != timetableB.end(); ++it)
		{
			if(it->second < 0)
			{
				if(current == 0) sumB -= it->second;
				else if(current > -it->second)
				{
					current += it->second;
				}
				else
				{
					sumB -= (it->second + current);
					current = 0;
				}
			}
			else
			{
				current += it->second;
			}
		}
		os<<"Case #"<<casenum + 1<<": "<<sumA<<" "<<sumB<<endl;
	}
	return 0;
}
