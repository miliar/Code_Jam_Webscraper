#include <vector>
#include <iostream>
#include <algorithm>
#include <utility>
#include <map>
#include <cmath>

using namespace std;

int main()
{
    int n;
    cin >> n;
    
    for(int z = 0; z < n; z++)
    {
	int retVal = 0;

	int h, w, r;
	int dx[2] = {-1, -2};
	int dy[2] = {-2, -1};
	cin >> h >> w >> r;

	vector<pair<int, int> > rocks;
	for(int i = 0; i < r; i++)
	{
	    int x, y;
	    cin >> y >> x;
	    rocks.push_back(make_pair(x, y));
	}

	sort(rocks.begin(), rocks.end());

	int dp[101][101]; 
        memset(dp, 0, sizeof dp);
	dp[1][1] = 1;
	

	for(int i = 1; i <= 100; i++)
	  for(int j = 1; j <= 100; j++)
	  {
	      for(int k = 0; k < 2; k++)
	      {
		  int new_i = i + dx[k];
		  int new_j = j + dy[k];
		  
		  if(new_i <= 0 || new_i > w || new_j <= 0 || new_j > h)
		      continue;
		  else if(!binary_search(rocks.begin(), rocks.end(), make_pair(new_i, new_j)))
		  {
		      dp[i][j] += dp[new_i][new_j];
		      dp[i][j] %= 10007;
		  }
	      }
	  }


	cout << "Case #" << z + 1 << ": " << dp[w][h] << endl;
    }
}
