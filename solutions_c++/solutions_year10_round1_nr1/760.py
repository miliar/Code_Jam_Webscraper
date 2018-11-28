#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cmath>
using namespace std;

int main()
{
	int T;
	cin>>T;

	for(int i = 0; i < T; ++i)
	{
		int N,K;
		cin>>N>>K;

		vector<string> vs;
		for(int j = 0; j < N; ++j)
		{
			string tmp;
			cin>>tmp;

			int pos = tmp.length()-1;
			for(int k = pos; k >= 0; --k)
				if(tmp[k] != '.')
				{
					char c = tmp[pos];
					tmp[pos] = tmp[k];
					tmp[k] = c;
					--pos;
				}

			vs.push_back(tmp);
		}

		string p1(K, 'R');
		string p2(K, 'B');
		bool r = false;
		bool b = false;

		// row
		for(int j = 0; j < N; ++j)
		{
			if(vs[j].find(p1) != string::npos)
				r = true;
			if(vs[j].find(p2) != string::npos)
				b = true;
		}

		// col
		for(int j = 0; j < N; ++j)
		{
			string col;
			for(int k = 0; k < N; ++k)
				col.push_back(vs[k][j]);

			if(col.find(p1) != string::npos)
				r = true;
			if(col.find(p2) != string::npos)
				b = true;
		}

		// 
		for(int j = 0; j < 2*N-1; ++j)
		{
			string dia;
			int y = j;
			int x = 0;
			if(j >= N)
			{
				y = N-1;
				x = j-N;
			}

			dia.push_back(vs[y][x]);

			while((x+1)<N && (y-1)>=0)
			{
				++x;
				--y;
				dia.push_back(vs[y][x]);
			}

			if(dia.find(p1) != string::npos)
				r = true;
			if(dia.find(p2) != string::npos)
				b = true;
		}

		for(int j = 0; j < 2*N-1; ++j)
		{
			string dia;
			int y = j;
			int x = N-1;
			if(j >= N)
			{
				y = N-1;
				x = N-1 - (j-N);
			}

			dia.push_back(vs[y][x]);

			while((x-1)>=0 && (y-1)>=0)
			{
				--x;
				--y;
				dia.push_back(vs[y][x]);
			}

			if(dia.find(p1) != string::npos)
				r = true;
			if(dia.find(p2) != string::npos)
				b = true;
		}

		cout<<"Case #"<<i+1<<": ";
		if(r && b)
			cout<<"Both";
		else if(r)
			cout<<"Red";
		else if(b)
			cout<<"Blue";
		else
			cout<<"Neither";

		cout<<endl;

	}

}