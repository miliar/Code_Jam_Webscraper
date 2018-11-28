#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <strstream>

using namespace std;

int nCases;
int caseNumber;
int answer;
int N;
int Ai[1000];
int Bi[1000];

void debug1()
{	cout << "" << endl;}

int ProcessCase()
{
	int intersect = 0;
	for (int i=0; i<N; i++)
	{
		for (int j=i+1; j<N; j++)
		{
			if ((Ai[j] < Ai[i]) && (Bi[j] > Bi[i]))
				intersect++;
			else
				if ((Ai[j] > Ai[i]) && (Bi[j] < Bi[i]))
					intersect++;
		}
	}
	answer = intersect;
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
	//file1 = "e:\\B-large.in";
	FILE * ps;
	freopen_s(&ps, file1.c_str(), "rt", stdin);
	// uncomment for file output:
	//file2 = "e:\\C-small-practice.out";
	file2 = "e:\\z2out.txt";
	//freopen_s(&ps, file2.c_str(), "wt", stdout);
#endif
	scanf("%d", &nCases);
	for (int ci=0; ci<nCases; ci++)
	{
		scanf("%d", &N);
		for (int i=0; i<N; i++)
		{
			scanf("%d", &Ai[i]);
			scanf("%d", &Bi[i]);
		}
		caseNumber = ci+1;
		answer = ProcessCase();
		cout << "Case #" << caseNumber << ": ";
		cout << answer << endl;
	}
	return 0;
}
