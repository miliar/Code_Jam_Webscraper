// STLBasics.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <list>
#include <set>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

bool wiresort(pair<int,int> x, pair<int,int> y)
{
	if(x.first < y.first)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int main()
{
	int T;

	cin >> T;

	for(int i = 1; i <= T; i++)
	{
		multimap<int, int> intersections;
		int N;
		vector< pair<int,int> > wires;
		

		cin >> N;
		for(int in = 0; in < N; in++)
		{
			int a, b;
			cin >> a >> b;
			wires.push_back(make_pair(a,b));
		}

		sort(wires.begin(), wires.end(), wiresort);

		for(int in = 0; in < N; in++)
		{
			for(int j = 0; j < N; j++)
			{
				if(in == j)
				{
					break;
				}

				if( ((wires[j].first - wires[in].first) * (wires[j].second - wires[in].second)) < 0 )
				{
					if(in < j)
					{
						intersections.insert(make_pair(in,j));
					}
					else
					{
						intersections.insert(make_pair(j,in));
					}
				}
			}			
		}
		cout << "Case #" << i << ": " << intersections.size() << "\n";
	}
}