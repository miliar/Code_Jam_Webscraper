// Google CodeJAM 2012
// Author: Syed Ghulam Akbar

#define _CRT_SECURE_NO_WARNINGS
#define _CRT_NONSTDC_NO_DEPRECATE

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;

int MaxNum[31];
int Surprising[31];

int Num[101];

int main() {
	int C;

	MaxNum[0] = 0;	// 0 0 0
	MaxNum[1] = 1;	// 0 0 1
	MaxNum[2] = 1;  // 0 1 1  
	MaxNum[3] = 1;	// 1 1 1
	MaxNum[4] = 2;	// 1 1 2
	MaxNum[5] = 2;	// 1 2 2
	MaxNum[6] = 2;	// 2 2 2
	MaxNum[7] = 3;	// 2 2 3
	MaxNum[8] = 3;	// 2 3 3
	MaxNum[9] = 3;	// 3 3 3
	MaxNum[10] = 4;	// 3 3 4
	MaxNum[11] = 4;	// 3 4 4
	MaxNum[12] = 4;	// 4 4 4
	MaxNum[13] = 5;	// 4 4 5
	MaxNum[14] = 5;	// 4 5 5
	MaxNum[15] = 5;	// 5 5 5
	MaxNum[16] = 6;	// 5 5 6
	MaxNum[17] = 6;	// 5 6 6
	MaxNum[18] = 6;	// 6 6 6
	MaxNum[19] = 7;	// 6 6 7
	MaxNum[20] = 7;	// 6 7 7
	MaxNum[21] = 7;	// 7 7 7
	MaxNum[22] = 8;	// 7 7 8
	MaxNum[23] = 8;	// 7 8 8
	MaxNum[24] = 8;	// 8 8 8
	MaxNum[25] = 9;	// 8 8 9
	MaxNum[26] = 9;	// 8 9 9
	MaxNum[27] = 9;	// 9 9 9
	MaxNum[28] = 10;// 9 9 10
	MaxNum[29] = 10;// 9 10 10
	MaxNum[30] = 10;// 10 10 10

	Surprising[0] = 0;	// 0 0 0
	Surprising[1] = 1;	// 0 0 1
	Surprising[2] = 2;  // 0 0 2  
	Surprising[3] = 2;	// 0 1 2
	Surprising[4] = 2;	// 1 1 2
	Surprising[5] = 3;	// 1 1 3
	Surprising[6] = 3;	// 1 2 3
	Surprising[7] = 3;	// 2 2 3
	Surprising[8] = 4;	// 2 2 4
	Surprising[9] = 4;	// 2 3 4
	Surprising[10] = 4;	// 3 3 4
	Surprising[11] = 5;	// 3 3 5
	Surprising[12] = 5;	// 3 4 5
	Surprising[13] = 5;	// 4 4 5
	Surprising[14] = 6;	// 4 5 5
	Surprising[15] = 6;	// 5 5 5
	Surprising[16] = 6;	// 5 5 6
	Surprising[17] = 7;	// 5 6 6
	Surprising[18] = 7;	// 6 6 6
	Surprising[19] = 7;	// 6 6 7
	Surprising[20] = 8;	// 6 7 7
	Surprising[21] = 8;	// 7 7 7
	Surprising[22] = 8;	// 7 7 8
	Surprising[23] = 9;	// 7 8 8
	Surprising[24] = 9;	// 8 8 8
	Surprising[25] = 9;	// 8 8 9
	Surprising[26] = 10;// 8 9 9
	Surprising[27] = 10;// 9 9 9
	Surprising[28] = 10;// 9 9 10
	Surprising[29] = 11;// 9 9 11
	Surprising[30] = 11;// 9 10 11

	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	scanf("%d",&C);
	string input;

	for (int test=1;test<=C;test++) {
		int N, S, maxScore;

		cin >> N >> S >> maxScore;
		int result=0, max;

		for (int i=0; i<N; i++)
			cin >> Num[i];

		// Sort the results
		std::sort(Num, Num+N);

		for (int i=0; i<N; i++)
		{
			/*
			max = 0;

			if (Num[i] < 3)
				max = 1;
			else if (Num[i] % 3 == 0)
				max = Num[i] / 3;
			else
				max = Num[i] / 3 + ((Num[i] % 3 == 2) ? 1 : 0) ;

			if (max + 1 >= maxScore && S > 0 && max > 1 && Num[i] > 1 )
				max += (S-- > 0) ? 1 : 0;
			*/

			if (S > 0 && Surprising[Num[i]] >= maxScore)
			{
				S--;
				max = Surprising[Num[i]];
			}
			else
				max = MaxNum[Num[i]];

			if (max >= maxScore)
				result++;
		}

		// Set the answer depending on the found state
		cout << "Case #" << test << ": " << result << endl;
	}

	fclose( out );
}