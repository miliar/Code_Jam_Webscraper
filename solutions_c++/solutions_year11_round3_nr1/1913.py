// Problem A Round 1C.cpp : Defines the entry point for the console application.
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

#define Mx 10000

#define fo(x,y) for (x =1; x<= y ; x++)
#define fon(x,y) for (x=y ; x>=1; x--)
#define my_set(x) memset(x,0,sizeof(x));


int main()
{
	int
		num_of_cases,
		num_of_col,
		num_of_row,
		index1,
		index2,
		index3,
		index4;

	int 
		sum_tmp;
	string 
		tmp_str;
	char
		tmp_char;
	int my_mat[Sz][Sz];

	int M_stack[Mx][2];

	int M_stack_max;

	string file_name("input_2.txt");
	ofstream output("out_2.txt");
	ifstream input(file_name.c_str());

	set<pair<int,int>> S;

	vector<pair<int,int>> V;
	
	input>>num_of_cases;

	for (index1 = 1; index1 <= num_of_cases; index1++)
	{
		output<<"Case #"<<index1<<":\n";
		input>>num_of_row;
		input>>num_of_col;
		my_set(my_mat);
		my_set(M_stack);
		V.clear();
		S.clear();
		M_stack_max = 0;
		sum_tmp = 0;
		fo(index2,num_of_row)
		{
			input>>tmp_str;
			fo(index3,num_of_col)
			{
				switch (tmp_str[index3-1])
				{
				case '#':
					sum_tmp++;
					my_mat[index2][index3] = 1;
					V.push_back(make_pair(index2,index3));
					S.insert(make_pair(index2,index3));
					break;
				case '.':
					break;
				default:
					break;
				}
			}

		}
		
		if (sum_tmp % 4)
		{
			output<<"Impossible\n";
		}
		else
		{
			bool tmp_flag = true;
			int tmp_size = V.size();
			for(index4 = 0; index4<tmp_size; index4++)
			{
				if(S.find(V[index4])!=S.end())
				{
					if(S.find(V[index4])!=S.end() && S.find(make_pair(V[index4].first+1, V[index4].second))!=S.end() && 
						S.find(make_pair(V[index4].first, V[index4].second +1))!=S.end() && 
						S.find(make_pair(V[index4].first, V[index4].second +1))!=S.end())
					{
						my_mat[V[index4].first][V[index4].second] = 1;
						my_mat[V[index4].first][V[index4].second+1] = 2;
						my_mat[V[index4].first+1][V[index4].second] = 3;
						my_mat[V[index4].first+1][V[index4].second+1] = 4;
						S.erase((make_pair(V[index4].first, V[index4].second)));
						S.erase((make_pair(V[index4].first + 1 , V[index4].second)));
						S.erase((make_pair(V[index4].first, V[index4].second +1)));
						S.erase((make_pair(V[index4].first+1, V[index4].second+1)));
					}
					else
					{
						tmp_flag = false;
						index4 = tmp_size;
					}
				}
			}
			char tmpp = 92;
			if (!tmp_flag)
			{
				output<<"Impossible\n";
			}
			
			else
			{
				fo(index2,num_of_row)
				{
					fo(index3,num_of_col)
					{
						switch (my_mat[index2][index3])
						{
							case 1:
							output<<"/";
							break;
							case 2:
							
							output<<tmpp;
							break;
							case 3:
								output<<tmpp;
									break;
							case 4:
								output<<"/";
								break;
							case 0:
								output<<".";
								break;
							default:
							break;
						}
					}
					output<<endl;
				}
			}
		}

		


		

	}
}