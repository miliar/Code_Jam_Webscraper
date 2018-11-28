#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;

int main()
{
	int N;
	cin >> N;

	for(int t=1; t <= N; ++t)
	{
		int S;
		cin >> S;
		if(cin.peek() == '\n')
			cin.get();

		map<string,int> senametab;
		vector<int> offset(S);

		const int INFINITY = -1;

		for(int i=0; i < S; ++i)
		{
			string sename;
			getline(cin, sename);

			senametab[sename] = i;

			offset[i] = INFINITY;
		}

		int Q;
		cin >> Q;
		if(cin.peek() == '\n')
			cin.get();

		int numSwitches=0, atInfinity=S;

		for(int j=0; j < Q; ++j)
		{
			string sename;
			getline(cin, sename);

			int c = senametab[sename];

			if(offset[c] == INFINITY)
			{
				offset[c] = j;

				if(! --atInfinity)
				{
					++numSwitches;

					for(int i=0; i < S; ++i)
						offset[i] = INFINITY;

					offset[c] = j;

					atInfinity = S - 1;
				}
			}
		}

		cout << "Case #" << t << ": " << numSwitches << endl;
	}

	return 0;
}