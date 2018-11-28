#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
using namespace std;


#define metafor(it, v) for ( it = v.begin(); it != v.end(); it++ )

int DoRide(queue<int> &groupQueue, int k, int N)
{
	int tickets=0;
	int upgroups=0;
	while(tickets+groupQueue.front() <= k && upgroups < N)
	{
		int g = groupQueue.front();
		tickets+=g;
		upgroups++;
		groupQueue.pop();
		groupQueue.push(g);
	}
	return tickets;
}

int sum(const vector<int> &groups)
{
	int s=0;
	vector<int>::const_iterator it;
	metafor(it, groups)
		s+=*it;
	return s;
}

vector<int> RevenuesPerCycle(const vector<int> &groups, int k, int R)
{
	queue<int> groupQueue;
	{
		vector<int>::const_iterator it;
		metafor(it, groups)
			groupQueue.push(*it);
	}
	queue<int> startQueue = groupQueue;

	vector<int> revenue;
	do
	{
		int riderevenue = DoRide(groupQueue, k, (int)groups.size());
		revenue.push_back(riderevenue);
	} while (revenue.size()<R && startQueue != groupQueue);
	return revenue;
}

int main()
{
	ifstream in("C:\\Users\\German\\Documents\\Visual Studio 2005\\Projects\\Problemas\\C-small-attempt0.in");
	//ifstream in("sample.in");
	ofstream out("C:\\Users\\German\\Documents\\Visual Studio 2005\\Projects\\Problemas\\sol.out");
	int T;
	in >> T;
	getline(in, string());
	for(int t=1; t<=T; t++)
	{
		int R, k, N;
		in >> R >> k >> N;
		vector<int> groups(N);
		{
			vector<int>::iterator it;
			metafor(it, groups)
				in >> *it;
		}
		vector<int> revenuesPerCycle = RevenuesPerCycle(groups, k, R);
		int cycleReps = R / (int)revenuesPerCycle.size();
		int totalRevenue = sum(revenuesPerCycle) * cycleReps;
		int remainingRides = R % revenuesPerCycle.size();
		for(int i=0;i<remainingRides;i++)
			totalRevenue += revenuesPerCycle[i];

		out << "Case #" << t << ": " << totalRevenue << endl;
		
	}
	system("pause");
	return 0;
}
