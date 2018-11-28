#include <iostream>
#include <string>
#include <fstream>

int N;
int Q;
int S;

const int MAXN = 20;
const int MAXS = 100;
const int MAXQ = 1000;

std::string sys[MAXS];

void ReadTestCase(std::ifstream& f)
{
	f>>S;
	std::getline(f,sys[0]);
	for (int s = 0; s < S; ++s )
	{
		std::getline(f,sys[s]);
	}
	f>>Q;
	std::string s;
	std::getline(f,s);
}

int FindSys(std::string szName)
{
	int i = 0;
	for (; i < S && sys[i] != szName; ++i);
	return i;
}


int ProcessTestCase(std::ifstream& f)
{	
	int nRes = 0;
	ReadTestCase(f);
	int nLeftMinuses = S;
	bool mmm[MAXS] = {false};
	for (int i = 0; i < Q; ++i)
	{
		std::string curQuery;
		std::getline(f,curQuery);
		int ind = FindSys(curQuery);
		if (!mmm[ind])
		{
			nLeftMinuses--;
		}
		if (!nLeftMinuses)
		{
			nRes++;
			nLeftMinuses = S-1;
			memset(mmm,0,sizeof(mmm));
		}
		mmm[ind] = true;
	}
	return nRes;
}


int main()
{
	std::ifstream f("./in.txt");
	std::ofstream fout("./out.txt");
	f>>N;
	for (int n = 0; n < N; ++n)
	{
		int res = ProcessTestCase(f);
		fout<<"Case #"<<n+1<<": "<<res<<std::endl;
	}
}
