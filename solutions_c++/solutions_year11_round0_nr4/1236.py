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


ofstream fout("output4b.txt");
ifstream fin("D-large.in");
//ifstream fin("test.txt");
 

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}


void get_input()
{
	fin >> t;	 
	int i, j;	

	for(i = 0 ; i < t; i++)
	{
		int  n;
		int * nums;
		int * src;
		int * done;

		fin >> n;

		src = new int[n];
		nums = new int[n];
		done = new int[n];

		map<int, int> pos_sorted;
		map<int, int > pos_raw;
		

		int num;	
		int sum = 0;
	 
		for(j = 0 ; j < n; j++)
		{			 
			fin >> num;	
			src[j] = num;
			nums[j] = num;	
			done[j] = 0;
		}
		qsort (nums, n, sizeof(int), compare);

		for(j = 0 ; j < n; j++)
		{			 
			if(src[j] != nums[j])
			{
				pos_raw[src[j]] = j;
				pos_sorted[nums[j]] = j;
				sum++;
			}			 	 	 
		}
		
		
		 

		int total = sum;

		sum = 0;
		for(j = 0 ; j < n; j++)
		{
			if(src[j]  != nums[j]  && done[j] == 0)
			{
				 
				if( nums[ pos_raw[nums[j] ]]  == src[j])
				{
					done[j] = done[ pos_raw[nums[j] ]] = 1;
					sum++;
					break;
				}
				 
			}
		}

		fout<<"Case #"<<i+1<<": "<<total<<".000000"<<endl;	
	 
	 
	}


}


 
 

int main(int argc, char * argv[])
{
	 
    get_input();
	 
	
	return 0;
}

