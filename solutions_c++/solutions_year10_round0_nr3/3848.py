#include <iostream>
#include <list>
#include <string>
#include <fstream>
#include <cstdlib>

#define MAX_ROW_ELEM 3

using namespace std;
void show_result(unsigned int R, unsigned int k, unsigned int N, list<int> lineV);
list<int> inpD;
list<int> row1;
list<int> row2;
list<int>::iterator iter1;
list<int>::iterator iter2;

main()
{
	unsigned int R, k, N, T, temp;
	bool top = true;
	ifstream indata;

	indata.open("C-small-sttempt1.in", ios::in);
	if(!indata)
	{
		cerr << "Error opening file!!" << endl;
		exit(1);
	}

	indata >> temp;
	while (!indata.eof())
	{
		if( ( row1.size() < MAX_ROW_ELEM ) )
		{
			indata >> temp;	
			row1.push_back(temp);
		}
		else
		{	
			N = row1.back();
			row1.pop_back();
			k = row1.back();
			row1.pop_back();
			R = row1.back();
			row1.pop_back();

			int ne = 0;
			for(ne = 0 ; ne < N ; ne++)
			{
				indata >> temp;
				row2.push_back(temp);
			}
			if(ne == N)
			{
				show_result(R, k, N, row2);
				row2.clear();
			}
		}
	}
}

void show_result(unsigned int R, unsigned int k, unsigned int N, list<int> lineV)
{
	int front_item;
	unsigned long cost = 0, TotalIncome = 0, round = 1, sum_of_n = 0;
	static int case_no = 1;

	for(iter2 =lineV.begin(); iter2 != lineV.end(); ++iter2)
		sum_of_n = sum_of_n + *iter2;

	//if sum_of_n is less than total capacity of roller coaster 
	//multiply sum_of_n by number of rides per day
	if( sum_of_n > k )
	{
		//calculating total cost per day
		for(; round <= R; round++)
		{
			while( cost <= k)
			{
				front_item = lineV.front();
				cost = cost + front_item; 
				if( cost <= k)
				{
					lineV.pop_front();
					lineV.push_back(front_item);	
				}
				else
				{
					TotalIncome = TotalIncome + ( cost - front_item );
				}
			}
			cost = 0;
		}
	}
	else 
		TotalIncome = sum_of_n * R;

	cout << "Case #"<< case_no << ": "<<TotalIncome << endl;
	case_no++;
}
