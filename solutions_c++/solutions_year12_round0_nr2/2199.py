//============================================================================
// Name        : GoogleQualification-B.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdlib.h>
using namespace std;

int apart(int num1, int num2);
int check(int value1, int value2, int value3);

int main() {
	int test_case, num_googlers, num_surprising, best_result;
	int mask_num_surprising;
	int googlers[100];
	int max_count_googlers;

	cin >> test_case;
	for(int i = 0; i < test_case; i++)
	{
		cin >> num_googlers >> num_surprising >> best_result;
		for(int j = 0; j < num_googlers; j++)
			cin >> googlers[j];

		mask_num_surprising = max_count_googlers = 0;
		bool test, check_surprising;

		for(int index = 0; index < num_googlers; index++)
		{
			test = false;
			check_surprising = false;
			for(int j = best_result; j <= 10; j++)
			{
				if(j > googlers[index])
					break;
				else {
					for(int m = 0; m <= 10; m++)
					{
						if((j + m) > googlers[index])
							break;
						else {
							for(int n = 0; n <= 10; n++)
							{
								if((j + m + n) == googlers[index])
								{
									int result = check(apart(j,m), apart(j,n), apart(m,n));

									if(result == 2)
									{
										if(check_surprising == false)
										{
											max_count_googlers++;
											test = true;
											break;
										}
										else {
											mask_num_surprising--;
											test = true;
											break;
										}
									}
									else if(result == 0)
									{
										if(check_surprising == false)
										{
											max_count_googlers++;
											mask_num_surprising++;
											check_surprising = true;
										}
									}
								}
								else if((j + m + n) > googlers[index])
									break;
							}
						}
						if(test)
							break;
					}
				}
				if(test)
					break;
			}
		}

		if(mask_num_surprising > num_surprising)
			max_count_googlers = max_count_googlers - (mask_num_surprising - num_surprising);
		cout << "Case #" << i + 1 << ": " << max_count_googlers << "\n";
	}

	return 0;
}

int apart(int num1, int num2)
{
	return abs(num1 - num2);
}

int check(int value1, int value2, int value3)
{
	int test;

	if((value1 < 2) && (value2 < 2) && (value3 < 2))
		test = 2;
	else if((value1 > 2) || (value2 > 2) || (value3 > 2))
		test = 1;
	else
		test = 0;

	return test;
}
