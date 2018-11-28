#include <fstream>

using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("B-large.in");
	out.open("B-large.out");

	int NUM_OF_CASES, NUM_OF_INT, NUM_OF_SURP, BEST_SCORE;
	int var, max, min;
	int count_above_best, count_in_surp;

	//read in
	in >> NUM_OF_CASES;
	for( int i = 0; i < NUM_OF_CASES; i++ )
	{
		in >> NUM_OF_INT >> NUM_OF_SURP >> BEST_SCORE;
		out << "Case #" << i + 1 << ": ";

		count_above_best = count_in_surp = 0;

		//calculate scope
		if( BEST_SCORE >=2 )
		{
			max = 3 * BEST_SCORE - 2;
			min = max - 2;

			for( int j = 0 ; j < NUM_OF_INT; j ++ )
			{
				in >> var;
				if( var >= max )
				{
					count_above_best ++ ;
				}else if( var >= min )
				{
					count_in_surp ++;
				}
			}

			//output
			if( NUM_OF_SURP > count_in_surp )
			{
				out << count_above_best + count_in_surp << endl;
			}else
			{
				out << count_above_best + NUM_OF_SURP << endl;
			}
		}else
		{
			//BEST_SCORE <= 1
			for( int j = 0 ; j < NUM_OF_INT; j ++ )
			{
				in >> var;
				if( var >= BEST_SCORE )
				{
					count_above_best ++ ;
				}
			}
			out << count_above_best << endl;
		}
	}

	out.close();
	in.close();
	return 0;
}