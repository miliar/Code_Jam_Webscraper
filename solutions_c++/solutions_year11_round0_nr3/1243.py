// turn_left.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <set>
#include <map>
#include <vector>


using namespace std;

int t;


ofstream fout("output3b.txt");
ifstream fin("C-large.in");
 

void get_input()
{
	fin >> t;	 
	int i, j;	

	for(i = 0 ; i < t; i++)
	{
		int  n;
		set<int> nums;
		fin >> n;

		int num;
		int compute_sum = 0;
		int sum = 0;
		int min = 1000001;
		 
	 
		for(j = 0 ; j < n; j++)
		{			 
			fin >> num;	
			if (num < min)
				min = num;

			sum += num;
			compute_sum ^= num;		 
		}
	 

		fout<<"Case #"<<i+1<<": ";
		
		if(compute_sum != 0)
		{
			fout<<"NO"<<endl;
		}
		else
			fout<<sum - min<<endl;
	 
	}


}


 
 

int main(int argc, char * argv[])
{
	 
    get_input();
	 
	
	return 0;
}

