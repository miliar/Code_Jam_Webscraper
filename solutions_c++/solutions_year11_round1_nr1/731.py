#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;

struct Test
{
	double N;
	int PG;
	int PD;
};

void Parse(int PD,int * Count2, int * Count5)
{
	for(int i = 0; i < 2; i++)
	{
		if(PD%2 == 0)
		{
			PD = PD/2;
			(*Count2)++;
		}
		if(PD%5 == 0)
		{
			PD = PD/5;
			(*Count5)++;
		}
	}
	return;
}
bool Check(double N,int PD,int PG)
{
	if(PG == 100 && PD < 100)
		return false;
	if(PG == 0 && PD > 0)
		return false;
	int Count2 = 0;
	int Count5 = 0;
	Parse(PD,&Count2,&Count5);
	if(Count2 == 2 && Count5 == 2)
		return true;
	else if(pow(2.0,(2 - Count2))*pow(5.0,(2 - Count5)) <= N)
		return true;
	return false;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large-ans.out");
	int T;
	std::vector<Test> AllTest;
	fin>>T;
	//AllTest.resize(T);
	for(int i = 0; i < T; i++)
	{
		AllTest.clear();
		AllTest.resize(1);
		fin>>AllTest[0].N;
		fin>>AllTest[0].PD;
		fin>>AllTest[0].PG;
		bool Flag = Check(AllTest[0].N,AllTest[0].PD,AllTest[0].PG);
		fout<<"Case #"<<i+1<<": ";
		if(Flag == true)
		{
			fout<<"Possible\n";
		}
		else
		{
			fout<<"Broken\n";
		}
	}
	fin.close();
	fout.close();
	return 0;
}
