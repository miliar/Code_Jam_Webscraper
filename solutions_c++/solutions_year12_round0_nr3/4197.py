#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fstream>
#include <string>
#include <list>

using namespace std;

ofstream outfile;

void recycled_pair(const int &small, const int &big)
{
	vector<int> my_vector;
	my_vector.resize(big+1);
	list<int> my_list;

	int ret_value = 0;
	int temp = 0;
	int leading_zero = 0;
	int new_num = 0;
	int num_digits = 1;

	for(int i = small; i <= big; ++i)
		my_vector[i] = i;

	for(int i = small; i <= big; ++i)
	{
		if( my_vector[i] == 0) continue;
		temp = i;
		while(temp > 0)
		{
			if(temp%10 == 0)	leading_zero++;			//Leading zeros ++
			my_list.push_back(temp%10);
			//cout<<temp%10<<endl;
			temp /= 10;
			//cout<<temp<<endl;
		}
		my_list.reverse();											//important
		list<int>::const_iterator iter1;
		list<int>::const_iterator iter2;

		for( iter1 = ++my_list.begin();  iter1 != my_list.end(); iter1++)			//Generate different combinations
		{
			iter2 = iter1;
			int size = my_list.size();
			while( size >= 1 )
			{
				new_num += (*iter2) * pow(10.0, size-1);
				iter2++;
				if(iter2 == my_list.end()) iter2 = my_list.begin();
				size--;
			}


			if(new_num == i) 
			{
				my_vector[new_num] = 0;
				new_num = 0;
				num_digits = 1;
				continue;
			}
			if(new_num <= big && new_num >= small) 
			{
				//outfile<<"new:"<<new_num<<"  i:"<<i<<endl;
				my_vector[new_num] = 0;					//Skip duplicated elements
				num_digits++;
			}		
			new_num = 0;		
		}


		int partial = 0;
		int size = my_list.size();
		//cout<<"num_digits-leading_zero: "<<num_digits-leading_zero<<endl;
		for(int p = 0; p < num_digits; p++)
		{
			partial += p;

		}
		//outfile<<"partial: "<<partial<<endl;
		ret_value += partial;
		partial = 0;
		num_digits = 1;
		leading_zero = 0;
		my_list.clear();
	}

	outfile<<ret_value<<endl;

}

int main()
{
	ifstream infile;

	infile.open("c:\\google\\C-small-attempt0.in");
	outfile.open("c:\\google\\result.txt");

	int test_case = 0;
	int small = 0;
	int big = 0;
	infile>>test_case;

	for(int i = 0; i < test_case; i++)
	{
		infile>>small;
		infile>>big;
		outfile<< "Case #"<<i+1<<": ";
		recycled_pair(small, big);
	}

	system("pause");
	return 0;
}