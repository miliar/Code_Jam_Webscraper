// 1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
		struct walkway
		{
			long B;
			long E;
			long w;
		};
		struct walk1
		{
			double X;
			double w;
		};
		bool minW(struct walk1 first, struct walk1 second)
		{
			return (first.w < second.w);
		}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("A-large.in");
	outFile.open("A-large.out");
	int caseNumMax;
	inFile >> caseNumMax;
	for (int caseNum = 0; caseNum < caseNumMax; ++caseNum)
	{
		double X, S, R, T;
		double result = 0.0;
		int N;
		inFile >> X >> S >> R >> T >> N;
		walkway temp;
		walk1 temp2;
		vector<walk1> walk;
		inFile >> temp.B >> temp.E >> temp.w;
		if (temp.B != 0)
		{
			temp2.X = temp.B;
			temp2.w = 0;
			walk.push_back(temp2);
		}
		temp2.X = temp.E - temp.B;
		temp2.w = temp.w;
		walk.push_back(temp2);
		long last = temp.E;
		for (int i = 1; i < N; ++i)
		{
			inFile >> temp.B >> temp.E >> temp.w;
			if (temp.B != last)
			{
				temp2.X = temp.B - last;
				temp2.w = 0;
				walk.push_back(temp2);
			}
			temp2.X = temp.E - temp.B;
			temp2.w = temp.w;
			walk.push_back(temp2);
			last = temp.E;
		}
		if (last != X)
		{
			temp2.X = X - last;
			temp2.w = 0;
			walk.push_back(temp2);
		}
			
		double TT;
		sort(walk.begin(), walk.end(), &minW);
		for (vector<walk1>::iterator it = walk.begin(); it < walk.end(); ++it)
		{
			TT = (*it).X / ((*it).w + R);
			if (TT <= T)
			{
				result += TT;
				T -= TT;
				(*it).X = 0;
			}
			else
			{
				result += T;
				(*it).X -= (((*it).w) + R) * T;
				T = 0;
			}
			if (T == 0)
				break;
		}
		vector<walk1>::iterator it;
		for ( it = walk.begin(); it < walk.end(); ++it)
		{
			if ( (*it).X != 0 )
				break;
		}
		if ( it != walk.begin() )
			walk.erase(walk.begin(), it);
		for ( it = walk.begin(); it < walk.end(); ++it)
		{
			result += (*it).X / ((*it).w + S);
		}
		outFile << "Case #" << caseNum + 1 << ": ";
		outFile.setf(ios::fixed,ios::floatfield);
		outFile.precision(6);
		outFile << result << endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}