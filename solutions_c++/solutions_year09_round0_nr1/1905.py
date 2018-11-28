#include "iostream"
#include "fstream"
#include "string"

using namespace std;

#define small_in "A-small.in"
#define small_out "A-small.out"
#define large_in "A-large.in"
#define large_out "A-large.out"

void main()
{
	int L=0, D=0, N=0;

	// Read input file
	ifstream infile;
	infile.open(large_in);
	infile >> L >> D >> N;
	string *word = new string[D];
	for(int i=0; i<D; i++)
	{
		infile >> word[i];
	}
	string *pattern = new string[N];
	for(int i=0; i<N; i++)
	{
		infile >> pattern[i];
	}
	infile.close();

	ofstream outfile;
	outfile.open(large_out);

	// Process
	for(int i=0; i<N; i++)
	{
		int K=0;
		int index=0, last_paren = -1;
		string *part = new string[L];
		bool in_paren = false;
		for(int j=0; j<(int)pattern[i].length(); j++)
		{
			if(pattern[i][j] == '(')
			{
				//if(j == last_paren + 1)
				//{
					last_paren = j;
				//}
				/*else
				{
					for(int k=last_paren+1; k<j; k++)
					{
						part[index].push_back(pattern[i][k]);
					}
					if(part[index].empty() == false)
					{
						index++;
						last_paren = j;
					}
				}*/
				in_paren = true;
			}
			else if(pattern[i][j] == ')')
			{
				for(int k=last_paren+1; k<j; k++)
				{
					part[index].push_back(pattern[i][k]);
				}
				if(part[index].empty() == false)
				{
					index++;
					last_paren = j;
				}
				in_paren = false;
			}
			else if(in_paren == false)
			{
				part[index].push_back(pattern[i][j]);
				index++;
			}
		}

		
		for(int j=0; j<D; j++)
		{
			int count = 0;
			for(int k=0; k<L; k++)
			{
				int found = part[k].find_first_of(word[j][k]) ;
				if(found != string::npos)
				{
					count ++;
				}
			}
			if(count == L)
			{
				K++;
			}
		}
		// Write to output file
		outfile << "Case #" << i+1 << ": " << K << endl;
	}
	outfile.close();
}