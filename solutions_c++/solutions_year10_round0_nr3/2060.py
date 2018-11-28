#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

class CrisPoint
{
public:
	long long SumByNow;
	int cp;
	CrisPoint(long long s,int p)
	{
		SumByNow = s;
		cp = p;
	}
};

bool Check(vector<CrisPoint> & cps,int np,int & start,int & end)
{
	for(int i = 0;i<cps.size();++i)
	{
		if(cps[i].cp == np)
		{
			start = i;
			end = cps.size()-1;
			for(int j = start+1;j<=end;++j)
			{
				cps[j].SumByNow -= cps[start].SumByNow;
			}
			return true;
		}
	}
	return false;
}

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	int N;
	fin>>N;
	for(int NOW = 1;NOW<=N;++NOW)
	{
		long long TimeOfRun;
		long long OneTimeLimit;
		int GroupNum;
		fin>>TimeOfRun;
		fin>>OneTimeLimit;
		fin>>GroupNum;
		long long * Group = new long long[GroupNum];
		long long AddSum = 0;
		for(int i = 0;i<GroupNum;++i)
		{
			fin>>Group[i];
		}

		vector<CrisPoint> CrisPoints;

		long long Sum = 0;
		int NowPoint = 0;
		int start;
		int end;
		while(TimeOfRun && !Check(CrisPoints,NowPoint,start,end))
		{
			long long TempSum =0;
			CrisPoint TempPoint(Sum,NowPoint);
			CrisPoints.push_back(TempPoint);
			int i = 0;
			while(TempSum+Group[NowPoint]<=OneTimeLimit && i<GroupNum)
			{
				++i;
				TempSum+=Group[NowPoint];
				NowPoint = (NowPoint+1)%GroupNum;
			}

			Sum+=TempSum;
			--TimeOfRun;
		}

		if(TimeOfRun)
		{
			AddSum = Sum - CrisPoints[start].SumByNow;
			Sum += AddSum*(TimeOfRun/(end-start+1));
			int kkk= TimeOfRun%(end-start+1);
			if(kkk)
			{
				Sum += CrisPoints[kkk+start].SumByNow;
			}
		}

		fout<<"Case #";
		fout<<NOW;
		fout<<": ";
		fout<<Sum<<endl;
	}
	return 0;
}