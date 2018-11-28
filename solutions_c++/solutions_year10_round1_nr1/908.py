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
#include <cstring>
#include <cstdlib>
#include <ctime>
 
#define SZ(a) (int)(a).size()
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define INF (int)1e9
 
#define ll long long
#define vi vector<int>
#define vs vector<string>
 
using namespace std;

string test(vs &board, int K)
{
	int N = SZ(board);
	bool red = false, blue = false;
	
	vector < vi > cnt(N, vector <int> (N, 1));

	for(int i = N - 1; i >= 0; i--)
	{
		for(int j = 0; j < N; j++)
		{
			if(board[i][j] == '.')
				continue;
			int a = 1;
			while(i + a < N && board[i + a][j] == board[i][j])
				a++;

			int b = 1;
			while(j - b >= 0 && board[i][j - b] == board[i][j])
				b++;
	
			int c = 1;
			while(i + c < N && j - c >= 0 && board[i + c][j - c] == board[i][j])
			{
				c++;
			}

			int d = 1;
			while(i + d < N && j + d < N && board[i + d][j + d] == board[i][j])			
			{
				d++;
			}
		
			if(a >= K || b >= K || c >= K || d >= K)
				if(board[i][j] == 'R')
					red = true;			
				else
					blue = true;			
			
		}
	}
	if(red && blue)
			return "Both";
	else if(red)
			return "Red";
	else if(blue)
			return "Blue";
	else
			return "Neither";

}

int main()
{
	int T;
	cin >> T;

	for(int i = 1; i <= T; i++)
	{
		int N, K;
		cin >> N >> K;

		vs board(N);
		for(int j = 0; j < N; j++)
		{
			cin >> board[j];
		}

		vs rboard(N);
		for(int j = 0; j < N; j++)
		{
			rboard[j] = "";
			for(int k = N - 1; k >= 0; k--)
			{
				string t = board[k].substr(j, 1);
				rboard[j] += t;
			}
		}

		for(int j = 0; j < N; j++)		
		{
			for(int k = N - 1; k >= 0; k--)
			{
				int low = k + 1;
				while(low < N && rboard[low][j] == '.')
				{
					rboard[low][j] = rboard[low - 1][j];
					rboard[low - 1][j] = '.';
					low++;
				}
				
			}
		}
		
		cout << "Case #" << i << ": " << test(rboard, K) << endl;
		/*for(int a = 0; a < N; a++) 
			cout << rboard[a] << endl;
		*/
	}
	return 0;
}
