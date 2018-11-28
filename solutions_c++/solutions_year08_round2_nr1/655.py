// Template for code jam!
//
#include "stdafx.h"
#include <math.h>
#include <fstream>
#include <string>
#include <vector>
//#include <algorithm>
//#include <map>
//#include <queque>
//#include <stack>
#include <set>

using namespace std;

//other functions may go here!

//main function!

typedef struct t_point{
	__int64 x;
	__int64 y;	
} point;

int _tmain(int argc, _TCHAR* argv[])
{
    ifstream inputFile("A-small.in");
    ofstream outputFile("A-small.out", std::ios::trunc);
	//ifstream inputFile("A-large.in");
    //ofstream outputFile("A-large.out", std::ios::trunc);
    if((!inputFile.is_open()) || (!outputFile.is_open()))
      return -1;  //error openning input/output file!

	int numIterations;
	//string receive; getline(inputFile, receive); numIterations = atoi(receive.c_str());
	inputFile >> numIterations;
	int numCases = 1;
	vector<point> pontos;
	long int n, A, B, C, D, M, count;
	point pontoAdd, check;
	while(numCases <= numIterations)
	{
		pontos.clear();
		//parsing code goes here
		inputFile >> n;
		inputFile >> A;
		inputFile >> B;
		inputFile >> C;
		inputFile >> D;
		inputFile >> pontoAdd.x;
		inputFile >> pontoAdd.y;
		inputFile >> M;
		pontos.push_back(pontoAdd);
		for(int h=1; h < n; h++)
		{
			pontoAdd.x = (A*pontoAdd.x + B)%M;
			pontoAdd.y = (C*pontoAdd.y + D)%M;
			pontos.push_back(pontoAdd);
		}
		//problem code goes here
		count = 0;
		for(int w=0; w<pontos.size()-2; w++)
		{
			for(int y=w+1; y<pontos.size()-1; y++)
			{
				for(int z=y+1; z<pontos.size(); z++)
				{
					__int64 tX = pontos[w].x + pontos[y].x + pontos[z].x;
					__int64 tY = pontos[w].y + pontos[y].y + pontos[z].y;
					if ((tX%3 == 0) && (tY%3 == 0))
						count++;					
				}
			}
		}
		outputFile << "Case #" << numCases << ": " << count << endl;
		numCases++;
	}
	return 0;
}

