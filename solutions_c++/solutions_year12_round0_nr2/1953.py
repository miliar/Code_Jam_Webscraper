#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef unsigned int uint;
typedef unsigned long ulong;

bool descending(uint, uint);

int main()
{
	uint T, N, S, p, t_i, pass;
	vector<uint> point;
	
	ios_base::sync_with_stdio(false);
	
	/* Max score in not surprised triplet */
	//                         0  1  2  3  4  5  6  7  8  9
	uint max_no_surprise[] = { 0, 1, 1, 1, 2, 2, 2, 3, 3, 3,
	
	//                        10 11 12 13 14 15 16 17 18 19
	                           4, 4, 4, 5, 5, 5, 6, 6, 6, 7,
							   
	//                        20 21 22 23 24 25 26 27 28 29 30
	                           7, 7, 8, 8, 8, 9, 9, 9,10,10,10 };

	/* Max score in surprised triplet */
    //                         0  1  2  3  4  5  6  7  8  9
    uint max_surprise[]    = { 0, 0, 2, 2, 2, 3, 3, 3, 4, 4,
	
	//                        10 11 12 13 14 15 16 17 18 19
	                           4, 5, 5, 5, 6, 6, 6, 7, 7, 7,
							   
    //                        20 21 22 23 24 25 26 27 28 29 30
	                           8, 8, 8, 9, 9, 9,10,10,10, 0, 0 };

	/* Read number of cases */
	cin >> T;
	
	/* For each case, */
	for (uint t = 1; t <= T; ++t)
	{
		/* Initially no one pass */
		pass = 0;
		
		/* Clear the point vector */
		point.clear();
		
		/* Read the number of Googlers */
		cin >> N;
		
		/* Read the number of surprising triplet scores */
		cin >> S;
		
		/* Read the total point threshold */
		cin >> p;
		
		/* Read all score of Googlers */
		for (uint n = 0; n < N; ++n)
		{
			cin >> t_i;
			point.push_back(t_i);
		}
		
		/* Sort the score descending */
		stable_sort(point.begin(), point.end(), descending);
		
		/* For each score, */
		for (uint i = 0; i < point.size(); i++)
		{
			/* Let him pass if the score is passed */
			if (max_no_surprise[point[i]] >= p)
				pass++;
			/* But if he not pass, */
			else
			{
				/* Check for available surprise */
				if (S > 0)
				{
					/* If the surprised make him pass, decrease coupon */
					if (max_surprise[point[i]] >= p)
					{
						pass++;
						S--;
					}
				}
			}
		}
		
		/* Display the output */
		cout << "Case #" << t << ": " << pass << "\n";
	}
	
	return 0;
}

bool descending(uint a, uint b)
{
	return a > b;
}

