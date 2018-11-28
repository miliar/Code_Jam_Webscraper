#include <fstream>
#include <iostream>

using namespace std;


long long count_ugly(string digits_in_string, int factor)
{
	int i, j, k;
	int mod;
	int n;
	int digits[40];
	long long table[40][210];
	long long num;
	long long last_num, pos;
	
	
	//initialize
	n = digits_in_string.length();
	for(i = 0; i < n; i++)
		digits[i] = (int)(digits_in_string[i] - '0');
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < factor; j++)
		{
			table[i][j] = 0;
		}	
	}

	num = 0;
	for(i = 0; i < n; i++)
	{
		num = num * 10 + digits[i];
		table[i][num % factor] = 1;

		pos = 1;
		last_num = 0;
		for(j = i; j > 0; j--)
		{
			last_num += pos * digits[j];
			pos *= 10;
			mod = last_num % factor;
			for(k = 0; k < factor; k++)
			{
				table[i][k] += table[j - 1][(factor - mod + k) % factor];
				table[i][k] += table[j - 1][(factor + mod + k) % factor];
			}
			
		}
	}
	cout << digits[0] << " " << table[0][0] << endl;
	return table[n - 1][0];
}

int main()
{
	ifstream fin("problemB.in");
	ofstream fout("problemB.out");
	
	int test_case;
	int num_test_cases;
	
	string digits;
	long long solution;
	fin >> num_test_cases;
	for(test_case = 1; test_case <= num_test_cases; test_case++)
	{
		fin >> digits;
		solution = 0;
		solution += count_ugly(digits, 2);
		cout << "2: " << count_ugly(digits, 2) << endl;
		solution += count_ugly(digits, 3);
		cout << "3: " << count_ugly(digits, 3) << endl;
		solution += count_ugly(digits, 5);
		cout << "5: " << count_ugly(digits, 5) << endl;
		solution += count_ugly(digits, 7);
		cout << "7: " << count_ugly(digits, 7) << endl;
		
		solution -= count_ugly(digits, 6);
		//cout << count_ugly(digits, 6) << endl;
		solution -= count_ugly(digits, 10);
		//cout << count_ugly(digits, 10) << endl;
		solution -= count_ugly(digits, 14);
		//cout << count_ugly(digits, 14) << endl;
		solution -= count_ugly(digits, 15);
		//cout << count_ugly(digits, 15) << endl;
		solution -= count_ugly(digits, 21);
		//cout << count_ugly(digits, 21) << endl;
		solution -= count_ugly(digits, 35);
		//cout << count_ugly(digits, 35) << endl;
		
		solution += count_ugly(digits, 30);
		//cout << count_ugly(digits, 30) << endl;
		solution += count_ugly(digits, 42);
		//cout << count_ugly(digits, 42) << endl;
		solution += count_ugly(digits, 70);
		//cout << count_ugly(digits, 70) << endl;
		solution += count_ugly(digits, 105);
		//cout << count_ugly(digits, 105) << endl;
		
		
		solution -= count_ugly(digits, 210);
		cout << count_ugly(digits, 210) << endl;
		
		fout << "Case #" << test_case << ": " << solution << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}