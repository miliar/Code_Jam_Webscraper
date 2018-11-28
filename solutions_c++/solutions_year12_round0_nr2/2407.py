// Google Code Jam - Qualification Round 2012 - Problem B. Dancing With the Googlers

#include "stdafx.h"
#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
	int T;
	cin >> T;

	for(int i=1; i<=T; i++)
	{
		int N, S, p;
		cin >> N;
		cin >> S;
		cin >> p;

		int y = 0;

		for(int j=0; j<N; j++)
		{
			int t;
			cin >> t;

			int avg = t/3;
			int rest = t%3;

			// t = 3*avg + rest
			//
			// Max bast in 'normal' case:
			//  if rest == 0 => t = avg + avg + avg         => avg
			//  if rest == 1 => t = avg + avg + (avg+1)     => avg+1
			//  if rest == 2 => t = avg + (avg+1) + (avg+1) => avg+1
			// Max best in surprising case:
			//  if rest == 0 => t = avg-1 + avg + avg+1     => avg+1 -- Need to check avg-1 > 0
			//  if rest == 1 => t = avg + avg + (avg+2)     => avg+2
			//  if rest == 2 => t = avg + avg + (avg+2)     => avg+2
			if(avg >= p || (rest >= 1 && avg+1 >= p))
			{
				y++;
			}
			else if(S > 0)
			{
				if(rest == 0) avg += 1;
				if(rest == 2) avg += 2;
				if(avg <= t && avg >= p)
				{
					y++;
					S--;
				}
			}
		}

		cout << "Case #" << i << ": " << y << endl;
	}

	return 0;
}

