#include <fstream>
#include <vector>
#include <iostream>
#include <algorithm>

/*

Candy Splitting


...


attempt 4 failed? This has become seriously embarssing. So exhausted, but must finish...
hopefully 6th time's a charm.

...Argh. I need some damned way to verify these OTHER than submitting them. I guess doing
it by hand is not that difficult, just freaking tedious as hell, and I'm rapidly running
out of juice here. 

Wow. Should've done one by hand to begin with, would've noticed sooner that if it's
possible at all, giving patrick any one piece of candy will ALWAYS result in the xor's
matching. How I failed to recognize this from the begining, when I recognized that I could
toss out any that didn't have an even number of bits in every column, I don't know. >.<

But, I finally caught it. Should work this time :P

*/

using namespace std;

#define BASENAME "C-large"


pair<int,int> Sums(vector<vector<int>>& values)
{
	pair<int,int> res(0,0);
	for (unsigned int i=0;	i<values.size(); ++i)
	{
		for (unsigned int j=0;	j<values[i].size(); ++j)
		{
			res.first+=values[i][j];
			res.second^=values[i][j];
		}
	}

	return res;
}


int main(int argc, char* argv[])
{
	
	ifstream inFile(BASENAME ".in");
	ofstream outFile(BASENAME ".out");

	int numCases;
	inFile>>numCases;

	for (int caseNum=1; caseNum<=numCases; ++caseNum)
	{
		outFile<<"Case #"<<caseNum<<": ";

		unsigned int numCandies;
		vector<int> candyValues;
		inFile>>numCandies;
		vector<int> bitCounts(20,0);

		while(numCandies-->0)
		{
			unsigned int value;
			inFile>>value;
			candyValues.push_back(value);

			int bitNum=0;
			while(value)
			{
				bitCounts[bitNum++]+=value&0x1;
				value>>=1;
			}
		}
	
		//cull out impossible cases before we waste time permuting
		bool impossible=false;
		for (int bit=0; bit<20; ++bit)
		{
			if ((bitCounts[bit]&0x1)==1)
			{
				impossible=true;
				break;
			}
		}

		if (!impossible)
		{
			int total=0;
			std::sort(candyValues.begin(),candyValues.end());
			for (int i=1; i<candyValues.size(); ++i)
				total+=candyValues[i];

			outFile<<total;

			/*
			int maxBit=0;
			//divide candies into "ranks" based on their highest non-zero bits
			vector<vector<int>> rankedValues(20,vector<int>());
			for (unsigned int curVal=0; curVal<candyValues.size(); ++curVal)
			{
				int l2=log2(candyValues[curVal]);
				rankedValues[l2].push_back(candyValues[curVal]);

				if (l2>maxBit)
					maxBit=l2;
			}
			
			//sort each rank
			for (int i=0; i<maxBit; ++i)
				std::sort(rankedValues[i].begin(), rankedValues[i].end());

			vector<pair<int,int>> permutations;
			//now we can go through permutations.
			pair<int,int> sean=Sums(rankedValues);
			pair<int,int> patrick(0,0);

			if (Permute(rankedValues,maxBit,sean,patrick))			
			{
				outFile<<sean.first;
				//cout<<"sean : "<<sean.first<<','<<sean.second<<'\t';
				//cout<<"patrick : "<<patrick.first<<','<<patrick.second<<endl;
			}
			else
			{
				//cout<<"no."<<endl;
				outFile<<"NO";
			}
			*/

		}
		else
		{
			//cout<<"no."<<endl;
			outFile<<"NO";
		}

		outFile<<endl;


	}
	/**/
	return 0;
}