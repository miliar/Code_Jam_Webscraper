# include <iostream>
# include <vector>

using namespace std;

vector<int> oList;
int oTarget;
int oPos;
vector<int> bList;
int bTarget;
int bPos;
vector<pair<char, int> > fullList;

void oMove()
{
	if (oTarget == -1)
	{
		return;
	}

	if (oList[oTarget] > oPos)
	{
		oPos++;
	}
	else if (oList[oTarget] < oPos)
	{
		oPos--;
	}
}

void bMove()
{
	if (bTarget == -1)
	{
		return;
	}

	if (bList[bTarget] > bPos)
	{
		bPos++;
	}
	else if (bList[bTarget] < bPos)
	{
		bPos--;
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	for (int curTestId = 0; curTestId < T; ++curTestId)
	{
		oList.clear();
		bList.clear();
		fullList.clear();

		int fullListSize;
		cin >> fullListSize;
		fullList.resize(fullListSize);
		for (int i = 0; i < fullListSize; ++i)
		{
			cin >> fullList[i].first >> fullList[i].second;
			if (fullList[i].first == 'O')
			{
				oList.push_back(fullList[i].second);
			}
			else
			{
				bList.push_back(fullList[i].second);
			}
		}

		if (oList.empty())
		{
			oTarget = -1;
		}
		else
		{
			oTarget = 0;
		}

		if (bList.empty())
		{
			bTarget = -1;
		}
		else
		{
			bTarget = 0;
		}
		oPos = 1;
		bPos = 1;

		int timeAns = 0;
		
		for (int mainTarget = 0; mainTarget < fullListSize; ++mainTarget)
		{
			bool reached = false;
			do
			{
				bool oPush = false;
				bool bPush = false;
				if (fullList[mainTarget].first == 'O')
				{
					if (oPos == fullList[mainTarget].second)
					{						
						reached = true;
						oPush = true;
						oTarget++;
						if (oTarget == oList.size())
						{
							oTarget = -1;
						}
					}
				}
				else if (fullList[mainTarget].first == 'B')
				{
					if (bPos == fullList[mainTarget].second)
					{						
						reached = true;
						bPush = true;
						bTarget++;
						if (bTarget == bList.size())
						{
							bTarget = -1;
						}
					}
				}				

				if (!oPush)
				{
					oMove();
				}

				if (!bPush)
				{
					bMove();
				}

				timeAns++;
			}
			while (!reached);						
		}

		cout << "Case #" << curTestId + 1 << ": " << timeAns << endl;
	}

	return 0;
}