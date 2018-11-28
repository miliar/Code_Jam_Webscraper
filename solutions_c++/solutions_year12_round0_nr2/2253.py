#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int 
	main () 
{
	ifstream in = ifstream ("in.txt");
	ofstream out = ofstream ("out.txt");
		
	int case_count;		// 1 <= T <= 100
	int count;			// 1 <= N <= 3 or 100
	int surprise;		// 0 <= S <= N
	int best;			// 0 <= p <= 10 
	vector <int> sum;	// 0 <= i <= 30
	int result;
	int surprise_used;

	in >> case_count;

	for (int i = 1; i <= case_count; ++i)
	{
		//
		// read input
		//

		in >> count;
		in >> surprise;
		in >> best;	

		result = 0;
		surprise_used = 0;
		sum.clear ();
		sum.resize (count, 0);

		for (int j = 0; j < count; ++j) 
		{
			in >> sum [j];
		}

		//
		// compute scores achiving best result
		//

		int triplet = 3;
		for (int j = 0; j < count; ++j)
		{
			int div = sum [j] / triplet;
			int rem = sum [j] % triplet;
			
			// a < b < c < d < e < f < g by 1
			
			if (div + 2 < best)
			{
				// to low
			}

			// div = d
			// score might be d+d+d, no surprise
			else if (div >= best)
			{	
				result++;
			}

			// div = b
			// rem = 2
			// score must be b+b+d to achieve d, surprise
			else if (div + 2 == best && rem == 2 && surprise_used < surprise)
			{
				result++;
				surprise_used++;
			}

			// div = c
			// rem = 0 
			// score must be b+c+d to achieve d, surprise
			else if (div + 1 == best && div >= 1 && rem == 0 && surprise_used < surprise)
			{				
				result++;
				surprise_used++;				
			}

			// div = c
			// rem = 1
			// score must be c+c+d to achieve d, no surprise
			//
			// div = c
			// rem = 2
			// score must be c+d+d to achieve d, no surprise
			else if (div + 1 == best && rem >= 1)
			{
				result++;
			}

			else 
			{
				// too low
			}
		}

		out << "Case #" << i << ": " << result << endl;
	}

	in.close ();
	out.close ();

	system ("pause");
}
