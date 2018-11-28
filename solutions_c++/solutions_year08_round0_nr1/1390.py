//
// Round 0, Task A.
//


#include <iostream>
#include <fstream>


using namespace std;


void solve();

int main()
{
	ifstream inf("in.txt");
	cin.rdbuf(inf.rdbuf());
	ofstream ouf("out.txt");
	cout.rdbuf(ouf.rdbuf());

	solve();

	return 0;
}


int find(const char engines[][128], const char engine[])
{
	int i = 0;
	while (strcmp(engine, engines[i]))
		++i;
	return i;
}


void solve()
{
	static char engines[128][128];
	static bool QueriedEngines[128];
	static char engine[128];

	int N;
	cin >> N;
	for (int n = 1; n <= N; ++n)
	{

		int S;
		cin >> S;
		cin.getline(engine, 128);		// How do I get rid of this?
		for (int s = 0; s < S; ++s)
			cin.getline(engines[s], 128);
		
		int Q;
		cin >> Q;
		cin.getline(engine, 128);		// How do I get rid of this?
		int rez = 0;
		int nQueried = 0;
		memset(QueriedEngines, 0, sizeof(QueriedEngines));
		for (int q = 0; q < Q; ++q)
		{
			cin.getline(engine, 128);
			int index = find(engines, engine);
			if (!QueriedEngines[index])
			{
				QueriedEngines[index] = true;
				++nQueried;
			}
			if (nQueried == S)
			{
				// do switch and reset
				memset(QueriedEngines, 0, sizeof(QueriedEngines));
				QueriedEngines[index] = true;
				nQueried = 1;
				++rez;
			}
		}

		cout << "Case #" << n << ": " << rez << endl;
	}
}