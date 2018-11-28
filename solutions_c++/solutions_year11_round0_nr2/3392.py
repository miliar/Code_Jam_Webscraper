# include <iostream>
# include <string>
# include <vector>
# include <algorithm>

using namespace std;

vector<string> combList;
int combNum;
vector<string> oppList;
int oppNum;
int alphaCnt[300];
string str;

bool CheckForOpp()
{
	for (int i = 0; i < oppNum; ++i)
	{
		if (alphaCnt[oppList[i][0]] > 0 && alphaCnt[oppList[i][1]] > 0)
		{
			return true;
		}
	}

	return false;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testNum;
	cin >> testNum;
	for (int curTestId = 1; curTestId <= testNum; ++curTestId)
	{
		cin >> combNum;
		combList.resize(combNum);
		for (int i = 0; i < combNum; ++i)
		{
			cin >> combList[i];
		}

		cin >> oppNum;
		oppList.resize(oppNum);
		for (int i = 0; i < oppNum; ++i)
		{
			cin >> oppList[i];
		}

		int inputSeqSize;
		cin >> inputSeqSize;
		string inputSeq;
		cin >> inputSeq;

		fill(alphaCnt, alphaCnt + 300, 0);
		str.clear();

		for (size_t curSimInd = 0; curSimInd < inputSeq.size(); ++curSimInd)
		{
			char cur = inputSeq[curSimInd];			

			str.push_back(cur);
			alphaCnt[cur]++;

			bool doSmth;
			do
			{
				doSmth = false;

				if (str.size() > 1)
				{
					const string lastTwo(str.end() - 2, str.end());

					for (int i = 0; i < combNum; ++i)
					{
						if ((lastTwo[0] == combList[i][0] && lastTwo[1] == combList[i][1])
							|| (lastTwo[1] == combList[i][0] && lastTwo[0] == combList[i][1]))
						{
							alphaCnt[lastTwo[0]]--;
							alphaCnt[lastTwo[1]]--;
							str.pop_back();
							str.pop_back();
							str.push_back(combList[i][2]);
							alphaCnt[combList[i][2]]++;
							doSmth = true;
							break;
						}
					}
				}

				if (CheckForOpp())
				{
					fill(alphaCnt, alphaCnt + 300, 0);
					str.clear();
					doSmth = true;
				}
			}
			while (doSmth);
		}

		cout << "Case #" << curTestId << ": " << "[";
		for (size_t i = 0; i < str.size(); ++i)
		{
			cout << str[i];
			if (i + 1 != str.size())
			{
				cout << ", ";
			}
		}
		cout << "]" << endl;
	}

	return 0;
}