#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;
int main(int argc, char *argv[])
{

	ifstream  ifs("input");
	ofstream ofs("output");

	int N;
	ifs >> N;

	for (int cs =0; cs < N; ++cs){

	int R,C;
	ifs >> R >>C;
	vector<vector<char> > vr (R, vector<char> (C, '.'));
	for (int i =0; i< R; ++i)
	{
		for (int j =0; j< C; ++j)
		{
			ifs >> vr[i][j];
		}
	}


	for (int i =0 ; i+1< R; ++i)
	{
		for (int j =0; j+1< C; ++j)
		{
			if ((vr[i][j] == '#') && (vr[i+1][j]== '#') && (vr[i+1][j+1] == '#') && (vr[i][j+1] == '#'))
			{
				vr[i][j] = '/';
				vr[i][j+1] = '\\';
				vr[i+1][j+1] = '/';
				vr[i+1][j] = '\\';
			}
		}
	}
	bool bFalse = false;
	for (int i =0 ; i< R; ++i)
	{
		for (int j =0; j< C; ++j)
		{
			if (vr[i][j] == '#')
			{
				ofs << "Case #" << cs+1<< ":" <<endl;
				ofs << "Impossible" << endl;
				bFalse =true;
				goto label1;
			}
		}
	}
	label1:
	if (bFalse)
		continue;

	ofs << "Case #" << cs+1<< ":" <<endl;
	for (int i =0 ; i< R; ++i)
	{
		for (int j =0; j< C; ++j)
		{
			ofs << vr[i][j];

		}
		ofs << endl;
	}

}



}
