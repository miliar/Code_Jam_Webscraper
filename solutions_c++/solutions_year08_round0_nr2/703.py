#include<iostream>
#include<list>
using namespace std;

int gettime()
{
	char a[6];
	int time=0;
	cin>>a;
	time += (a[0]-'0')*10*60;
	time += (a[1]-'0')*60;
	time += (a[3]-'0')*10;
	time += (a[4]-'0');
	return time;
}

struct sch
{
	int timeA, timeD;
	bool AtoB;
};

bool operator < (sch& a, sch& b)
{
	return (a.timeD < b.timeD);
}

struct nooftrains
{
	int time;
	int n;
};

bool operator < (nooftrains& a, nooftrains& b)
{
	return (a.time < b.time);
}

list<sch> trains;
int noinA[1440];
int noinB[1440];

void additem(bool A, int time, bool arrive)
{
//	cout<<"A time arrive : "<<A<<' '<<time<<' '<<arrive<<endl;
	int* temp = A? noinA:noinB;
	int add = (arrive)?1:-1;
	for(int i=time; i<1440; i++)
		temp[i] += add;
}

int main()
{
	int N, N2, NA, NB, NA2, NB2, T, countA, countB, time;
	cin>>N;
	N2=N;
	while(N2--)
	{
		cin>>T>>NA>>NB;
		sch temp;
		NA2=NA; NB2=NB;
		temp.AtoB = true;
		countA = countB = 0;
		trains.clear();
		for(int j=0; j<1440; j++)
			noinA[j]=noinB[j]=0;
		while(NA2--)
		{
			temp.timeD = gettime();
			temp.timeA = gettime();
			trains.push_back(temp);
		}
		temp.AtoB=false;
		while(NB2--)
		{
			temp.timeD = gettime();
			temp.timeA = gettime();
			trains.push_back(temp);
		}
		trains.sort();
		for(list<sch>::iterator i = trains.begin(); i!=trains.end(); i++)
		{
			time = (*i).timeD;
			int sta = ((*i).AtoB)? noinA[time]: noinB[time];
			if(sta)
			{
				additem((*i).AtoB, time, false);
				additem(!(*i).AtoB, T + (*i).timeA, true);
			}
			else
			{
				(*i).AtoB ? countA++: countB++;
				additem(!(*i).AtoB, T + (*i).timeA, true);
			}
		}
		cout<<"Case #"<<N-N2<<": "<<countA<<' '<<countB;
		if(N2)
			cout<<endl;
	}
}
