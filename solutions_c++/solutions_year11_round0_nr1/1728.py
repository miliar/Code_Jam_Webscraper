#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int calculateNewPos(int currPos, int dir)
{
	int newPos = currPos;
	
}

int main()
{
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		int N;
		cin >> N;
		vector<char> R(N);
		vector<int>  P(N);
		
		for(int j = 0; j < N; j++)
		{
			cin >> R[j];
			cin >> P[j];
		}
		
		int currO = 1;
		int bufferO = 0;
		int currB = 1;
		int bufferB = 0;
		int ans = 0;
		for(int j = 0; j < N; j++)
		{
			if(R[j] == 'O')
			{
				int tO = abs(P[j] - currO) - bufferO;
				ans += max(tO, 0) + 1;
				bufferO = 0;
				bufferB += max(tO, 0) + 1;
				currO = P[j];
			}
			else
			{
				int tB = abs(P[j] - currB) - bufferB;
				ans += max(tB, 0) + 1;
				bufferB = 0;
				bufferO += max(tB, 0) + 1;
				currB = P[j];
			}
		}
		
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	//system("pause");
	return 0;
}
