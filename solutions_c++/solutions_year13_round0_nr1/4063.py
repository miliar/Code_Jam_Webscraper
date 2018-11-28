
#include <iostream>
#include <string.h>
#include <memory.h> 
#include <fstream>
		  using namespace std;

char chesses2[17];
bool flag_array[17];
bool min_flag_array[17];

//   1  2  3  4
//   5  6  7  8
//   9 10 11 12
//  13 14 15 16

static int min_flip_count = 17;
int swap_handle(char &chess)
{
	if (chess == '-')
	{
		chess = '+';
		return 1;
	}
	else if(chess == '+')
	{
		chess = '-';
		return 10;
	}
	return 100;
}

int flip2(int k, char *chesses, bool *flag_array)
{
	int b_inc_count = 0;
	//   1  2  3  4
	//   5  6  7  8
	//   9 10 11 12
	//  13 14 15 16
	swap_handle(chesses[k]);
	swap_handle(chesses[k%4]);
	swap_handle(chesses[k%4 + 4]);
	swap_handle(chesses[k%4 + 8]);
	swap_handle(chesses[k%4 + 12]);
	if (k%4 == 0)
	{
		swap_handle(chesses[16]);
	}

	swap_handle(chesses[(k - 1)/4*4 + 1]);
	swap_handle(chesses[(k - 1)/4*4 + 2]);
	swap_handle(chesses[(k - 1)/4*4 + 3]);
	swap_handle(chesses[(k - 1)/4*4 + 4]);
	flag_array[k] = true;
	return 0;
}

bool check_all_b2(char *chesses)
{
	bool flag = true;
	//   1  2  3  4
	//   5  6  7  8
	//   9 10 11 12
	//  13 14 15 16
	for (int i = 1; i != 17; i++)
	{
		if (chesses[i]  != '-')
		{
			flag = false;
			break;
		}
	}
	return flag;
}

bool check_all_bool_array(bool *flag_array)
{
	bool flag = true;
	for (int i = 1; i != 17; i++)
	{
		if (flag_array[i] == false)
		{
			flag = false;
			break;
		}
	}
	return flag;
}

inline int process2(int start, int flip_count, char *chesses1, bool *flag_array1)
{
	if(flip_count < min_flip_count)
	{
		for (int i = start; i != 17; i++)
		{
			if (flag_array1[i] == false)
			{
				char chesses[17];
				bool flag_array[17];
				memcpy(chesses, chesses1, sizeof(chesses));
				memcpy(flag_array, flag_array1, sizeof(flag_array));
				flip2(i, chesses, flag_array);
				if (check_all_b2(chesses))
				{
					if(min_flip_count > flip_count)
					{
						min_flip_count = flip_count;
						memcpy(min_flag_array, flag_array, sizeof(flag_array));
					}
					return 0;
				} 
				else
					process2(i, flip_count + 1, chesses, flag_array);
			}
		}
	}
	return 0;
}



//   1  2  3  4
//   5  6  7  8
//   9 10 11 12
//  13 14 15 16


char is_equal(int i, int j, int k, int l)
{
	if((chesses2[i] + chesses2[j] + chesses2[k] + chesses2[l]) == 88*4 || ((chesses2[i] + chesses2[j] + chesses2[k] + chesses2[l]) == 88*3 + 84))
		return 'X';

	else if((chesses2[i] + chesses2[j] + chesses2[k] + chesses2[l]) == 79*4 || ((chesses2[i] + chesses2[j] + chesses2[k] + chesses2[l]) == 79*3 + 84))
		return 'O';

	else
		return 'd';
}

char check_one_chess(int i)
{
	char result = 'd';
	result = is_equal(i%4, i%4 + 4, i%4 + 8, i%4 + 12);
	if(result != 'd')
		return result;

	result = is_equal((i - 1)/4*4 + 1, (i - 1)/4*4 + 2, (i - 1)/4*4 + 3, (i - 1)/4*4 + 4);
	if(result != 'd')
		return result;
}

char judge()
{
	char result = 'd';
	for (int i = 1; i < 17; i = i + 5)
	{
		if (chesses2[i] != '.')
		{
			result = check_one_chess(i);
			if(result != 'd')
				return result;
		}
	}
	result = is_equal(1, 6, 11, 16);
	if(result != 'd')
		return result;

	result = is_equal(4, 7, 10, 13);
	if(result != 'd')
		return result;

	return result;
}

int main()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("A-small-attempt0.in");
	outFile.open("A-small-attempt0.out");
	int num_cases;
	inFile>>num_cases;
	char a;		
	inFile.get(a);

	for (int j = 1; j <= num_cases; j++)
	{
		for (int i = 0; i != 4; i++)
			inFile.getline(chesses2 + i*4 + 1, 5);

		char result = judge();
		outFile<<"Case #"<<j<<": ";
		if (result == 'X' || result == 'O')
			outFile<<result<<" won\n";	
		else
		{
			for (int k = 1; k < 17; k++)
			{
				if (chesses2[k] == '.')
				{
					outFile<<"Game has not completed\n";
					break;
				}
				
			}
			outFile<<"Draw\n";
		}
		if(j != num_cases)
			inFile.get(a);
	}
	return 0;
}


