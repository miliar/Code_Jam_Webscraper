// 1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream is;
	is.open("A-large.in");
	int T;
	vector<int> O;
	vector<int> B;
	string order = "";
	char c;
	int p;
	is>>T;
	ofstream os("A-large.out");
	int po, pb;
	int j, k;
	int terms;
	for(int ii=1; ii<=T; ii++)
	{
		O.clear();
		B.clear();
		order = "";
		j = k = 0;
		int total = 0;
		int d =0;
		po =pb = 1;
		is>>terms;
		for(int t = 0; t<terms; t++)
		{
			is>>c>>p;	
			if(c == 'O')
			{
				O.push_back(p);
				order += "O";
			}

			else
			{
				B.push_back(p);
				order += "B";
			}
		}
	
	
		
		for (int i=0; i<order.length(); i++)
		{
			if (order[i] == 'O')
			{
				
				d = abs(O[j] - po);
				total += d+1;
				if (po<O[j])
					po += d;
				else if (po > O[j])
					po -= d;
				++j;
				if(B.size() != 0 && k<B.size())
				{
					if(pb < B[k])
					{
						pb += d+1;
						if (pb > B[k])
							pb = B[k];
					}
					else if(pb > B[k])
					{
						pb -= (d+1);
						if(pb<B[k])
							pb = B[k];
					}
				}
			}
			else if (order[i] == 'B')
			{
				d = abs(B[k] - pb);
				total += d+1;
				if(pb < B[k])
					pb += d;
				else if(pb > B[k])
					pb -=d;

				++k;
				if(O.size() != 0 && j<O.size())
				{
					if(po < O[j])
					{
						po += d+1;
						if(po > O[j])
							po = O[j];
					}
					else if(po > O[j])
					{
						po -= (d+1);
						if(po < O[j])
							po = O[j];
					}
				}
			}
		}
		os<<"Case #"<<ii<<": "<<total<<endl;

	}
	
	return 0;
}

