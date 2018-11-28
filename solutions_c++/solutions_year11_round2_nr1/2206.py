// Problem A round 1B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdafx.h"
#include <stdio.h>
#include <assert.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <stack>
#include <string>
#include <queue>
#include <set>
#include <algorithm>
#include <iterator>
#include <map>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define Sz 101

#define fo(x,y) for (x =1; x<= y ; x++)
#define fon(x,y) for (x=y ; x>=1; x--)
#define my_set(x) memset(x,0,sizeof(x));


int main()
{
	int
		num_of_cases,
		num_of_teams,
		index1,
		index2,
		index3,
		index4;

	double 
		sum_tmp,
		num_of_games,
		wp,
		owp,
		oowp;

	double 
		NCAA[Sz][Sz];

	int
		NCAA_orig[Sz][Sz];
	string 
		tmp_str;
	char
		tmp_char;

	string file_name("input_2.txt");
	ofstream output("out_2.txt");
	ifstream input(file_name.c_str());

	
	input>>num_of_cases;

	for (index1 = 1; index1 <= num_of_cases; index1++)
	{
		output<<"Case #"<<index1<<":\n";
		my_set(NCAA);
		my_set(NCAA_orig);
		input>>num_of_teams;
		for (index2 = 1; index2 <= num_of_teams; index2++)
		{
			input>>tmp_str;
			
			for(index3 = 0; index3 <num_of_teams; index3++)
			{
				switch (tmp_str[index3])
				{
				case '1':
					NCAA_orig[index2][index3+1] = 1;
					break;
				case '0':
					NCAA_orig[index2][index3+1] = 2;
					break;
				case '.':
					NCAA_orig[index2][index3+1] = 3;
					break;
				default:
					break;
				}
			}
		}

		cout<<endl;
		for (index2 = 1; index2 <= num_of_teams; index2++)
		{

			sum_tmp = 0;
			num_of_games = 0;
			
			for(index3 = 1; index3 <= num_of_teams; index3++)
			{
				switch (NCAA_orig[index2][index3])
				{
				case 1:
					sum_tmp++;
					num_of_games++;
					break;
				case 2:
					num_of_games++;
					break;
				case 3:
					break;
				default:
					break;
				}
			}
			NCAA[index2][0] = sum_tmp/num_of_games;
			NCAA[index2][1] = num_of_games;
			NCAA[index2][2] = sum_tmp;
		}

		for (index2 = 1; index2 <= num_of_teams; index2++)
		{
			
			
			for(index3 = 1; index3 <= num_of_teams; index3++)
			{
				if (index2==1 && index3 == 3)
				{}
				if (NCAA_orig[index2][index3]<=2)
				{
					NCAA[index2][3] += (NCAA[index3][2] - (NCAA_orig[index3][index2]%2)) / (NCAA[index3][1]-1);  
				}
			}
			NCAA[index2][4] = NCAA[index2][3] / NCAA[index2][1];
		}

		for (index2 = 1; index2 <= num_of_teams; index2++)
		{
			
			
			for(index3 = 1; index3 <= num_of_teams; index3++)
			{
				if (NCAA_orig[index2][index3]<=2)
				{
					NCAA[index2][5] += NCAA[index3][4];  
				}
				
			}
			NCAA[index2][6] = NCAA[index2][5]/NCAA[index2][1];

			output<<( (0.25 * NCAA[index2][0]) + (0.5 * NCAA[index2][4]) + (0.25 * NCAA[index2][6]))<<endl;
			
		}



	}

	return 0;
}

