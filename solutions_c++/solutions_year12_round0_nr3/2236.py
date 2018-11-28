//============================================================================
// Name        : GoogleQualification-C.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string.h>
using namespace std;

struct returnvalue {
	char str[10];
};

long int int_char(char str[]);
returnvalue char_int(long int num);
bool check(long int num1, long int num2, long int start, long int end);
bool check_distinct(long int array[], int num_list, long int new_num);

int main() {
	long int distinct_number[10];
	int num_list_distinct;
	int testcase;
	char A[20];
	int B;
	char mask_A[20];
	int A_int, B_int;
	int len;
	int count;
	int n = 0;

	cin >> testcase;

	for(int i = 0; i < testcase; i++)
	{
		count = 0;
		cin >> A_int >> B_int;
		for(long int j = A_int; j <= B_int; j++)
		{
			strcpy(A,char_int(j).str);
			len = strlen(A);
			num_list_distinct = 0;
			for(int k = 1; k < len; k++)
			{
				strcpy(mask_A,A);
				for(int m = len - 1; m >= 0; m--)
					mask_A[m + k] = mask_A[m];

				n = 0;
				for(int m = len; m < len + k; m++)
					mask_A[n++] = mask_A[m];
				mask_A[len] = '\0';

				B = int_char(mask_A);

				if(check(j, B, A_int, B_int))
				{
					if(check_distinct(distinct_number, num_list_distinct, B))
					{
						count++;
						distinct_number[num_list_distinct++] = B;
					}
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << count << "\n";
	}

	return 0;
}

long int int_char(char str[])
{
	int num = 0;
	for(int i = 0; str[i]; i++)
		num = (num * 10) + (str[i] - '0');

	return num;
}

returnvalue char_int(long int num)
{
	char sttr[10];
	returnvalue stt;
	int i = 0;
	while(num)
	{
		sttr[i] = (num % 10) + '0';
		num /= 10;
		i++;
	}
	sttr[i] = '\0';
	stt.str[i] = '\0';

	i--;

	for(int j = 0; sttr[j]; j++)
		stt.str[i--] = sttr[j];

	return stt;
}

bool check(long int num1, long int num2, long int start, long int end)
{
	bool test = true;
	if((num1 < start) || (num2 < start))
		test = false;
	if((num1 > end) || (num2 > end))
		test = false;
	if(num2 <= num1)
		test = false;

	return test;
}

bool check_distinct(long int array[], int num_list, long int new_num)
{
	bool test = true;
	for(int i = 0; i < num_list; i++)
		if(array[i] == new_num)
		{
			test = false;
			break;
		}

	return test;
}
