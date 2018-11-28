//
// Round 0, Task B.
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


void GetData(int t0[], int t1[], int n, int T)
{
	for (int i = 0; i < n; ++i)
	{
		int h, m;
		char c;
		cin >> h >> c >> m;
		t0[i] = h*60 + m;
		cin >> h >> c >> m;
		t1[i] = h*60 + m + T;
	}
}


void sort(int arr[], int n)
{
	for (int i = 0; i < n - 1; ++i)
	{
		int min = arr[i], imin = i;
		for (int j = i + 1; j < n; ++j)
			if (arr[j] < min)
			{
				min = arr[j];
				imin = j;
			}
		if (imin != i)
		{
			arr[imin] = arr[i];
			arr[i] = min;
		}
	}
}


int DoCount(int arrive[], int nA, int depart[], int nD)
{
	int rez = nD;
	sort(arrive, nA);
	sort(depart, nD);
	for (int a = 0, d = 0; (a < nA) && (d < nD); ++a, ++d)
		for (; d < nD; ++d)
			if (arrive[a] <= depart[d])
			{
				--rez;
				break;
			};
	return rez;
}


void solve()
{
	static int timesA0[128], timesA1[128];
	static int timesB0[128], timesB1[128];

	int N;
	cin >> N;

	for (int n = 1; n <= N; ++n)
	{
		int T;
		cin >> T;

		int nA, nB;
		cin >> nA >> nB;
		GetData(timesA0, timesA1, nA, T);
		GetData(timesB0, timesB1, nB, T);

		int rezB = DoCount(timesA1, nA, timesB0, nB);
		int rezA = DoCount(timesB1, nB, timesA0, nA);		

		cout << "Case #" << n << ": " << rezA << ' ' << rezB << endl;
	}
}