#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <float.h>
#include <assert.h>
#include <queue>
#include <iostream>
#include <fstream>

using namespace std;
#define INPUT "in.txt"
#define OUTPUT "out.txt"
#define MAXCASELEN 105
#define TMAX 30

void ReadIn( queue<string> * q )
{
	char * T = (char * ) calloc  (MAXCASELEN, sizeof(char));
	ifstream * is = new ifstream();
	is->open(INPUT);
	while (is->good())
	{
		is->getline(T,MAXCASELEN);
		q->push(string(T));	
	}
	free(T);
}

int ParseAndCompute( string s)
{
	int div, mod;
	int count = 0;
	int N = atoi(&s[0]);		//#dancers
	int S = atoi(&s[2]);        //#surprising score triplets
	int p = atoi(&s[4]);        //best result triplet with at least an element of size >= p 
	int * tScores  = (int *) calloc ( N,     sizeof(int)); //dancers score sums
	int * triplets = (int *) calloc ( N * 3, sizeof(int));    //dancers score tripplets

	int ssize = s.size();
	int sindex;
	for(int i = 0; i < N; i++)
	{
		sindex = s.rfind(' ',ssize);
		tScores[count] = atoi(&s[sindex]);
		ssize = sindex-1;
		count ++;
	}
	assert(N == count);

	//distribute
	for(int i = 0; i < N; i++)
	{
		div = tScores[i] / 3;
		mod = tScores[i] % 3;
		triplets[i*3+0] = div;
		triplets[i*3+1] = div;
		triplets[i*3+2] = div;
		for(int j = i * 3; j < i * 3 + mod; j++) triplets[j]++;
	}

	//apply surprise on suitable triplets
	count = 0;
	for(int i = 0; i < N; i++)
	{
		if(count == S) break;
		if(triplets[i*3+0] == triplets[i*3+1]) 
		{ 
			if(triplets[i*3+0] + triplets[i*3+1] == 0) continue;
			else 
			{	
				if(triplets[i*3+0] == p-1) //check if interesting
				{
					triplets[i*3+0]++; triplets[i*3+1]--;
				}else continue;
			}
		}
	
		else if(triplets[i*3+1] == triplets[i*3+2]) 
		{
			if(triplets[i*3+1] + triplets[i*3+2] == 0) continue;
			else
			{ 
				if(triplets[i*3+1] < p) //check if interesting
				{
					triplets[i*3+1]++; triplets[i*3+2]--;	
				}else continue;		
			}	
		}
		count++;
	}

	//look for those > p 
	count = 0;
	for(int i = 0; i < N; i++)
	{
		if(triplets[i*3+0]>=p || triplets[i*3+1]>=p || triplets[i*3+2]>=p) count++;
	}
	return count;
}

int main( int argc, char **argv )	
{
	int casecntr = 1;
	ofstream out;
	out.open(OUTPUT);
	queue<string> input;
	ReadIn(&input);
	input.pop();
	while (!input.empty())
	{
		int res = ParseAndCompute(input.front());
		cout << "Case #" << casecntr << ": " << res << endl;
		out  << "Case #" << casecntr << ": " << res << endl;
		input.pop();
		casecntr++;
	}
	return 0;
}



