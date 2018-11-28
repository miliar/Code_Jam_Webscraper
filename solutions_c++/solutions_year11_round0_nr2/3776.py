// test.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char combine[36][3];
char opposed[28][2];
char input[1024];
ofstream fout("out.txt");

int C, D, N;

void reset()
{
	for(int i = 0; i < 28; i ++)
	{
		memset(combine[i], 0, 3);
		memset(opposed[i], 0, 2);
	}
	for(int i = 28; i < 36; i ++)
	{
		memset(combine[i], 0, 3);
	}
}



int checkOppose(char a, char b)
{
	if(a > b)
	{
		char tmp = a;
		a = b;
		b = tmp;
	}
	for(int i = 0; i < D; i ++)
	{
		if(opposed[i][0] == a)
		{
			if(opposed[i][1] == b)
				return 1;
		}
	}
	return 0;
}

int checkOppsePosition(int index)
{
	for(int i = 0; i < index; i ++)
	{
		if(checkOppose(input[i], input[index]))
			return 1;
	}
	return 0;
}

char checkCombine(char a, char b)
{
	if(a > b)
	{
		char tmp = a;
		a = b;
		b = tmp;
	}
	for(int i = 0; i < C; i ++)
	{
		if(combine[i][0] == a)
		{
			if(combine[i][1] == b)
				return combine[i][2];
		}
	}
	return 'a';
}

void printOut()
{
	char out[1024];
	memset(out, 0, 1024);
	sprintf(out, "[");
	int first = 1;
	for(int i = 0; i < N; i ++)
	{
		if(input[i] != 'x')
		{
			if(first == 1)
			{
				sprintf(out, "%s%c", out, input[i]);
				first = 0;
			}
			else
			{
				sprintf(out, "%s, %c", out, input[i]);
			}
			
		}
	}
	sprintf(out, "%s]", out);
	printf(out);
	fout << out<<endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	 ifstream fin("data.txt");
	 //ofstream fout("out.txt");
	 string s;  

    
	 int testCaseNum;
	 fin >> testCaseNum;
	 char output[1024];
	 int result;

	 for(int i = 0; i < testCaseNum; i ++)
	 {    
		 printf("testCase # : %d\t", i +1);
		 fout << "Case #"<<i+1<<": ";
		 reset();
		 fin >> C;
		 memset(output, 0, 1024 * sizeof(char));
	
		 for(int j = 0; j < C; j ++)
		 {
			fin >> combine[j];	
			if(combine[j][0] > combine[j][1])
			{
				char tmp = combine[j][1];
				combine[j][1] = combine[j][0];
				combine[j][0] = tmp;
			}
			printf(combine[j]);
			printf("\t");
			
		 }		
		 fin >> D;
		 for(int j = 0; j < D; j ++)
		 {
			 fin >> opposed[j];	
			 
			 if(opposed[j][0] > opposed[j][1])
			 {
				 char tmp = opposed[j][1];
				 opposed[j][1] = opposed[j][0];
				 opposed[j][0] = tmp;
			 }
			 printf(opposed[j]);
			 printf("\t");
		 }	
		 fin >> N;		 
		 fin >> input;	
		
		 for(int j = 0; j < N - 1; j ++)
		 {
			char res;
			if((res = checkCombine(input[j], input[j+1])) != 'a')
			{
				input[j] = 'x'; 
				input[j+1] = res;
			}
			else{
				//result = checkOppose(input[j], input[j+1]);
				result = checkOppsePosition(j+1);
				if(result)
				{
					for(int index =0; index < j +2; index ++)
					{
						input[index] = 'x';
					}
				}
			}
		 }
		 //printf(input);
		 printOut();
		 printf("\n");
	 }
}


