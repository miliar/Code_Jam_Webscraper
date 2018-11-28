// googleTest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>
using namespace std;
typedef vector<string> vs;
int pos[8][2] = {{0,-1},{-1,-1},{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1}};
int check(char *arr, int width,int heigh,int k)
{
	int p,q;
	int bFlag = 0;
	int rFlag = 0;
	for (int i =0; i < heigh; i++)
		for (int j = 0; j < width; j++)
		{
			if (arr[i*width +j] == '.' || (arr[i*width+j] == 'R' && rFlag) || (arr[i*width+j] == 'B' && bFlag))
				continue;
			// Ë®Æ½
			char c = arr[i*width +j];
				int count = 1;
			if (k <= width -j) {
				for (p = j+1; p < width; p++)
				{
					if (arr[i*width +p] == c)
						count ++;
					else
						break;
				}
				if (count == k)
				{
					if (c == 'R')
						rFlag = 1;
					else
						bFlag = 1;
				}
			}
			count = 1;
			
			if (k <= heigh -i)
			{
				//Êú
				for (p = i +1; p < heigh ; p ++)
				{
					if (arr[p*width+j] == c)
						count ++;
					else 
						break;
				}
				if (count == k)
				{
					if (c == 'R')
						rFlag = 1;
					else
						bFlag = 1;
				}
				// zuo 
				count =1;
				if (k <= j+1) {
					for (p= i+1,q=j-1; p < heigh && q>=0; p++,q--)
					{
						if (arr[p*width+q] == c)
							count ++;
						else 
							break;

					}
					if (count == k)
					{
						if (c == 'R')
							rFlag = 1;
						else
							bFlag = 1;
					}

				}
				//you
				count = 1;
				if (k <= width -j)
				{
					for (p= i+1,q=j+1; p < heigh && q<width; p++,q++)
					{
						if (arr[p*width+q] == c)
							count ++;
						else 
							break;

					}
					if (count == k)
					{
						if (c == 'R')
							rFlag = 1;
						else
							bFlag = 1;
					}
				}
			}
		}
		if (rFlag & bFlag)
			return 3;
		if (rFlag)
			return 1;
		if (bFlag)
			return 2;
		return 0;
}
void rotate(string &line)
{
	for (int i = line.size()-1; i >= 0; i --)
	{
		if (line[i] == '.') {
			for (int j = i-1; j >=0;j --)
				if (line[j] != '.') {
					line[i] = line[j];
					line[j] = '.';
					break;
				}
		}
		
	}
}
int main(int argc, char* argv[])
{
	ifstream infile("A-large(2).in");
	ofstream outfile("resFile");
	string line;
	char *buf;
	getline(infile,line);
	int lineCnt= 0;
	while(getline(infile,line))
	{
		int N,k;
		lineCnt ++;
		sscanf(line.data(),"%d %d",&N,&k);
		buf = (char *)malloc(N*N*1);
		char *head = buf;
		for (int i = 0; i < N; i ++) {
			getline(infile,line);
			rotate(line);
			strncpy(head,line.data(),N);
			head = head +N;
		}
		int res = check(buf,N,N,k);
		outfile << "Case #" << lineCnt << ": ";
		switch(res)
		{
		case 0:
			outfile << "Neither" << endl;
			break;
		case 1:
			outfile << "Red" << endl;
			break;
		case 2:
			outfile << "Blue" << endl;
			break;
		case 3:
			outfile << "Both" << endl;
			break;
		}
	}
	outfile.close();
	infile.close();
}

