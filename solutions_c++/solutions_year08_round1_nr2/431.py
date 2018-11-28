#include <iostream>
using namespace std;

const int N=2000;
const int M=2000;

int minMalted;
bool best[N+1];

int need_count[M+1];
int need_x[M+1][N+1]; //m customers, every one have at most N need
bool need_y[M+1][N+1];

int n, m;



bool matched(bool *value)
{
	bool result=true;
	int i,j;
	for(i=0; i<m; i++)
	{
		for(j=0; j<need_count[i]; j++)
		{
			if(value[need_x[i][j]-1] == need_y[i][need_x[i][j]-1])
			{
				break;
			}
		}
		if(j>=need_count[i])
		{
			result = false;
			break;
		}
	}
	return result;
}

void dps(int index, bool *value, int maltCount)
{
	if(index == n-1)
	{
		if(maltCount<minMalted && matched(value) )
		{
			minMalted = maltCount;
			memcpy(best, value, sizeof(best));
		}
		return;
	}
	value[index+1] = false;
	dps(index+1, value, maltCount);
	value[index+1] = true;
	dps(index+1, value, maltCount+1);
}

void solve()
{
	bool value[N+1];
	memset(value, 0, sizeof(value));
	value[0] = false;
	dps(0, value, 0);
	value[0] = true;
	dps(0, value, 1);
}

int main()
{
	int c; //test cases
	int k; //current test case
	cin >> c;
	k=1;
	while(k<=c)
	{
		cin >> n;
		cin >> m;
		memset(need_count, 0, sizeof(need_count));
		memset(need_x, 0, sizeof(need_x));
		memset(need_y, 0, sizeof(need_y));
		for(int i=0; i<m; i++)
		{
			cin >> need_count[i];
			for(int j=0; j<need_count[i]; j++)
			{
				cin >> need_x[i][j];
				cin >> need_y[i][need_x[i][j]-1]; //bool values!
			}
		}
		minMalted = N+1;
		solve();
		cout << "Case #" << k << ":" ;
		if(minMalted == N+1)
		{
			cout << " IMPOSSIBLE" << endl;
		}
		else
		{
			for(int i=0; i<n; i++)
				cout <<  " " << best[i];
			cout << endl;
		}
		k++;
	}

	return 0;
}