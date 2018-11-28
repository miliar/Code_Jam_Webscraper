#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <algorithm>

using namespace std;

int Smallest=INT_MAX, Largest = 0;

struct Trip
{
	int SM, SH, EM, EH;
	bool StartAtA;
	int Start, End;
	Trip(int _SH, int _SM, int _EH, int _EM, bool A):SH(_SH), SM(_SM), EH(_EH), EM(_EM), StartAtA(A)
	{
		Start = SH * 60 + SM;
		End = EH * 60 + EM;

		if (End <= Start)
		{
			swap(End,Start);
			swap(SH, EH);
			swap(SM, EM);
			cout <<"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"<<endl;
		}
		Largest >?= End;
		Smallest <?= Start;
	}

	void Display()
	{
		if (StartAtA)
			cout << SH<<":"<<SM<<" ---> "<< EH << ":"<<EM<<endl;
		else
			cout << EH<<":"<<EM<<" <--- "<< SH << ":"<<SM<<endl;
	}
};

bool operator < (Trip O, Trip T)
{
	if (O.End == T.End)
		return (O.Start < T.Start);
	return (O.End < T.End);
}

deque <Trip> Trips;
vector <int> TrainsA;
vector <int> TrainsB;

void DisplayTrips()
{
	for (int i=0; i < Trips.size(); ++i)
	{
		Trips[i].Display();
	}
}

void TakeTrainA(int Time)
{
	TrainsA[Time]--;

	if (TrainsA[Time] < 0)
			cout <<"*********************WRONG************************"<<Time<<endl;
}

void TakeTrainB(int Time)
{
	TrainsB[Time]--;

	if (TrainsB[Time] < 0)
		cout <<"*********************WRONG************************"<<Time<<endl;
}


void PutTrainA(int Time)
{
	TrainsA[Time]++;
}


void PutTrainB(int Time)
{
	TrainsB[Time]++;
}

int TrainAvailableA(int Time)
{
	for (int i= Time; i >= 0; --i)
	{
		if (TrainsA[i] > 0)
			return i;
	}
	return -1;
}

int TrainAvailableB(int Time)
{
	for (int i= Time; i >= 0; --i)
	{
		if (TrainsB[i] > 0)
			return i;
	}
	return -1;
}


void ShowTrains()
{
	for (int i=Smallest; i < Largest; ++i)
	{
		cout << i/60 <<":" << i%60<<"    "<<TrainsA[i] << "\t"<<TrainsB[i]<<endl;
	}
	cout << "===================================="<<endl;
}

int AddedA, AddedB;
void Solve(int T)
{
	//int Rem = Trips.size();
	sort (Trips.begin(), Trips.end());
	DisplayTrips();

	AddedA = 0;
	AddedB = 0;

	Smallest=INT_MAX;
	Largest = 0;

	while (!Trips.empty())
	{
		Trip Cur = Trips.front();
		Trips.pop_front();
		if (Cur.StartAtA)
		{
			int Train = TrainAvailableA(Cur.Start);
			if (Train >= 0)
			{
				// Train ready
				TakeTrainA(Train);
			}
			else
			{
				AddedA++;
			}
			PutTrainB(Cur.End+T);
		}
		else
		{
			int Train = TrainAvailableB(Cur.Start);
			if (Train >= 0)
			{
				// Train ready
				TakeTrainB(Train);
			}
			else
			{
				AddedB++;
			}
			PutTrainA(Cur.End+T);
		}

		//ShowTrains();
	}

}


int main()
{
	ifstream cin ("B.in");
	ofstream fout ("B.out");
	char c;
	int nCases, NA, NB, Turn;
	cin >> nCases;

	for (int iCase = 1; iCase <= nCases; ++iCase)
	{
		Trips.clear();
		TrainsA.clear();
		TrainsB.clear();

		TrainsA.resize(1800, 0);
		TrainsB.resize(1800, 0);

		cin >> Turn >> NA >> NB;

		for (int i=0; i < NA;++i)
		{
			int SH, SM, EH, EM;
			cin >> SH>>c>>SM >> EH >>c>> EM;
			Trip Temp(SH, SM, EH, EM, true);
			Trips.push_back(Temp);
		}
		for (int i=0; i < NB;++i)
		{
			int SH, SM, EH, EM;
			cin >> SH>>c>>SM >> EH >>c>> EM;
			Trip Temp(SH, SM, EH, EM, false);
			Trips.push_back(Temp);
		}

		cout << "Case #"<<iCase<<": "<<endl;
		cout << Turn << endl;
		Solve(Turn);
		cout <<AddedA<< " "<<AddedB<<endl;

		fout << "Case #"<<iCase<<": "<<AddedA<< " "<<AddedB<<endl;
	}
	return 0;
}
