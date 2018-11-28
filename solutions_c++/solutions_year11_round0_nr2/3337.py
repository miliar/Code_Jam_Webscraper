#include<iostream>
#include<string>

using namespace std;

char comb[9][9];
bool dest[9][9];

const char EMPTY = 'e';
const int LIST_SIZE = 120;

char list[LIST_SIZE];

int enc(int base)
{
	switch(base) 
	{
		case 'Q': return 1;
		case 'W': return 2;
		case 'E': return 3;
		case 'R': return 4;
		case 'A': return 5;
		case 'S': return 6;
		case 'D': return 7;
		case 'F': return 8;
		default:
			return 0;
	}
}

void reset()
{
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			comb[i][j] = EMPTY;
			dest[i][j] = false;
		}
	}
	
	for (int i = 0; i < LIST_SIZE; i++)
		list[i] = EMPTY;
}


int main()
{
	int t;
	cin >> t;

	for (int tc = 0; tc < t; tc++)
	{
		reset();

		int c;
		cin >> c;

		//Combinations
		for (int i = 0; i < c; i++)
		{
			char el[3];
			cin >> el[0] >> el[1] >> el[2];
			comb[enc(el[0])][enc(el[1])] = el[2];
			comb[enc(el[1])][enc(el[0])] = el[2];
		}

		int d;
		cin >> d;
		for (int i = 0; i < d; i++)
		{
			char el[2];
			cin >> el[0] >> el[1];
			dest[enc(el[0])][enc(el[1])] = true;
			dest[enc(el[1])][enc(el[0])] = true;
		}

		int n;
		cin >> n;

		int list_index = 0;

		for (int i = 0; i < n; i++)
		{
			cin >> list[list_index];

			if (list_index > 0)
			{
				char c = comb[enc(list[list_index])][enc(list[list_index-1])];
				if (c != EMPTY)
				{
					list[list_index-1] = c;
					list[list_index] = EMPTY;
					list_index--;
				}
				else 
				{
					for  (int j = 0; j < list_index; j++)
					{
						if (dest[enc(list[list_index])][enc(list[j])])
						{
							for (int l = 0; l <= list_index; l++)
							{
								list[l] = EMPTY;
							}
							list_index = -1;
							break;
						}
					}
				}
			}

			list_index++;
		}

		//Output
		cout << "Case #" << (tc+1) << ": [";

		for (int i = 0; i < list_index; i++)
		{
			if (i != 0)
				cout << ", ";

			cout << list[i];
		}

		cout << "]" << endl;
	}
	return 0;
}

