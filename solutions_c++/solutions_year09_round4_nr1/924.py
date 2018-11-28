#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int SolveTestCase()
{
	int n;
	cin >> n;
	vector<string> mat(n);
	
	string str;
	
	for (int i = 0; i < n; i++)
		cin >> mat[i];

	int ans = 0;
	for (int i = 0; i < n - 1; i++)
	{
		for (int j = i; j < n; j++)
		{
			bool good = true;
			for (int h = i + 1; h < n; h++)
				if (mat[j][h] == '1')
					good = false;

			if (good)
			{
				ans += j - i;
				for (int q = j; q > 0; q--)
					swap(mat[q], mat[q - 1]);
				
				break;
			}
		}
	}


	return ans;
}

void PrintAnswerToTestCase(int caseNumber, int ans)
{
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase() );

	return 0;
}