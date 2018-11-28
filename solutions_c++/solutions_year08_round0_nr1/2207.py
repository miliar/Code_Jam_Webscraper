#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void search_the_best_solution(int engine_number , int engine_name_number , int &switchc , int &countn , vector <string> engine , vector <string> engine_name);

int main()
{
	int case_number;
	int i , j , k;
	ifstream input;
	input.open("A-large(1).in");
	ofstream output("output.txt");
	input>>case_number;
	for(i = 0; i < case_number; i++)
	{
		vector <string> engine;
		vector <string> engine_name;
		int engine_number = 0;
		int engine_name_number = 0;
		string en;
		input>>engine_number;
		getline(input , en);
		for (j = 0; j < engine_number; j++)
		{
			getline(input , en);
			engine.push_back(en);
		}
		input>>engine_name_number;
		if(engine_name_number != 0)
		{
			getline(input , en);
		}
		for (k = 0; k < engine_name_number; k++)
		{
			string enn;
			getline(input , enn);
			engine_name.push_back(enn);
		}
		
		
		int switch_count = 0;
		int count_name = 0;
		if(engine_name_number == 0)
		{
			output<<"Case #"<<i+1<<": "<<switch_count<<endl;
		}
		while(count_name != engine_name_number)
		{
			search_the_best_solution(engine_number , engine_name_number , switch_count , count_name , engine , engine_name);
			if(count_name == engine_name_number)
				output<<"Case #"<<i+1<<": "<<switch_count<<endl;
			else
				count_name--;
		}
	}
	input.close();
	return 0;
}


void search_the_best_solution(int engine_number , int engine_name_number , int &switchc , int &countn , vector <string> engine , vector <string> engine_name)
{
	int count = engine_number;
	int i , j , k;
	vector <string> engine_test(engine_number);
	for(i = 0; i < engine_number; i++)
	{
		engine_test[i] = engine[i];
	}
	for (i = countn; i < engine_name_number; i++)
	{
		for(j = 0; j < engine_number; j++)
		{
			if(engine_name[i] == engine_test[j])
			{
				engine_test[j] = " ";
				count--;
				break;
			}
		}
		countn++;
		if(count == 0)
		{
			switchc++;
			break;
		}
	}
	
}