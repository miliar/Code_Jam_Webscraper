#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

#define all(x) (x).begin(),(x).end()
#define forn(i,s,e) for(int i=(s),_e=(e);i<_e;i++)
#define rep(i,n) forn(i,0,n)
#define pb push_back 
#define db(i) cout<<#i<<"= "<<i<<endl; 

ifstream fin("C-small.in");
ofstream fout("output.out");

const int MAX = 1010;
long long v[MAX];
long long csum[MAX];
long long memo[MAX];
int nextPlace[MAX];
long long nRides, capacity, nGroups;

//takes in [low,high)
inline int lowerBound2(long long array[],int low, int high, const long long &key)
{
	--high;
	int lowVal = 0;
	if (low > 0)
		lowVal = array[low - 1];
    while (low < high) 
	{
		int mid = (low + high + 1) >> 1;
		if (array[mid] - lowVal <= key)
	    	low = mid;
		else
	    	high = mid - 1;
    }
    return low;
}


int lowerBound(long long array[],int low, int high, const long long &key)
{    
    int curPlace;
    int count, step;
    count = high - low;
    int lowVal = 0;
    if ( low > 0 )
    	lowVal = array[low - 1];
    while (count > 0 )
    {
        curPlace = low; 
        step = count / 2; 
        curPlace+=step;
        
        //if segment sum is less than key
        if( array[curPlace] - lowVal < key )
        {
            low = ++curPlace;
            count -= step + 1;
        }
        else
            count = step;
    }
    return low;
}



int main()
{
	int nCases;
	fin >> nCases;
	for (int ij = 1; ij <= nCases; ij++)
	{
		fin >> nRides >> capacity >> nGroups;
		long long curSum = 0;
		for (int i = 0; i < nGroups; i++)
		{
			fin >> v[i];
			curSum += v[i];
			csum[i] = curSum;
			memo[i] = -1;
			nextPlace[i] = -1;
		}
		
		//take as many as possible to fill upto capacity
		long long searchVal = capacity;
		int startPlace = 0;
		int endPlace = nGroups - 1;
		long long totCost = 0;
		for (int rideNum = 1; rideNum <= nRides; rideNum++)
		{
			
			if ( memo[startPlace] != -1 )
			{
				totCost += memo[startPlace];
				startPlace = nextPlace[startPlace];
				continue;
			}
				
			//look for no cycle 
			
			//check if end point satisfies capacity; therefore no cycle
			//if sum from v[startPlace]+...+v[endPlace] >= search val
			long long startVal = 0;
			if (startPlace != 0)
				startVal = csum[startPlace - 1];
				
			long long stripTot = csum[endPlace] - startVal;
			long long segSum = 0;
			int lbInd = 0;
			if (  stripTot >= searchVal )
			{
				//cout << "No cycle\n";
				//do a lower bound search on segment given startPlace endPlace 
				//and searchVal
				lbInd = lowerBound2(csum, startPlace, endPlace + 1, searchVal);
				if (csum[lbInd] - startVal > searchVal)
					--lbInd;
				if (lbInd < 0) 
					lbInd = nGroups - 1;
				segSum = csum[lbInd] - startVal;
				if (segSum > searchVal)
						segSum = 0;
				totCost += segSum;
				memo[startPlace] = segSum;
			}
			else
			{
				//cout << "Cycle\n";
				//grab all [start,end], do lowerbound on [0,start)
				searchVal -= stripTot;
				if (startPlace != 0)
				{
					lbInd = lowerBound2(csum, 0, startPlace, searchVal);
					//db(lbInd);db(startPlace);
					if (csum[lbInd] > searchVal)
						--lbInd;
					if (lbInd < 0) 
						lbInd = nGroups - 1;
					segSum = csum[lbInd];
					if (segSum > searchVal)
						segSum = 0;
				}
				totCost += stripTot + segSum;
				memo[startPlace] = stripTot + segSum;
			}
			//update searchVal, startPlace, endPlace, totCost
			int newPlace = (lbInd + 1) % nGroups;
			nextPlace[startPlace] = newPlace;
			startPlace = newPlace;
			searchVal = capacity;
			/*
			db(totCost);
			db(startPlace);
			db(segSum);
			int z;
			fin >> z;
			*/
		}

		fout << "Case #" << ij << ": " << totCost << "\n";
	}
			
		
    printf("done\n");
    int z;
    scanf("%d",&z);
    return 0;
}
