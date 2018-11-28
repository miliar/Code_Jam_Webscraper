#include <iostream>
#include <stdio.h>

using namespace std;

int groups[1000];
int numRides[1000];			//till the first time group i is first in line
long long numEuros[1000];	//till the first time group i is first in line
long long numProfit[1000];	//this ride only
int offs[1000];				//number of groups that get in when group i is first in line

int T,R,k,N;

void init()
{
	for (int i = 0; i < 1000; i++)
	{
		groups[i] = -1;
		numEuros[i] = -1;
		numRides[i] = -1;
		numProfit[i] = -1;
		offs[i] = -1;
	}
}

long long profit(int curr)
{
	if (numProfit[curr] != -1)
		return numProfit[curr];
	
	long long num = 0;
	long long newcurr = curr;
	long long lastcurr = curr;
	int j = 0;
	bool atLeastOne = false;
	while (num <= k)
	{
		if (newcurr == curr && atLeastOne)
			break;
		lastcurr = newcurr;
		num += groups[newcurr];
		newcurr++;
		newcurr %= N;
		j++;
		atLeastOne = true;
	}
	if (num > k)
	{
		num -= groups[lastcurr];
		j--;
	}
	offs[curr] = j;
	numProfit[curr] = num;
	return num;
}

void solve(int c)
{
	long long int euros = 0, loop;
	int curr = 0;
	int i,j;
	for (i = 0; i < R; i++)
	{
		if (numEuros[curr] != -1)
			break;
		numRides[curr] = i;
		numEuros[curr] = euros;
		euros += profit(curr);
		curr += offs[curr];
		curr %= N;
	}
	if (i != R)
	{
		// Loop terminated by break statement
		// This means we've detected a cycle
		loop = euros;
		int count = 0;
		for (j = i; j < R; j += i - numRides[curr])
		{
			euros += loop - numEuros[curr];
			count++;
		}
		// Now we've made too many rides
		j -= i - numRides[curr];
		euros -= loop - numEuros[curr];
		for ( ; j < R; j++)
		{
			euros += numProfit[curr];
			curr += offs[curr];
			curr %= N;
		}
	}
	// Use cout for easier long long int printing
	cout << "Case #" << c << ": " << euros << endl;
}

int main()
{
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		init();
		scanf("%d %d %d", &R, &k, &N);
		for (int j = 0; j < N; j++)
		{
			int temp;
			scanf("%d", &temp);
			groups[j] = temp;
		}
		solve(i + 1);
	}
	return 0;
}

