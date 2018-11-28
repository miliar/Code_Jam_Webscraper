#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n;
		cin >> n;
		int cur1 = 1,  cur2 = 1;
		int time1 = 0, time2 = 0;
		string str;
		int x;
		int time = 0;
		for(int i = 0; i < n; i++)
		{
			cin >> str >> x;
			if(str[0] == 'B')
			{
				if(time - time1 >= abs(x - cur1))
				{
					time++;
				}
				else
				{
					time += abs(x - cur1) - time + time1 + 1;
				}
				cur1 = x;
				time1 = time;
			}
			else
			{
				if(time - time2 >= abs(x - cur2))
				{
					time++;
				}
				else
				{
					time += abs(x - cur2) - time + time2 + 1;
				}
				cur2 = x;
				time2 = time;
			}
		}
		cout << time << endl;
	}
	return 0;
}
