#include <iostream>
#include <vector>

using namespace std;

int T, N;
int total;
int posA, posB;

vector<pair<int,int> > qO, qB;

int movePush(int& pos, int target)
{
	if (pos < target)
		pos++;
	else
		if (pos > target)
			pos--;
		else
			return 1;

	return 0;
}

void moveOnly(int& pos, int target)
{
	if (pos < target)
		pos++;
	else
		if (pos > target)
			pos--;		
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("ouput.out", "w", stdout);

	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		cin >> N;
		
		posA = 1;
		posB = 1;
		qO.clear();
		qB.clear();

		for (int i = 0; i < N; ++i)
		{
			char pl;
			int bt;
			cin >> pl >> bt;
			if (pl == 'O')
				qO.push_back(make_pair(bt,i));
			else
				qB.push_back(make_pair(bt,i));
		}

		int indO, indB;
		indO = indB = 0;
		total = 0;

		qO.push_back(make_pair(1, 1000000));
		qB.push_back(make_pair(1, 1000000));

		while (indO + 1 < qO.size() || indB + 1 < qB.size())
		{
			if (qO[indO].second < qB[indB].second)
			{
				++total;
				indO += movePush(posA, qO[indO].first);
				moveOnly(posB, qB[indB].first);
			}
			else
			{
				++total;
				indB += movePush(posB, qB[indB].first);
				moveOnly(posA, qO[indO].first);
			}
		}

		cout << "Case #" << t <<": " << total << endl;
	}

	return 0;
}