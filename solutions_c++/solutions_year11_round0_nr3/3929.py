#pragma once

#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <list>
#include <string.h>
#include <fstream>

using namespace std;


int main()
{
	int test_count=0, i, j, k, num, num_flag=0, total_sum, divide_sum, sum, result_flag, max_sum;
	int no_test, pos1, pos2, result_sum, real_sum;
	char *str, *result;
	str = new char[8096];
	result = new char[256];

	vector <int> input;
	vector <int> bin_a;
	vector <int> bin_b;
	vector <int> bin_c;

	//string input, output;
	ifstream in("input.txt");
	ofstream out("output.txt");


	if(!in) 
		cout << "Cannot open input file.\n";

	

	while(in) 
	{
		in.getline(str, 8095);  
		
		if(in) 
		{
			input.clear();

			if (test_count == 0)
			{
				no_test = atoi(str);
			}

			else
			{
				result_flag = 0;
				max_sum = -9999;
				total_sum = result_sum = divide_sum = real_sum = 0;
				if (num_flag == 0)
				{
					num = atoi(str);
					num_flag = 1;
				}
				else
				{
					num_flag = 0;
					result = strtok( str, " ");
					input.push_back(atoi(result));

					for (i=1 ; i<num ; i++)
					{
						result = strtok( NULL, " ");
						input.push_back(atoi(result));
					}	

					for (i=0 ; i<num ; i++)
					{
						total_sum ^= input.at(i);
						real_sum += input.at(i);
					}

					if (total_sum == 0)
					{
						result_flag = 1;
					}

					if (result_flag == 1)
					{
						result_flag = 0;
						i = 0;
						while (i<num)
						{
							divide_sum = result_sum = 0;
							sum = input.at(i);

							for (pos1 = i-1 ; pos1 >= 0 ; pos1--)
									divide_sum ^= input.at(pos1);

							for (pos2 = i+1 ; pos2 < num ; pos2++)
								divide_sum ^= input.at(pos2);

							if (sum  == divide_sum)
							{
								pos1 = i;
								pos2 = i;
								result_flag = 1;

								for (k=pos1 ; k<=pos2 ; k++)
									result_sum += input.at(k);

								result_sum = (result_sum >= (real_sum-result_sum)?result_sum:(real_sum-result_sum));

								max_sum = (result_sum >= max_sum)?result_sum:max_sum;
									
							}

							for (j=i+1 ; j<num ; j++)
							{
								sum ^= input.at(j);
								divide_sum = result_sum = 0;

								for (pos1 = i-1 ; pos1 >= 0 ; pos1--)
									divide_sum ^= input.at(pos1);

								for (pos2 = j+1 ; pos2 < num ; pos2++)
									divide_sum ^= input.at(pos2);


								if (sum  == divide_sum && (j-i+1) != num)
								{
									pos1 = i;
									pos2 = j;
									result_flag = 1;

									for (k=pos1 ; k<=pos2 ; k++)
										result_sum += input.at(k);

									result_sum = (result_sum >= (real_sum-result_sum)?result_sum:(real_sum-result_sum));

									max_sum = (result_sum >= max_sum)?result_sum:max_sum;
									
								}
							}
							i++;
						}
						
					}



				}
			}

			


			if (test_count > 0 && num_flag == 0)
			{
				out << "Case #" << test_count << ": ";

				if (result_flag == 0)
					out << "NO\n";
				else
					out << max_sum << endl;
				
				test_count++;
			}

			if (test_count == 0)
				test_count++;

			
		}
		
	}

in.close();

return 0;
}