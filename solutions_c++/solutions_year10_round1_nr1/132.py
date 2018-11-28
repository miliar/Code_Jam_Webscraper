#include <vector>
#include <algorithm>

#include <cstdio>

using namespace std;

#define RED 0
#define BLUE 1

bool findRun(int color, int N, int K, const vector<vector<int> >& cols)
{
	for (int c = 0; c < N; ++c)
	{
		int run = 0;
		for (int p = 0; p < N; ++p)
		{
			if (cols[c][p] == color)
			{
				if (++run >= K)
					return true;
			}
			else
				run = 0;
		}
	}
	for (int r = 0; r < N; ++r)
	{
		int run = 0;
		for (int p = 0; p < N; ++p)
		{
			if (cols[p][r] == color)
			{
				if (++run >= K)
					return true;
			}
			else
				run = 0;
		}
	}
	for (int s = -N + 1; s <= N - 1; ++s)	// s == c - r
	{
		int run = 0;
		for (int c = max(0, s); c <= N - 1 + min(0, s); ++c)
		{
			if (cols[c][c - s] == color)
			{
				if (++run >= K)
					return true;
			}
			else
				run = 0;
		}
	}
	for (int s = 0; s <= (N - 1) * 2; ++s)	// s == c + r
	{
		int run = 0;
		for (int c = max(0, s - N + 1); c <= min(N - 1, s); ++c)
		{
			if (cols[c][s - c] == color)
			{
				if (++run >= K)
					return true;
			}
			else
				run = 0;
		}
	}
	return false;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int idxCase = 0; idxCase < T; ++idxCase)
    {
        int N, K;
        scanf("%d%d", &N, &K);
    	vector<vector<int> > cols(N);
    	for (int c = 0; c < N; ++c)
    	{
    		cols[c].reserve(N);
    		for (int i = 0; i < N; ++i)
    		{
	    		char ch;
    			scanf(" %c", &ch);
    			switch (ch)
    			{
    			case 'R':
    				cols[c].push_back(RED);
    				break;
    			case 'B':
    				cols[c].push_back(BLUE);
    				break;
    			}
    		}
    		reverse(cols[c].begin(), cols[c].end());
    		cols[c].insert(cols[c].end(), N - (int)cols[c].size(), -1);
    	}
    	bool red = findRun(RED, N, K, cols);
    	bool blue = findRun(BLUE, N, K, cols);
    	const char* res;
    	if (red)
    	{
    		if (blue)
    			res = "Both";
    		else
    			res = "Red";
    	}
    	else
    	{
    		if (blue)
    			res = "Blue";
    		else
    			res = "Neither";
    	}
    	printf("Case #%d: %s\n", idxCase + 1, res);
    }
    return 0;
}
