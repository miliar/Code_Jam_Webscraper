#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

#define GCJ
#ifdef GCJ
ifstream fin("A-large.in");
ofstream fout("A.out");
#define cin	fin
#define cout fout
#endif

int main()
{
	int T, N;
	cin >> T;
	for(int i=0; i<T; ++i)
	{
		cin >> N;
		int ans = 0;
		vector<int> ordersBtn;
		vector<int> ordersID;
		for(int j=0; j<N; ++j)
		{
			char robot;
			int btn;
			cin >> robot >> btn;
			if(robot == 'O')
			{
				ordersID.push_back(0);
				ordersBtn.push_back(btn);
			}
			else
			{
				ordersID.push_back(1);
				ordersBtn.push_back(btn);
			}
		}

		int lastOrderTime_global = 0;
		int lastOrderTime[2] = {0};
		int pos[2] = {1, 1};
		for(int k=0; k<ordersID.size(); ++k)
		{
			int robotID = ordersID[k];
			int step = abs(ordersBtn[k] - pos[robotID]);
			if (lastOrderTime[robotID] + step < lastOrderTime_global)
			{
				lastOrderTime_global = lastOrderTime_global + 1;
			}
			else
			{
				lastOrderTime_global = lastOrderTime[robotID] + step + 1;
			}
			lastOrderTime[robotID] = lastOrderTime_global;
			pos[robotID] = ordersBtn[k];
		}
		cout << "Case #" << i+1 << ": " << lastOrderTime_global << endl;
	}
	return 0;
}