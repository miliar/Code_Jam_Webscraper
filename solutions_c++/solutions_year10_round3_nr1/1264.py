#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <fstream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

typedef struct _mypoint{
	int x;
	int y; 
}mypoint; 

int main()
{
	
	mypoint myp[10000]; 
	ifstream fin; 
	ofstream fout; 
	fin.open("A-large.in");
	fout.open("testout.txt");

	int i,j,z,T,N;
	int A,B; 
	fin>>T;
	for (i=0; i<T; i++)
	{
		int interaction =0; 
		fin>>N; 
		for (j=0; j<N; j++)
		{
			fin>>myp[j].x>>myp[j].y; 
		}

		for (j=0; j<N; j++)
		{
			for (z=j+1; z<N; z++)
			{

				if(myp[z].x > myp[j].x) 
				{	
					if(myp[z].y < myp[j].y) 
							interaction++; 
				}
				else 
				{
					if(myp[z].y > myp[j].y) 
							interaction++; 
				}
				

			}

		}
		fout<<"Case #"<<i+1<<": "<<interaction<<endl;

			
	}

	return 0; 
}