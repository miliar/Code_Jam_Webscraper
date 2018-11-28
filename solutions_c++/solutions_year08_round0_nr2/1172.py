#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <stdio.h>
using namespace std;
struct T_Schedule {
	int dep;
	int arr;
	bool bAtoB;
	
};

int nAB,nBA,T;
int nResAB,nResBA;
vector<T_Schedule> vItem;

bool compArr(const T_Schedule &a,const T_Schedule &b) {return a.arr<b.arr;}
bool compDep(const T_Schedule &a,const T_Schedule &b) {return a.dep<b.dep;}


struct T_Train {
	int nTimeAvailable;
	bool bInitialPos;
	bool bCurrentPos;
};

vector<T_Train> vTrains;	// time until which train is occupied

void solve()
{
	nResAB=0;
	nResBA=0;
	vTrains.clear();
	sort (vItem.begin(),vItem.end(),compDep);
	
	int i,j;
	for (i=0;i<vItem.size();i++)
	{	// parsing schedule items
		int nDep=vItem[i].dep;
		int nArr=vItem[i].arr;
		bool bAtoB=vItem[i].bAtoB;

		bool bTrainExists=false;
		for (j=0;j<vTrains.size();j++)
		{
			if (vTrains[j].bCurrentPos==bAtoB && vTrains[j].nTimeAvailable<=nDep)
			{
				vTrains[j].bCurrentPos=!vTrains[j].bCurrentPos;
				vTrains[j].nTimeAvailable=nArr;
				bTrainExists=true;
				break;
			}

		} //j
		if (!bTrainExists)
		{
			T_Train newTrain;
			newTrain.bInitialPos=bAtoB;
			newTrain.bCurrentPos=!bAtoB;
			newTrain.nTimeAvailable=nArr;
			vTrains.push_back(newTrain);
		}

	}

	for (i=0;i<vTrains.size();i++)
	{
		if (vTrains[i].bInitialPos==true)
			nResAB++;
		else
			nResBA++;
	}

}


int main()
{
	int i,j,k;
	int num_cases;
	fstream fin,fout;
//	fin.open ("B-small.txt", fstream::in);

	fin.open ("B-large.in", fstream::in);
	fout.open("B-large.out",fstream::out);

	fin >>num_cases;


	for (i=0;i<num_cases;i++)
	{
		vItem.clear();

		fin >>T;
		fin >>nAB>>nBA;
		string sdep, sarr;
		
		for (j=0;j<nAB;j++)
		{
			fin >>sdep>>sarr;
			T_Schedule s;
			s.dep=(60*atoi(sdep.substr(0,2).c_str()))+atoi(sdep.substr(3,2).c_str());
			s.arr=(60*atoi(sarr.substr(0,2).c_str()))+atoi(sarr.substr(3,2).c_str())+T;
			s.bAtoB=true;
			vItem.push_back(s);
		}
		for (j=0;j<nBA;j++)
		{
			fin >>sdep>>sarr;
			T_Schedule s;
			s.dep=(60*atoi(sdep.substr(0,2).c_str()))+atoi(sdep.substr(3,2).c_str());
			s.arr=(60*atoi(sarr.substr(0,2).c_str()))+atoi(sarr.substr(3,2).c_str())+T;
			s.bAtoB=false;
			vItem.push_back(s);
		}
		//Solve
		solve();
	//	if (nResBA<0) nResBA=0;
	//	if (nResAB<0) nResAB=0;

		fout << "Case #"<<i+1<<": "<<nResAB<<" "<<nResBA<<endl;		

	}
}