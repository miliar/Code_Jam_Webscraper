#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <strstream>

using namespace std;

int nCases;
int caseNumber;
int answer;
int N;	//all chicks, max 50
int K;	//k chicks, max = N
int B;	//barn, max 1,000,000,000
int T;	//time, max 1,000
int Xi[50];	//position
int Vi[50];	//speed
double Ti[50];	//time

void debug1()
{
	cout << "" << endl;
}

int ProcessCase()
{
	int curK = 0;
	answer = 0;
	// time, assuming no barrier
	for (int i=0; i<N; i++)
	{
		double dist = B - Xi[i];
		Ti[i] = dist / Vi[i];
	}
	int nswap = 0;
	int chickleft = K;
	for (int i=N-1; i>=0; i--)
	{
		if (Ti[i] <= T)
			chickleft--;
		else
			nswap += chickleft;
		if (chickleft == 0)
			break;
	}
	if (chickleft == 0)
		answer = nswap;
	else
		answer = -1;
	return answer;
}

int main()
{
#ifdef SN_INPUT_FILE
	string file1;
	string file2;
	//file1 = "e:\\test_input1.txt";
	//file1 = "e:\\A-large-practice.in";
	file1 = "e:\\ztest.txt";
	//file1 = "e:\\A-small-attempt0.in";
	file1 = "e:\\B-small-attempt0.in";
	FILE * ps;
	freopen_s(&ps, file1.c_str(), "rt", stdin);
	// uncomment for file output:
	//file2 = "e:\\C-small-practice.out";
	file2 = "e:\\z1out.txt";
	freopen_s(&ps, file2.c_str(), "wt", stdout);
#endif
	scanf("%d", &nCases);
	for (int ci=0; ci<nCases; ci++)
	{
		scanf("%d", &N);
		scanf("%d", &K);
		scanf("%d", &B);
		scanf("%d", &T);
		for (int i=0; i<N; i++)
		{
			scanf("%d", &Xi[i]);
		}
		for (int i=0; i<N; i++)
		{
			scanf("%d", &Vi[i]);
		}
		caseNumber = ci+1;
		answer = ProcessCase();
		cout << "Case #" << caseNumber << ": ";
		if (answer >= 0)
			cout << answer << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	//cout << "press any key to continue..." << endl; _getch();
	return 0;
}
