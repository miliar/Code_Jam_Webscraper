#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

ifstream inf;
ofstream outf;
	

int main(void){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	int tests;
	inf >> tests;
	for (int test = 0; test < tests; test++)
	{		
		int n;
		inf >> n;
		int pos[2], ctime, wait[2];
		int robot, npos;
		pos[0] = pos[1] = 1;
		wait[0] = wait[1] = 0;
		ctime = 0;
		for (int i = 0; i < n; i++)
		{
			char c;
			inf >> c >> npos;
			if (c == 'O') 
				robot = 0;
			else
				robot = 1;
			int fnd = 1 - robot;
			int dist = abs(npos - pos[robot]);
			dist = max(0, dist - wait[robot]);
			int otime = dist + 1;
			wait[fnd] +=otime;
			wait[robot] = 0;
			ctime +=otime;
			pos[robot] = npos;
		}
		outf << "Case #" << test+1 << ": " << ctime << endl;
		
		
	}

	outf.close();
	return 0;
}
