/*
 *  universe.cpp
 *  
 *
 *  Created by Ben Sanders on 7/17/08.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 */

#include<iostream>
#include<fstream>
#include<iomanip>
#include<cmath>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<numeric>

using namespace std;

#define fori(c) for(int i = 0; i < c; i++)
#define forj(c) for(int j = 0; j < c; j++)
#define all(v) (v).begin(), (v).end()
#define mod(a,b) (((a%b)+b)%b)

using namespace std;

int main()
{
	ifstream fin("uin.txt");
	ofstream fout("uout.txt");
	
	int N;
	fin >> N;
	for(int lulz = 0; lulz < N; lulz++)
	{
		int res = 10000000;

		map<string,int> engine;
		int S;
		fin >> S;
		string trash;
		getline(fin,trash);
		fori(S)
		{
			string temp;
			getline(fin, temp);
			//cout << temp << endl;
						//engine.push_back(make_pair(temp,0));
			engine[temp]=0;
		}
		int Q;
		fin >> Q;
		getline(fin,trash);

		fori(Q)
		{
			string temp;
			getline(fin,temp);
			//cout << "search: " << temp << endl;
			int mymin = 1000000;
			for(map<string,int>::iterator it = engine.begin(); it != engine.end(); it++)
			{
				if(it->second != -1)
				{
					mymin = min(mymin,it->second);
				}
			}
			mymin++;
			for(map<string,int>::iterator it = engine.begin(); it != engine.end(); it++)
			{
				if(it->first != temp)
				{ 
				    if(mymin < it->second)
					{
						it->second = mymin;
					}
					else if(it->second == -1)
					{
						it->second = mymin;
					}
				}
				//cout << it->first << "\t" <<  it->second << " " << endl;
			}
			engine[temp]=-1;


		}
		for(map<string,int>::iterator it = engine.begin(); it != engine.end(); it++)
		{
			if(it->second != -1)
			{
				res = min(res,it->second);
			}
		}

		fout << "Case #" << lulz + 1<< ": " << res << endl;

	}
	fin.close();
	fout.close();
	
}
