#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <functional>
#include <numeric>
#include <iomanip>
using namespace std;



#define DRAW -1
#define XWON 1
#define OWON 0
#define UNFINISHED 10
int main(int argc, char * argv[])
{
	ifstream fin("input.txt"); 
	ofstream fout("output.txt");
	
	if(!fin.good())
	{
		cout << "opps" << endl;
	}
	string str;
	getline(fin, str);
	
	const int T = atoi(str.c_str());

	for( int aaa = 0; aaa < T ; aaa++)
	{
		vector<vector<char> > full_vec;

		//	Load everything!!
		istringstream iss(str);
		for (int bbb = 0 ; bbb < 4 ; ++bbb)
		{
			getline(fin, str);		iss.clear(); iss.str(str);
			vector<char> temp_vec;
			for (int ccc = 0; ccc < 4; ++ccc) 
			{
				char temp_char;
				iss >> temp_char;
				temp_vec.push_back(temp_char);
			}
			full_vec.push_back(temp_vec);
		}

		//cout << full_vec[1][1];

		bool finished = true;
		//	Check for completion.
		for (int bbb = 0; bbb < 4 ; ++bbb) 
		{
			for (int ccc = 0 ; ccc < 4 ; ++ccc)
			{
				if(full_vec[bbb][ccc] == '.')
				{
					finished = false;
				}
			}
		}


		// 	Check for X:
		//	Check rows.
		int status = DRAW;
		for (int bbb = 0; bbb < 4 ; ++bbb) 
		{
			bool complete = true;
			for (int ccc = 0 ; ccc < 4 ; ++ccc)
			{
				if(full_vec[bbb][ccc] == 'O' || full_vec[bbb][ccc] == '.')
				{
					complete = false;
					break;
				}
			}
			if (complete)
			{
				status = XWON;
				goto DONE;
			}
		}

		//	Check cols.
		for (int ccc = 0; ccc < 4 ; ++ccc) 
		{
			bool complete = true;
			for (int bbb = 0 ; bbb < 4 ; ++bbb)
			{
				if(full_vec[bbb][ccc] == 'O' || full_vec[bbb][ccc] == '.')
				{
					complete = false;
					break;
				}
			}
			if (complete)
			{
				status = XWON;
				goto DONE;
			}
		}
		// 	Check diags 1.
		{
			bool complete = true;
			for (int bbb = 0; bbb < 4 ; ++bbb) 
			{
				if(full_vec[bbb][bbb] == 'O' || full_vec[bbb][bbb] == '.')
				{
					complete = false;
					break;
				}
			}
			if (complete)
			{
				status = XWON;
				goto DONE;
			}
		}
		// 	Check diags 2.
		{
			bool complete = true;
			for (int bbb = 0; bbb < 4 ; ++bbb) 
			{
				if(full_vec[bbb][3-bbb] == 'O' || full_vec[bbb][3-bbb] == '.')
				{
					complete = false;
					break;
				}
			}
			if (complete)
			{
				status = XWON;
				goto DONE;
			}
		}




		// 	Check for Y:
		//	Check rows.
		for (int bbb = 0; bbb < 4 ; ++bbb) 
		{
			bool complete = true;
			for (int ccc = 0 ; ccc < 4 ; ++ccc)
			{
				if(full_vec[bbb][ccc] == 'X' || full_vec[bbb][ccc] == '.')
				{
					complete = false;
					break;
				}
			}
			if (complete)
			{
				status = OWON;
				goto DONE;
			}
		}

		//	Check cols.
		for (int ccc = 0; ccc < 4 ; ++ccc) 
		{
			bool complete = true;
			for (int bbb = 0 ; bbb < 4 ; ++bbb)
			{
				if(full_vec[bbb][ccc] == 'X' || full_vec[bbb][ccc] == '.')
				{
					complete = false;
					break;
				}
			}
			if (complete)
			{
				status = OWON;
				goto DONE;
			}
		}
		// 	Check diags 1.
		{
			bool complete = true;
			for (int bbb = 0; bbb < 4 ; ++bbb) 
			{
				if(full_vec[bbb][bbb] == 'X' || full_vec[bbb][bbb] == '.')
				{
					complete = false;
					break;
				}
			}
			if (complete)
			{
				status = OWON;
				goto DONE;
			}
		}
		// 	Check diags 2.
		{
			bool complete = true;
			for (int bbb = 0; bbb < 4 ; ++bbb) 
			{
				if(full_vec[bbb][3-bbb] == 'X' || full_vec[bbb][3-bbb] == '.')
				{
					complete = false;
					break;
				}
			}
			if (complete)
			{
				status = OWON;
				goto DONE;
			}
		}




		if (!finished && (status == DRAW))
		{
			status = UNFINISHED;
		}
		DONE:
		switch (status)
		{
			case DRAW:
				fout << "Case #" << aaa+1 << ": Draw\n";
				break;
			case XWON:
				fout << "Case #" << aaa+1 << ": X won\n";
				break;
			case OWON:
				fout << "Case #" << aaa+1 << ": O won\n";
				break;
			case UNFINISHED:
				fout << "Case #" << aaa+1 << ": Game has not completed\n";
				break;
		}
		getline(fin, str);		iss.clear(); iss.str(str);
		//fout << fixed << setprecision(6) << "Case #" << aaa+1 << ": " << setprecision(6) << static_cast<double>( minKey )<< setprecision(6) <<  endl;

	}	

	fin.close(); fout.close();
	return 0;
}
