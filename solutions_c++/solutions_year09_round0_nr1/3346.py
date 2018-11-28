#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <locale>

using namespace std;

int L, D, N;
vector<string> K;
vector<int> arrCount;
vector<string> candidate;
vector< vector<string>* > splitCandi;

string strCurProc;

void Split(string original, vector<string>* arrSplit)
{
	int size = original.length();
	int curPos = 0;
	while (1)
	{
		if (isalpha(original[curPos]))
		{
			arrSplit->push_back(original.substr(curPos, 1));
			curPos++;
		}
		else if (original[curPos++] == '(')
		{
			int last = curPos;
			while (1)
			{
				if (original[last] == ')')
					break;
				last++;
			}

			arrSplit->push_back(original.substr(curPos, last - curPos));
			curPos = last + 1;
		}

		if (curPos == size)
			break;
	}
}

void Input()
{
	ifstream ifs("A-small.in");

	ifs >> L >> D >> N;

	for (int i = 0; i < D; i++)
	{
		string curLine;
		ifs >> curLine;
		K.push_back(curLine);
	}

	for (int i = 0; i < N; i++)
	{
		string curLine;
		ifs >> curLine;
		candidate.push_back(curLine);

		vector<string>* arr = new vector<string>;
		Split(curLine, arr);

		splitCandi.push_back(arr);
		arrCount.push_back(0);
	}

	ifs.close();
}

void constructor(int curPos, char strCon[], int count)
{
	if (count >= 1)
	{
		int validCnt = 0;
		for (int i = 0; i < D; i++)
		{
			string str = K[i];
			if (!strncmp(str.c_str(), strCon, count)) {
				validCnt++;
				break;
			}
		}

		if (validCnt == 0)
			return;
	}

	if (count == L)
	{
		for (int i = 0; i < D; i++)
		{
			if (K[i] == strCon)	{
				arrCount[curPos]++;
				break;
			}
		}

		return;
	}

	vector<string>* arr = splitCandi[curPos];

	string str = arr->at(count);
	for (int j = 0; j < str.size(); j++)
	{
		strCon[count] = str[j];
		constructor(curPos, strCon, count + 1);
	}
}

void Process()
{
	char arr[15] = {0};
	for(int i = 0; i < N; i++)
	{
		cout << "Case #" << i + 1 << endl;
		constructor(i, arr, 0);
	}
}

void Output()
{
	ofstream ofs("A-small.out");
	for (int i = 0; i < N; i++)
		ofs << "Case #" << i+1 << ": " << arrCount[i] << endl;

	ofs.close();
}

int main(void)
{
	Input();
	Process();
	Output();

	
	for (int i = 0 ; i < splitCandi.size(); i++)
	{
		delete splitCandi[i];
	}

	return 0;
}