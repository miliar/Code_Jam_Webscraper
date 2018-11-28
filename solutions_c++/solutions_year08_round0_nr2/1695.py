/*
 *  trains.cpp
 *  
 *
 *  Created by Ben Sanders on 7/17/08.
 *  Copyright 2008 __MyCompanyName__. All rights reserved.
 *
 */

#include<iostream>
#include<iomanip>
#include<cmath>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<numeric>
#include<fstream>

using namespace std;

#define fori(c) for(int i = 0; i < c; i++)
#define forj(c) for(int j = 0; j < c; j++)
#define all(v) (v).begin(), (v).end()
#define mod(a,b) (((a%b)+b)%b)

int main()
{
	ifstream fin("tin.txt");
	ofstream fout("tout.txt");
	
	int N;
	fin >> N;
	string trash;
	
	for(int google = 0; google < N; google++)
	{
		int turnaround;
		fin >> turnaround;
		int A, B;
		fin >> A >> B;
		vector<pair <int, char> > Atrains, Btrains;

		getline(fin,trash);
		fori(A)
		{
			string temp;
			getline(fin,temp);
			cout << temp << endl;
			int h1,m1,h2,m2;
			sscanf(temp.c_str(),"%d:%d %d:%d", &h1, &m1, &h2, &m2);
			cout << h1*60 + m1 << " " << h2*60 + m2 + turnaround << endl;
			Atrains.push_back(make_pair(h1*60 + m1, 'z'));
			Btrains.push_back(make_pair(h2*60 + m2 + turnaround, 'a'));

		}
		fori(B)
		{
			string temp;
			getline(fin,temp);
			cout << temp << endl;
			int h1,m1,h2,m2;
			sscanf(temp.c_str(),"%d:%d %d:%d", &h1, &m1, &h2, &m2);
			cout << h1*60 + m1 << " " << h2*60 + m2 + turnaround << endl;
			Btrains.push_back(make_pair(h1*60 + m1, 'z'));
			Atrains.push_back(make_pair(h2*60 + m2 + turnaround, 'a'));
		}
		sort(Atrains.begin(),Atrains.end());
		sort(Btrains.begin(),Btrains.end());
		
		int Acount = 0;
		int Bcount = 0;
		
		int Afinalnum = 0;
		int Bfinalnum = 0;
		cout << "A" << endl;
		fori(Atrains.size())
		{
			cout << Atrains[i].first << '\t' << Atrains[i].second << endl;
			if(Atrains[i].second == 'a')
			{
				Acount++;
			}
			else
			{
				if(Acount > 0)
				{
					Acount--;
				}
				else
				{
					Afinalnum++;
					Acount=0;
				}
			}
		}
		cout << "B" << endl;
		fori(Btrains.size())
		{
			cout << Btrains[i].first << '\t' << Btrains[i].second << endl;

			if(Btrains[i].second == 'a')
			{
				Bcount++;
			}
			else
			{
				if(Bcount > 0)
				{
					Bcount--;
				}
				else
				{
					Bfinalnum++;
					Bcount = 0;
				}
			}	
		}
		fout << "Case #" << google+1 << ": " << Afinalnum << " " << Bfinalnum << endl;
	}
	
}
