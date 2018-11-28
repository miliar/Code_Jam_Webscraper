#include<fstream>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<functional>
#include<numeric>
using namespace std;
typedef long long ll;

int result;
vector<int> c;
int cards[10004];
int freebies[10004];

bool solve(int next)
{
	while (cards[next] == 0)
	{
		if (next > 10000) return true;
		++next;
	}

	int freeToUse = min(cards[next], freebies[next]);
	if (freeToUse > 0)
	{
		cards[next] -= freeToUse;
		freebies[next] -= freeToUse;
		freebies[next+1] += freeToUse;
		return solve(next);
	}
	
	// Need to try a new straight
	int numToStart = cards[next];
	for (int i=0; i<result; ++i)
	{
		cards[next+i] -= numToStart;
		if (cards[next+i] < 0)
			return false;
	}

	freebies[next+result] += numToStart;
	return solve(next);
}

bool solve()
{
	memset(cards,0,sizeof(cards));
	memset(freebies,0,sizeof(freebies));
	for (int i=0; i<c.size(); ++i)
		++cards[c[i]];
	vector<int> empty;
	return solve(0);
}




int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	unsigned int numberOfCases;
	fin >> numberOfCases;

	int N;
	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		fin >> N;
		c.assign(N,0);
		result = 0;
		for (int i=0; i<N; ++i)
		{
			result = 1;
			fin >> c[i];
		}

		if (c.size() > 1)
		{
			sort(c.begin(), c.end());
			result = c.size();
			if (!solve())
			{
				result = result / 2;
				while (result > 1 && !solve())
					--result;
			}

		}

		fout << "Case #" << zz << ": " << result << endl;
	}

	return 0;
}