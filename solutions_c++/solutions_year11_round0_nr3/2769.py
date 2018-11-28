#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>

using namespace std;

typedef unsigned int uint;
typedef unsigned long long ull;
typedef std::bitset<1000> IntBits;


int bad_math(const vector<int> &nums)
{
	int total=0;
	for(uint p=0; p<nums.size(); ++p)
	{
		total = total ^ nums[p];
	}
	return total;
}

int reg_math(const vector<int> &nums)
{
	int total=0;
	for(uint p=0; p<nums.size(); ++p)
	{
		total += nums[p];
	}
	return total;
}

int main()
{
	uint numTest;
	cin >> numTest;
	for(uint test=0; test<numTest; ++test)
	{
		int numCandies;
		cin >> numCandies;
		vector<int> candies(numCandies);
		for(uint c=0; c<candies.size(); ++c)
		{
			cin >> candies.at(c);
		}
		int seanMax=0; 
		sort(candies.begin(), candies.end());
		//do
		//{
		uint upperLim = 1<<numCandies;
		for(uint bin=1; bin < upperLim; ++bin)
		{
			IntBits brep(bin);
			vector<int> pats;
			vector<int> seans;
			for(uint s=0; s<brep.size() && s<candies.size(); ++s)
			{
				if(brep.test(s) == 0) seans.push_back(candies.at(s));
				else pats.push_back(candies.at(s));
			}
			
			int seanTot = reg_math(seans);
			if(seanTot <= seanMax) break;
			
			//int patTot = reg_math(pats);
			//if(patTot > seanTot) break;
			
			if(bad_math(pats) == bad_math(seans))
			{
				seanMax = seanTot;
			}
		}
		//}while(next_permutation( candies.begin(), candies.end() ));
		
		cout<<"Case #"<<test+1<<": ";
		if(seanMax != 0) cout<<seanMax<<endl;
		else cout<<"NO"<<endl;
	}
}
