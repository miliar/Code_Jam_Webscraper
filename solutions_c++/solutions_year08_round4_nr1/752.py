#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FORE(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define CLEAR(x,with) memset(x,with,sizeof(x))  

#define pb push_back
#define all(x) (x).begin(),(x).end()
#define sz(a) int((a).size())

typedef pair<int,int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

int main()
{
	int numCases;
	cin >> numCases;

	for(int c=1; c<=numCases; c++)
	{
		int M, V;
		int ans = 0;
		cin >> M >> V;

		vector<pii> in;
		for(int i=0; i<(M-1)/2; i++)
		{
			pii temp;
			cin >> temp.first >> temp.second;
			in.push_back(temp);
		}
		for(int i=(M-1)/2; i<M; i++)
		{
			pii temp;
			cin >> temp.first;
			temp.second = -1;
			in.push_back(temp);
		}

		vi val;
		for(int i=0; i<M; i++) val.push_back(-1);
		for(int i=M-1; i>=0; i--)
		{
			if(i < (M-1)/2)
			{
				if(in[i].first == 0) // and
					val[i] = val[2*i+1] | val[2*i+2];
				else // or
					val[i] = val[2*i+1] & val[2*i+2];
			}
			else
			{
				val[i] = in[i].first;
			}
		}
		vi cost;
		for(int i=0; i<M; i++) cost.push_back(-1);

//		for(int i=0; i<M; i++) cout << "val " << i << " : " << val[i] << endl;
		for(int i=(M-1)/2 - 1; i>=0; i--)
		{
//			cout << "doing " << i << endl;
			int child1 = 2*i+1, child2 = 2*i+2;
			int calc_cost = 12345;
			if(val[i] == 0) // want to change it to 1
			{
				for(int ii=0; ii<2; ii++)
				{
					if(cost[child1] == -1 && val[child1] != ii) // can't change it
						continue;
					for(int jj=0; jj<2; jj++)
					{
						if(cost[child2] == -1 && val[child2] != jj) // can't change it
						continue;
//cout << ii << " " << jj << endl;
						int sum_cost = 0;
						if(ii != val[child1]) sum_cost += cost[child1];
						if(jj != val[child2]) sum_cost += cost[child2];
						if(in[i].first == 0 && ((ii | jj) == 1))
							calc_cost = min(calc_cost, sum_cost);
						else if(in[i].first == 1 && ((ii & jj) == 1))
							calc_cost = min(calc_cost, sum_cost);

						if(in[i].second == 1) // changeable
						{
							if(in[i].first == 0 && ((ii & jj) == 1)) 
								calc_cost = min(calc_cost, sum_cost + 1);
							else if(in[i].first == 1 && ((ii | jj) == 1))
								calc_cost = min(calc_cost, sum_cost + 1);
						}
					}
				}
			}
			else // want to change it to 0
			{
				for(int ii=0; ii<2; ii++)
				{
//					cout << i << " " << ii << " --" << endl;
					if(cost[child1] == -1 && val[child1] != ii) // can't change it
						continue;
					for(int jj=0; jj<2; jj++)
					{
//						cout << i << " " << ii << " " << jj << endl;
						if(cost[child2] == -1 && val[child2] != jj) // can't change it
							continue;

						
						int sum_cost = 0;
						if(ii != val[child1]) sum_cost += cost[child1];
						if(jj != val[child2]) sum_cost += cost[child2];
						if(in[i].first == 0 && ((ii | jj) == 0)) // and
							calc_cost = min(calc_cost, sum_cost);
						else if(in[i].first == 1 && ((ii & jj) == 0)) // or
							calc_cost = min(calc_cost, sum_cost);

						if(in[i].second == 1) // changeable
						{
							if(in[i].first == 0 && ((ii & jj) == 0)) // and
								calc_cost = min(calc_cost, sum_cost + 1);
							else if(in[i].first == 1 && ((ii | jj) == 0)) // or
								calc_cost = min(calc_cost, sum_cost + 1);
						}
					}
				}
			}
			if(calc_cost == 12345) cost[i] = -1;
			else cost[i] = calc_cost;

//			cout << i << " : " << cost[i] << endl;
		}


		if(val[0] == V) cost[0] = 0;
		if(cost[0] == -1)
			cout << "Case #" << c << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << c << ": " << cost[0] << endl;
	}

	return 0;
}
