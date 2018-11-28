#include <fstream>
#include <iostream>
#include <vector>
#define _max 10010
using namespace std;

int M, V;
int changable[_max];
int and_gate[_max];
int value[_max];
int table0[_max];
int table1[_max];
int solution;

int solve_it(int target_value)
{
	int i;
	int l, r;
	for(i = (M - 1) / 2 + 1; i <= M; i++)
	{
		if(value[i] == 1)
		{
			table0[i] = _max;
			table1[i] = 0;
		}
		else
		{
			table0[i] = 0;
			table1[i] = _max;
		}
	}
	
	for(i = (M - 1) / 2; i >= 1; i--)
	{
		l = i * 2;
		r = i * 2 + 1;
		if(and_gate[i] == 1)
		{// and
			table0[i] = table0[l] + table0[r];
			if(table0[l] + table1[r] < table0[i]) table0[i] = table0[l] + table1[r];
			if(table1[l] + table0[r] < table0[i]) table0[i] = table1[l] + table0[r];
			
			table1[i] = table1[l] + table1[r];
			
			if(changable[i] == 1)
			{ // or
				if(table0[l] + table0[r] + 1 < table0[i]) table0[i] = table0[l] + table0[r] + 1;
				
				if(table1[l] + table0[r] + 1 < table1[i]) table1[i] = table1[l] + table0[r] + 1;
				if(table0[l] + table1[r] + 1 < table1[i]) table1[i] = table0[l] + table1[r] + 1;
				if(table1[l] + table1[r] + 1 < table1[i]) table1[i] = table1[l] + table1[r] + 1;				
			}
		}
		else 
		{// or
			table0[i] = table0[l] + table0[r];

			table1[i] = table1[l] + table0[r];
			if(table0[l] + table1[r] < table1[i]) table1[i] = table0[l] + table1[r];
			if(table1[l] + table1[r] < table1[i]) table1[i] = table1[l] + table1[r];
			
			if(changable[i] == 1)
			{ // and
				if(table1[l] + table1[r] + 1 < table1[i]) table1[i] = table1[l] + table1[r] + 1;
				
				if(table0[l] + table0[r] + 1 < table0[i]) table0[i] = table0[l] + table0[r] + 1;
				if(table0[l] + table1[r] + 1 < table0[i]) table0[i] = table0[l] + table1[r] + 1;
				if(table1[l] + table0[r] + 1 < table0[i]) table0[i] = table1[l] + table0[r] + 1;
			}
		}
		if(table0[i] > _max) table0[i] = _max;
		if(table1[i] > _max) table1[i] = _max;
	}
	
	if(target_value == 0)
	{
		return table0[1];
	}
	else
	{
		return table1[1];
	}
}

int main()
{
	ifstream fin("problemA.in");
	ofstream fout("problemA.out");
	
	int test_case;
	int num_test_cases;	
	
	int i;

	fin >> num_test_cases;
	for(test_case = 1; test_case <= num_test_cases; test_case++)
	{	
		fin >> M >> V;
		for(i = 1; i <= (M - 1) / 2; i++)
		{
			fin >> and_gate[i] >> changable[i];
		}
		for(; i <= M; i++)
		{
			fin >> value[i];
		}
		solution = solve_it(V);
		if(solution < _max)
			fout << "Case #" << test_case << ": " << solution << endl;
		else
			fout << "Case #" << test_case << ": IMPOSSIBLE" << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}