#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


int combineRules[26][26];
bool opposedRules[26][26];

int elementToRepresent(char x);
char representToElement(int x);

int main()
{

	ifstream input ("B-small.in");
	ofstream output ("B-small.out");
	
	int T, C, D, N;
	int t, i, j, tmp1, tmp2, tmp3, tmpSize;
	string rule1;
	string rule2;
	char token[200];
	char result[200];

	input >> T;

	for(t = 0; t < T; ++t)
	{
		//initialization
		for(i = 0; i < 26; ++i)
			for( j = 0; j < 26; ++j)
			{
				opposedRules[i][j] = false;
				combineRules[i][j] = -1;		
			}
		
		token[0] = '\0';
		result[0] = '\0';

		//process combination rule
		input >> C;
		if(C != 0)
		{
			for(j = 0; j < C; ++j)
			{
				input >> rule1;
				tmp1 = elementToRepresent(rule1[0]);
				tmp2 = elementToRepresent(rule1[1]);
				tmp3 = elementToRepresent(rule1[2]);
				
				combineRules[tmp1][tmp2] = tmp3;
				combineRules[tmp2][tmp1] = tmp3;
			}
		}

		//process opposition rule
		input >> D;
		if(D != 0)
		{
			for(j = 0; j < D; ++j)
			{
				input >> rule2;
				tmp1 = elementToRepresent(rule2[0]);
				tmp2 = elementToRepresent(rule2[1]);

				opposedRules[tmp1][tmp2] = true;
				opposedRules[tmp2][tmp1] = true;
			}
		}

		for(i = 0; i < 26; ++i)
			opposedRules[i][i] = false;

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
			result[0] = token[0];
			result[1] = '\0';

			for(i = 1; i < N; ++i)
			{
				tmpSize = strlen(result);
				result[tmpSize] = token[i];
				result[tmpSize+1] = '\0';
				tmpSize = strlen(result);

				if(tmpSize > 1)
				{
					//process the combination
					char tmpC1 = result[tmpSize-1];
					char tmpC2 = result[tmpSize-2];
					tmp1 = combineRules[elementToRepresent(result[tmpSize-2])][elementToRepresent(result[tmpSize-1])];
					if(tmp1 != -1)
					{
						result[tmpSize-2] = representToElement(tmp1);
						result[tmpSize-1] = '\0';
					}

					//process the opposition
					if(tmp1 == -1)
					{
						tmpSize = strlen(result);
						if(tmpSize > 1)
						{
							char tmpC1 = result[tmpSize-1];
							//for(j = 0; j < tmpSize-1; ++j)
							for(j = tmpSize-2; j>=0; --j)
							{
								char tmpC2 = result[j];
								bool tmpBool = opposedRules[elementToRepresent(tmpC1)][elementToRepresent(tmpC2)];
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
	
	return 0;
}

int elementToRepresent(char x)
{
	return (x - 'A');
}

char representToElement(int x)
{
	return (x + 'A');
}
