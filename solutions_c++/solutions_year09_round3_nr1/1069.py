#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <complex>
using namespace std;

//char check[36] = {'a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'};
//bool check_val[10];


int main()
{
    
	ifstream fin("A-small-attempt2.in");
	ofstream fout("output.txt");
	
	

	int tcase;
	fin >> tcase;

	string input;
	string result = "";
	string save_number = "";
	string save_alpha = "";
	int numbercount = 0;

	for(int t=1; t<=tcase;t++)
	{
		result = "";
		save_number = "";
		save_alpha = "";
		numbercount = 0;
		fin >> input;
		int strlength = input.length();

	
		for(int i=0; i<strlength; i++)
		{
			
			if(i==0)
			{
				save_alpha += input[i];
				save_number += "1";
				result = "1";
				numbercount++;
				continue;

			}

			if(save_alpha.find_first_of(input[i]) != -1)
			{
				//int a = save_alpha.at(input[i]);
				int a= save_alpha.find_first_of(input[i]);
				result += save_number[a];
			}
			else
			{
				save_alpha += input[i];
				if(numbercount == 1)
				{
					save_number += "0";
					result += "0";
					numbercount++;
				}
				else
				{
					char *b = new char[1];
					_itoa(numbercount, b, 10 );

					save_number += b[0];
					result += b[0];
					numbercount++;
		
				}
			}


		}

		long unsigned sum = 0;
		long unsigned temp = 0;
		int count = result.length();
		for(int i=0; i<count; i++)
		{
			char *b = new char[i];
			b[0] = result[i];
			int c = atoi(b);
			if(numbercount == 1) numbercount++;		
			temp = _Pow_int(numbercount, count-i-1);
			   
			sum += (temp*c);
		}
		
		fout << "Case #" << t << ": " << sum << endl;
	}
  



	return 1;
}

