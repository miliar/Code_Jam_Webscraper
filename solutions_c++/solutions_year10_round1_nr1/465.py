#include <iostream>
#include <algorithm>
#include <stack>
#include <string>
#include <queue>
#include <vector>
#include <map>

#define for0(a,b) for(int a = 0; a < b; a ++)

using namespace std;

char ba[50][50];
char bb[50][50];

int main()
{
	int T; cin >> T;
	for0(kase,T)
	{
		int N, K;
		cin >> N >> K;
		string xs; //cin >> xs;
		for0(i,N)
		{
			cin >> xs;
			for0(j,N)
			{
				ba[i][j] = xs[j];
			}
		}
		
		// cout <<endl << "Before" << endl;
		// for0(i,N)
		// {
			// for0(j,N)
				// cout << ba[i][j];
			// cout << endl;
			// }
		// cout << endl << "After" << endl;
		for0(i,N) for0(j,N)
			bb[j][N-i-1] = ba[i][j];
		// for0(i,N)
		// {
			// for0(j,N)
				// cout << bb[i][j];
			// cout << endl;
			// }
		// cout <<  endl << "Gravity" << endl;
		for0(n,N)
		{
			for0(j,N)
			{
				for(int i = N-1; i > 0; i --)
				{
					if (bb[i][j] == '.')
					{
						bb[i][j] = bb[i-1][j];
						bb[i-1][j] = '.';
					}
				}
			}
		}
		// for0(i,N)
		// {
			// for0(j,N)
				// cout << bb[i][j];
			// cout << endl;
		// }
		
		bool redK = false, blueK = false;
		int curRed, curBlue;
		// cout << "K = " << K << endl;
		// rows
		for0(i,N) 
		{
			curRed = curBlue = 0;
			for0(j,N)
			{
				if (bb[i][j] == 'R') curRed ++;
				else curRed = 0;
				if (bb[i][j] == 'B') curBlue ++;
				else curBlue = 0;
				if (curRed == K) redK = true;
				if (curBlue == K) blueK = true;
			}
		}
		// cols
		for0(j,N) 
		{
			curRed = curBlue = 0;
			for0(i,N)
			{
				if (bb[i][j] == 'R') curRed ++;
				else curRed = 0;
				if (bb[i][j] == 'B') curBlue ++;
				else curBlue = 0;
				if (curRed == K) redK = true;
				if (curBlue == K) blueK = true;
			}
		}
		
		// diags 1
		for0(i,N)
		{
		
			curRed = curBlue = 0;
			for0(j,i+1)
			{
				if (bb[i-j][j] == 'R') curRed ++;
				else curRed = 0;
				if (bb[i-j][j] == 'B') curBlue ++;
				else curBlue = 0;
				if (curRed == K) redK = true;
				if (curBlue == K) blueK = true;
			}
		}
		// diags 2
		for0(i,N)
		{
		
			curRed = curBlue = 0;
			for0(j,i+1)
			{
				if (bb[N-(i-j)-1][N-j-1] == 'R') curRed ++;
				else curRed = 0;
				if (bb[N-(i-j)-1][N-j-1] == 'B') curBlue ++;
				else curBlue = 0;
				if (curRed == K) redK = true;
				if (curBlue == K) blueK = true;
			}
		}
		// diags 3
		for0(i,N)
		{
		
			curRed = curBlue = 0;
			for0(j,i+1)
			{
				if (bb[N-(i-j)-1][j] == 'R') curRed ++;
				else curRed = 0;
				if (bb[N-(i-j)-1][j] == 'B') curBlue ++;
				else curBlue = 0;
				if (curRed == K) redK = true;
				if (curBlue == K) blueK = true;
			}
		}
		// diags 4
		for0(i,N)
		{
		
			curRed = curBlue = 0;
			for0(j,i+1)
			{
				if (bb[i-j][N-j-1] == 'R') curRed ++;
				else curRed = 0;
				if (bb[i-j][N-j-1] == 'B') curBlue ++;
				else curBlue = 0;
				if (curRed == K) redK = true;
				if (curBlue == K) blueK = true;
			}
		}
		if (redK && blueK)
			cout << "Case #" << (kase+1) << ": Both" << endl;
		else if (redK)
			cout << "Case #" << (kase+1) << ": Red" << endl;
		else if (blueK)
			cout << "Case #" << (kase+1) << ": Blue" << endl;
		else
			cout << "Case #" << (kase+1) << ": Neither" << endl;
	}
	
}
