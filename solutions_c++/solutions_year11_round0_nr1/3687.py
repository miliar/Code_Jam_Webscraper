#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int N = 0;
int * T = NULL;
vector<int> * O;
vector<int> * B;
vector<bool> * OActive;

void LoadData()
{
	fstream is("data.in", ios_base::in);
	is >> N;
	T = new int[N];
	B = new vector<int>[N];
	O = new vector<int>[N];
	OActive = new vector<bool>[N];

	for (int i = 0; i < N; ++i)
	{
		is >> T[i];
		for (int j = 0; j < T[i]; ++j)
		{
			char c = 0;
			int x = 0;
			is >> c >> x;
			if (c == 'B')
			{
				B[i].push_back(x);
				OActive[i].push_back(false);
			}
			else
			{
				O[i].push_back(x);
				OActive[i].push_back(true);
			}
		}
	}
}

#define sign(x) ((x == 0) ? 0 : ((x > 0) ? 1 : -1))

int SolveCase(const int & i)
{
	int lRes = 0;
	auto oit = O[i].begin();
	auto bit = B[i].begin();
	vector<bool>::iterator actit = OActive[i].begin();
	int t = 1;
	int op = 1;
	int bp = 1;

	//while (oit != O[i].end() && bit != B[i].end())
	while (actit != OActive[i].end())
	{
		if (*actit)
		{
			if (op == *oit) // pushed
			{
				++actit;
				++oit;
			}
			else
			{
				op += sign(*oit - op);
			}
			if (bit != B[i].end())
				bp += sign(*bit - bp);
		}
		else
		{
			if (bp == *bit) // pushed
			{
				++actit;
				++bit;
			}
			else
			{
				bp += sign(*bit - bp);
			}
			if (oit != O[i].end())
				op += sign(*oit - op);
		}
		++t;
	}
	lRes = t - 1;
	return lRes;
}

int main()
{
	LoadData();
	fstream os("data.out", ios_base::out);
	for (int i = 0; i < N; ++i)
		os << "Case #" << (i + 1) << ": " << SolveCase(i) << endl;
	os.close();
	return 0;
}

