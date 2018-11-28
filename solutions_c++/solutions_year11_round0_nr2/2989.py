#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


int combine[26][26];
bool opposed[26][26];

int cToi(char x)
{
	/*
	if( x == 'Q')
		return 0;
	else if( x == 'W')
		return 1;
	else if( x == 'E' )
		return 2;
	else if( x == 'R' )
		return 3;
	else if( x == 'A' )
		return 4;
	else if( x == 'S' )
		return 5;
	else if( x == 'D' )
		return 6;
	else if( x == 'F' )
		return 7;
	else
		return (x - 'A');
		*/
	return (x - 'A');

}

char iToc(int x)
{
	/*
	if( x == 0 )
		return 'Q';
	else if( x == 1 )
		return 'W';
	else if( x == 2 )
		return 'E';
	else if( x == 3 )
		return 'R';
	else if( x == 4 )
		return 'A';
	else if( x == 5 )
		return 'S';
	else if( x == 6 )
		return 'D';
	else if( x == 7 )
		return 'F';
	else
		return (x + 'A');
		*/
	return (x + 'A');
}




int main()
{

	ifstream input ("B-large.in");
	if(!input.is_open())
	{	
		cout << "error to open input file" << endl;
		return -1;
	}

	ofstream output ("B-large.out");
	if(!output.is_open())
	{
		cout << "unable to create the output file" << endl;
		return -1;
	}
	
	int T, C, D, N;
	int t, i, j, tmp1, tmp2, tmp3, tmpSize;
	string combineRule;
	string opposedRule;
	char token[200];
	char result[200];
	bool tokenFlag[26];
	//vector<char> result;

	input >> T;

	for(t = 0; t < T; ++t)
	{
		

		//initialization
		for(i = 0; i < 26; ++i)
			for( j = 0; j < 26; ++j)
			{
				opposed[i][j] = false;
				combine[i][j] = -1;		
			}
		for(i = 0; i < 26; ++i)
			tokenFlag[i] = false;
		
		token[0] = '\0';
		result[0] = '\0';

		//process combination rule
		input >> C;
		if(C != 0)
		{
			for(j = 0; j < C; ++j)
			{
				input >> combineRule;
				tmp1 = cToi(combineRule[0]);
				tmp2 = cToi(combineRule[1]);
				tmp3 = cToi(combineRule[2]);
				
				combine[tmp1][tmp2] = tmp3;
				combine[tmp2][tmp1] = tmp3;
			}
		}

		//process opposition rule
		input >> D;
		if(D != 0)
		{
			for(j = 0; j < D; ++j)
			{
				input >> opposedRule;
				tmp1 = cToi(opposedRule[0]);
				tmp2 = cToi(opposedRule[1]);

				opposed[tmp1][tmp2] = true;
				opposed[tmp2][tmp1] = true;
			}
		}

		for(i = 0; i < 26; ++i)
			opposed[i][i] = false;

		//process the string
		input >> N;
		input >> token;
		
		output << "Case #" << t+1 << ": " << "[" ;
		if (C == 0 && D == 0)
		{
			for( i = 0; i < N - 1; ++i)
				output << token[i] << ", ";
			output << token[i] << "]" << endl;
		}
		else
		{
			//result.push_back(token[0]);
			result[0] = token[0];
			result[1] = '\0';

			for(i = 1; i < N; ++i)
			{

				//result.push_back(token[i]);
				//tmpSize = result.size();
				tmpSize = strlen(result);
				result[tmpSize] = token[i];
				result[tmpSize+1] = '\0';
				tmpSize = strlen(result);

				if(tmpSize > 1)
				{
					//process the combination
					char tmpC1 = result[tmpSize-1];
					char tmpC2 = result[tmpSize-2];
					tmp1 = combine[cToi(result[tmpSize-2])][cToi(result[tmpSize-1])];
					if(tmp1 != -1)
					{
						result[tmpSize-2] = iToc(tmp1);
						result[tmpSize-1] = '\0';
						//result.pop_back();
					}

					//process the opposition
					if(tmp1 == -1)
					{
						tmpSize = strlen(result);
						if(tmpSize > 1)
						{
							char tmpC1 = result[tmpSize-1];
							for(j = 0; j < tmpSize-1; ++j)
							//for(j = tmpSize-2; j>=0; --j)
							{
								char tmpC2 = result[j];
								bool tmpBool = opposed[cToi(tmpC1)][cToi(tmpC2)];
								if(tmpBool)
								{
									result[0] = '\0';
									break;
								}
							}
						}
					}

				}

			}
			
			tmpSize = strlen(result);
			if(tmpSize == 0)
				output << "]" << endl;
			else
			{
				for( i = 0; i < tmpSize - 1; ++i)
					output << result[i] << ", ";
				output << result[i] << "]" << endl;
			}
		}

	}
	
	system("pause");
	return 0;
}