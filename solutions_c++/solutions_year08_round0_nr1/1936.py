#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool seenAll(vector<bool> seen)
{
	for (int i = 0; i < seen.size(); i++)
        if (!seen[i])
            return false;

	return true;
}

int main()
{
	int N, S, Q;

	cin >> N;
	for (int i = 1; i <= N; i++)
	{
		cin >> S; getchar();
		vector<string> SE(S);
		vector<bool> seen(S, false);

		for (int j = 0; j < S; j++)
			getline(cin, SE[j]);

		cin >> Q; getchar();
		int switches = 0;
		string query;
		for (int j = 0; j < Q; j++)
		{
			getline(cin, query);
			seen[find(SE.begin(), SE.end(), query) - SE.begin()] = true;
			if (seenAll(seen))
			{
				switches++;
				seen.assign(S, false);
       			seen[find(SE.begin(), SE.end(), query) - SE.begin()] = true;
            }
		}

		cout << "Case #" << i << ": " << switches << endl;
	}

	return 0;
}
