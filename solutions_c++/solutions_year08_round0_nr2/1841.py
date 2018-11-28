// Code Jam 2.cpp : 定义控制台应用程序的入口点。
//


//#include <set>
#include <vector>
#include <fstream>
#include <assert.h>
#include <algorithm>
//#include "Functions.h"
class TrainTable;
typedef std::vector<TrainTable> MyContainer;
typedef MyContainer::iterator MyIt;

int TransformMinute(int Hour,int minute)
{
	return minute+Hour*60;
}

bool IsBeforeLeaving(int leavingTime,
					 int arrivingTime,
					 int turnaroundTime)
{
	return leavingTime>arrivingTime+turnaroundTime;
}
class TrainTable
{
public:
	int Arrival;
	int Leaving;
	int turnaround;
	char Tag;
public:
	explicit TrainTable(int a,int l, int t,char AB)
		:Arrival(a),Leaving(l),
		turnaround(t),Tag(AB){}
	~TrainTable()
	{

	}
	bool operator <(const TrainTable & rhs) const
	{
		if(Leaving<rhs.Leaving)
			return true;
		return (Leaving==rhs.Leaving)&&(Arrival>rhs.Arrival);
		//return false;
	}
	bool IsId(char c)
	{
		return c==Tag;
	}
};

struct Train{
	int Arrival;
	char where;
	explicit Train(int A,char w):Arrival(A),where(w){}
	explicit Train():Arrival(0),where(0){}
};

extern int cTrains[];
extern int cTrains2[];
extern bool* fUsedFlag;
extern size_t Container_Size;

void GetMinTrains(const MyContainer & c,
				  char where,
				  int ArrivalTime,const size_t Start)
{
	if((cTrains[0]+cTrains[1])
		<=
		(cTrains2[0]+cTrains2[1])
		)
	{
		return;
	}
	bool bNewTrain=true;
	static int cNumSet=1;
	for(size_t i=Start;i<Container_Size;++i)
	{
		if(fUsedFlag[i]==false)
		{
			if(ArrivalTime+c[0].turnaround<=c[i].Leaving
				&&where==c[i].Tag)
			{
				bNewTrain=false;
				fUsedFlag[i]=true;
				cNumSet++;
				GetMinTrains(c,where+((where-'A')?-1:1),c[i].Arrival,i+1);
				cNumSet--;
				fUsedFlag[i]=false;
				break;
			}

		}
	}
	if(bNewTrain)
	{
		for(size_t i=1;i<Container_Size;++i)
		{
			if(fUsedFlag[i]==false)
			{
				fUsedFlag[i]=true;
				int index=c[i].Tag-'A';
				cTrains2[index]++;
				cNumSet++;
				GetMinTrains(c,
					c[i].Tag+( (c[i].Tag-'A')?-1:1)
					,c[i].Arrival,i+1);
				cNumSet--;
				cTrains2[index]--;
				fUsedFlag[i]=false;
				return;
			}
		}
	}
	if(cNumSet==Container_Size)
	{
		if((cTrains[0]+cTrains[1])
		>
		(cTrains2[0]+cTrains2[1])
		)
		{
			cTrains[0]=cTrains2[0];cTrains[1]=cTrains2[1];
		}
		return;
	}
}

int cTrains[2];
int cTrains2[2];
bool* fUsedFlag=NULL;
size_t Container_Size;

int main(int argc, char* argv[])
{
	std::ifstream infile("B-input.in");
	assert(!infile==false);
	std::ofstream outfile("output");
	assert(!outfile==false);
	int cLoopTime;
	infile>>cLoopTime;
	assert(!infile==false);


	for(int f=0;f!=cLoopTime;++f)
	{
		int TurnAroundTime;
		infile>>TurnAroundTime;
		assert(!infile==false);
		int cTrainAB,cTrainBA;
		infile>>cTrainAB;
		assert(!infile==false);
		infile>>cTrainBA;

		MyContainer TrainTableSet;
		for(int j=0;j!=cTrainAB;++j)
		{
			int HH,MM,iTimeLeaving,iTimeArrival;
			infile>>HH;
			assert(!infile==false);
			infile.ignore();
			infile>>MM;
			assert(!infile==false);
			iTimeLeaving=TransformMinute(HH,MM);
			infile>>HH;
			assert(!infile==false);
			infile.ignore();
			infile>>MM;
			assert(!infile==false);

			iTimeArrival=TransformMinute(HH,MM);
			TrainTableSet.push_back(TrainTable(iTimeArrival,iTimeLeaving,TurnAroundTime,'A'));
		}

		for(int j=0;j!=cTrainBA;++j)
		{
			int HH,MM,iTimeLeaving,iTimeArrival;
			infile>>HH;
			assert(!infile==false);
			infile.ignore();
			infile>>MM;
			assert(!infile==false);
			iTimeLeaving=TransformMinute(HH,MM);
			infile>>HH;
			assert(!infile==false);
			infile.ignore();
			infile>>MM;
			assert(!infile==false);

			iTimeArrival=TransformMinute(HH,MM);
			TrainTableSet.push_back(TrainTable(iTimeArrival,iTimeLeaving,TurnAroundTime,'B'));
		}
		
		typedef std::vector<Train> MyVec;
		MyVec trains;
		

		fUsedFlag=(bool*) calloc(sizeof(bool),TrainTableSet.size());
		memset(cTrains2,0,sizeof cTrains2);
		cTrains[0]=cTrainAB;cTrains[1]=cTrainBA;
		std::sort(TrainTableSet.begin(),TrainTableSet.end());
		Container_Size=TrainTableSet.size();
		assert(fUsedFlag);
		cTrains2[TrainTableSet[0].Tag-'A']++;
		GetMinTrains(TrainTableSet,TrainTableSet[0].Tag+
			((TrainTableSet[0].Tag-'A')?-1:1),TrainTableSet[0].Arrival,1);


		free(fUsedFlag);

		outfile<<"Case #"<<f+1<<": "<<cTrains[0]<<" "
			<<cTrains[1]<<"\n";
	}
	return 0;
}

