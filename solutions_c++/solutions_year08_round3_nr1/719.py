#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>

using namespace std;

bool checkInt(string tmp)
{
	for(int i=2; i<tmp.size(); i++)
	{
		if(tmp[i]!='0')
			return false;
	}

	return true;
}

bool predSort(pair<int,int> a, pair<int,int> b)
{
	return (a.first>b.first);
}

void sortt(vector<pair<int,int>>& places)
{
	sort(places.begin(),places.end(),predSort);
}

void placee(vector<pair<int,int>>& places, vector<int>& keys, int p)
{
	int next = 0;

	for(int i=0; i<places.size(); i++)
	{
		if(next>(keys.size()-1))
			next=0;
		if(keys[next]<=p)
		{
			keys[next]++;
			places[i].second=keys[next];
			next++;
		}
		else
		{
			next++;
			i--;
		}
	}
}

void countt(vector<pair<int,int>>& places, int& count)
{
	for(int i=0; i<places.size(); i++)
	{
		count+= places[i].first*places[i].second;
	}
}

int main()
{
	FILE* inFile = fopen("test.in","rt");
	FILE* outFile = fopen("test.out","wt");
	
	int casenum;



	fscanf(inFile,"%d\n",&casenum);

	for(int cs=1; cs<=casenum; cs++)
	{
		int p,k,l,count = 0;

		fscanf(inFile,"%d%d%d\n",&p,&k,&l);

		vector<int> keys(k,0);
		vector<pair<int,int>> places;

		for(int i=0; i<l;i++)
		{
			pair<int,int> temp;
			
			fscanf(inFile,"%d",&(temp.first));

			places.push_back(temp);
		}

		sortt(places);
		
		placee(places,keys,p);

		countt(places, count);

		fprintf(outFile,"Case #%d: %d\n",cs,count);
	}
	

	return 0;
}