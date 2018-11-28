#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const string in_fname="B-large.in";
const string out_fname="B-out.txt";

void AssignFiles()
{
	freopen(in_fname.c_str(),"r",stdin);
	freopen(out_fname.c_str(),"w",stdout);
}

void CloseFiles()
{
	fclose(stdin);
	fclose(stdout);
}

struct Trip
{
	int TimeDep,TimeArr;	//the time in minutes
	Trip(int dep,int arr,bool ab): TimeDep(dep), TimeArr(arr), AB(ab) {};
	bool AB;

	bool operator<(Trip& r)
	{
		return TimeDep<r.TimeDep;
	}
};

vector<Trip> Trips;
vector<int> WaitA,WaitB;
int TurnTime;

int DecodeTime(string& s)
{
	int hh,mm;
	sscanf(s.c_str(),"%d:%d",&hh,&mm);

	return hh*60+mm;
}

int UpdateWait(vector<int>& v)
{
	int res=0;

	for(unsigned int i=0;i<v.size();i++)
	{
		v[i]--;
		if (v[i]==0)
		{
			res++;
			v.erase(v.begin()+i);
			i--;
		}
	}


	return res;
}

int main()
{
	AssignFiles();

	int NumCases;
	int TrainsAtA,TrainsAtB,ResA,ResB;
	cin>>NumCases;
	for(int Case=1;Case<=NumCases;Case++)
	{
		Trips.clear();
		WaitA.clear();
		WaitB.clear();

		string buf;
		string Time1,Time2;
		int countAB,countBA;
		cin>>TurnTime;
		cin>>countAB>>countBA;
		getline(cin,buf);
		for(int i=0;i<countAB;i++)
		{
			cin>>Time1>>Time2;
			Trips.push_back(Trip(DecodeTime(Time1),DecodeTime(Time2),true));
		}
		for(int i=0;i<countBA;i++)
		{
			cin>>Time1>>Time2;
			Trips.push_back(Trip(DecodeTime(Time1),DecodeTime(Time2),false));
		}
	
		TrainsAtA=TrainsAtB=ResA=ResB=0;
		sort(Trips.begin(),Trips.end());

		for(int time=0;time<=24*60;time++)
		{
			TrainsAtA+=UpdateWait(WaitA);
			TrainsAtB+=UpdateWait(WaitB);
			for(unsigned int i=0;i<Trips.size();i++)
			{
				if(Trips[i].TimeDep==time)
				{
					if(Trips[i].AB)
						TrainsAtA--; else
						TrainsAtB--;

					if(TrainsAtA<0)
					{
						TrainsAtA=0;
						ResA++;
					}
					if(TrainsAtB<0)
					{
						TrainsAtB=0;
						ResB++;
					}
				}
				if(Trips[i].TimeArr==time)
				{
					if(TurnTime>0)
					{
						if(Trips[i].AB)
							WaitB.push_back(TurnTime); else
							WaitA.push_back(TurnTime);
					} else
					{
						if(Trips[i].AB)
							TrainsAtB++; else
							TrainsAtA++;
					}
				}
			}
		}

		cout<<"Case #"<<Case<<": "<<ResA<<" "<<ResB<<"\n";
	}

	CloseFiles();
	return 0;
}
