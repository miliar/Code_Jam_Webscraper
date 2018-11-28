#include <iostream>
#include <fstream>
#include <string>

using namespace std;
char code(char);
void main()
{
	string infile ="test.in";
	string outfile = "output3.txt";
	int N;
	int T;
	int surprise;
	int surcount = 0;
	int maxcount = 0;
	bool flag = true;
	int p;
	int a[100];
	int b[300];
	int max;
	int maxindex;

	ifstream source;
	ofstream target;

	source.open(infile.c_str());
	target.open(outfile.c_str());

	source >> T;
	for ( int z =0; z <T; z++)
	{
		maxindex = -1;
		max =0;
		maxcount = 0;
		surcount = 0;
		source >> N;
		source >> surprise;
		source >> p;
		for ( int i =0; i < N; i++)
		{
			source >> a[i];
		}

		int j =0;
		for ( int h =0; h <N; h++)
		{
			b[j] = a[h] / 3;
			b[j+1] = (a[h] - b[j]) / 2;
			b[j+2] = a[h] - b[j] - b[j+1];
			if (( b[j+2] >= p) || ( b[j+1] >= p) || ( b[j] >= p) )
			{
				maxcount++;
				flag = false;
			}

			if ( b[j] >= max)
			{
				max = b[j];
				maxindex = j;
			}
			if ( b[j+1] >= max)
			{
				max = b[j+1];
				maxindex = j+1;
			}
			if ( b[j+2] >= max)
			{
				max = b[j+2];
				maxindex = j+2;
			}
				
			
		/*

			if (( surcount < surprise) && ( maxcount < 3) )
			{
				if (( abs(double(b[j] - p)) <= 1 ) || ( abs(double(b[j+1] - p)) <= 1 ) || ( abs(double(b[j+2] - p)) <= 1 ))  
					if( ( b[j+2] != 10) && ( b[j] != 10) && ( b[j+1] != 10) && ( b[j+2] != p) && ( b[j] != p) && ( b[j+1] != p) && ( b[j+2] != 0) && ( b[j] != 0) && ( b[j+1] != 0))
					{
						//b[j+1] = b[j+1] - 1;
						//b[j+2 ] = b[j+2] + 1;
						maxcount++;
						surcount++;
					}
				}
		
		*/
			//( (abs(double((b[j+2]-b[j+1]))) + 1 <= 1) && (abs(double((b[j]-b[j+1]))) + 1 <= 1) && (abs(double((b[j]-b[j+2]))) + 1 <= 1) )
			if (( surcount < surprise) && ( maxcount < 3) )
				if ( abs(double((a[h] / 3)-p)) <= 2 && flag && ( b[j+2] != 0) && ( b[j] != 0) && ( b[j+1] != 0) && ( b[j+2] != 10) && ( b[j] != 10) && ( b[j+1] != 10))
				{
					if ( b[j] + 1 >= p || b[j+1]+1 >=p || b[j+2]+1 >= p )
						if (( b[j] == float((b[j+1]+ max))/2) || (b[j] == float((b[j+2] + max))/2) || (b[j+1] == float((b[j+2] + max ))/2))
							maxcount++;
					surcount++;
				}
			flag = true;
			j += 3;
			max = 0;
		}
		

		/*
			for ( int d =0; d < 3*N; d++)
		{
			if ( ( b[d] >=p) || ( b[d+2] >=p) || ( b[d+1] >=p) )
				maxcount++;
			d++;
			d++;
		}	
		*/

		target << "Case #" << z+1 << ": " << maxcount << endl;
		
		
		for ( int l = 0; l < 100; l++)
			a[l] = -1;
		for (int k = 0; k < 300; k++)
			b[k] = -1;
			
	}
	system("pause");

}

