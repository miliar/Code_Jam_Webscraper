#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <strstream>

using namespace std;

int nCases;
int caseNumber;
int answer;
int N; // dirExists
int Noriginal;
int M; // dirToCreate;
char adirExists[10000][110];
char adirTocreate[100][110];


void debug1()
{
	cout << "" << endl;
}

int ProcessCase()
{
	Noriginal = N;
	answer = 0;
	string newdir;
	string parent;
	int pos;
	for (int i=0; i<M; i++)
	{
		newdir.assign(adirTocreate[i]);
		//try to create from parent
		int startpos = 1;
		while (true)
		{
			pos = newdir.find('/', startpos);
			if (pos >= 0)
				startpos = pos + 1;
			else
				pos = newdir.length();
			parent = newdir.substr(0, pos);
			//does parent exist?
			bool parentExists = false;
			for (int j=0; j<N; j++)
			{
				if (parent.compare(adirExists[j]) == 0)
				{
					parentExists = true;
					break;
				}
			}
			if (!parentExists)
			{
				strcpy(adirExists[N], parent.c_str());
				N++;
			}
			if (pos == newdir.length())
				break;
		}
	}
	answer = N - Noriginal;
	if (answer < 0)
		answer = 0;
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
	file1 = "e:\\A-small-attempt0.in";
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
		scanf("%d", &M);
		for (int i=0; i<N; i++)
		{
			scanf("%s", adirExists[i]);
		}
		for (int i=0; i<M; i++)
		{
			scanf("%s", adirTocreate[i]);
		}
		caseNumber = ci+1;
		answer = ProcessCase();
		cout << "Case #" << caseNumber << ": ";
		cout << answer << endl;
	}
	//cout << "press any key to continue..." << endl; _getch();
	return 0;
}
