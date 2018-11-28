#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

const int ArrA=1;
const int ArrB=2;
const int DepA=3;
const int DepB=4;


void main()
{
	vector<pair<int,int> > schedule;
	int n,t,na,nb;
	int i,j;
	int curA,curB,trainA,trainB;
	int depH,depM,arrH,arrM;
	char c;

	ifstream ifs("B-large.in");
	ofstream ofs("B-large.out");

	ifs>>n;

	for(i=0; i<n; i++)
	{
		schedule.clear();
		curA=curB=trainA=trainB=0;

		ifs>>t;
		ifs>>na>>nb;
		for(j=0; j<na; j++)
		{
			ifs>>depH>>c>>depM;
			schedule.push_back(pair<int,int>(depH*60+depM,DepA));

			ifs>>arrH>>c>>arrM;
			schedule.push_back(pair<int,int>(arrH*60+arrM+t,ArrB));
		}
		for(j=0; j<nb; j++)
		{
			ifs>>depH>>c>>depM;
			schedule.push_back(pair<int,int>(depH*60+depM,DepB));

			ifs>>arrH>>c>>arrM;
			schedule.push_back(pair<int,int>(arrH*60+arrM+t,ArrA));
		}

		sort(schedule.begin(),schedule.end());

		for(j=0; j<schedule.size(); j++)
		{
			if(schedule[j].second==DepA)
				curA--;
			if(schedule[j].second==ArrA)
				curA++;
			if(schedule[j].second==DepB)
				curB--;
			if(schedule[j].second==ArrB)
				curB++;

			if(curA==-1)
			{
				trainA++;
				curA++;
			}
			if(curB==-1)
			{
				trainB++;
				curB++;
			}		
		}
		ofs<<"Case #"<<i+1<<": "<<trainA<<' '<<trainB<<endl;
	}
}
