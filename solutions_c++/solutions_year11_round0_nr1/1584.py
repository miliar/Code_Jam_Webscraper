#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <sstream>
#include <stack>
#include <vector>

#include <limits.h>
#include <math.h>
#include <stdio.h>

using namespace std;

#define foreach(k, b, N) for (int k = b; k <= N; k++)
#define foreach_r(k, b, N) for (int k = b; k >= N; k--)

int
main()
{
	int cases; 
	int result = 0;
	int B[150];
	int O[150];
	int order[150];
	int color[150]; // O = 0, B = 1;

	cin >> cases;

	foreach(i, 1, cases) {
		string tmp;

		getline(cin, tmp);
		istringstream ss(tmp);

		int N;	
		cin >> N;

		memset(B, 0, sizeof(B));
		memset(O, 0, sizeof(O));
		memset(order, 0, sizeof(order));
		memset(color, 0, sizeof(color));

		int rcount = 0;
		int ocount = 0;
		int count = 0;

		foreach(j, 0, N - 1) {
			string c;
			int val;

			cin >> c;
			cin >> val;

			if (c.compare("B") == 0) {
				B[rcount++] = val;
				color[j] = 1;
			}
			else
				O[ocount++] = val;
			
			order[count++] = val;
		}

		result = 0;
		int k = 0; // O
		int l = 0; // B
		int turn = color[0];
		int prev_turn = color[0];
		int avail = 0;
		foreach(j, 0, N - 1) {
			int t = 0;
			turn = color[j];
			
			if (turn == 0) {
				int pval = (k == 0) ? 1 : O[k - 1];
				
				if (prev_turn != turn) {
					if (abs(order[j] - pval) <= avail)
						t = 1;	
					else
						t = abs(order[j] - pval) - avail + 1;
					avail = 0;
				}
				else {
					t = abs(order[j] - pval) + 1;
				}
				
				avail += t;
				result += t;
				k++;
			}
			else {
				int pval = (l == 0) ? 1 : B[l - 1];
				if (prev_turn != turn) {
					if (abs(order[j] - pval) <= avail)
						t = 1;
					else
						t = abs(order[j] - pval) - avail + 1;
					avail = 0;
				}
				else {
					t = abs(order[j] - pval) + 1;
				}
				avail += t;
				result += t;
				l++;
			}
			prev_turn = turn;
		}

		printf("Case #%d: %d\n", i, result);
	}

	return 0;
}
