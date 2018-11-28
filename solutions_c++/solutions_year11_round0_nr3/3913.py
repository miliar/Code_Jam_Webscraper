// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	 ifstream fin("data.txt");
	 ofstream fout("out.txt");
	 string s;  

	 char output[1024];
	 int testCaseNum;
	 fin >> testCaseNum;

	 int N;
	 int min_val;
	 long sum;
	 int result;
	 int data;

	 for(int i = 0; i < testCaseNum; i ++)
	 {    
		 fin >> N;
		 if( N == 1)
		 {
			 sprintf(output, "Case #%d: NO\n", i+1);
			 fout << output;
			 fin >> N;			
			 continue;
		 }
		 memset(output, 0, 1024*sizeof(char));
		 sum = 0;
		 min_val = -1;
		 for(int j = 0; j < N; j ++)
		 {
			fin >> data;
			if(min_val == -1) 
			{
				min_val = data;
				result = data;
			}
			else{
				if(data < min_val)
					min_val = data;
				result ^= data;
			}
			sum += data;
		 }		  
		 if(result == 0)
		 {
			 sprintf(output, "Case #%d: %d\n", i+1, (sum - min_val));
			 fout << output;
		 }
		 else{
			  sprintf(output, "Case #%d: NO\n", i+1);
			  fout << output;
		 }
	 }
}

