#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

struct Googler {
	 int total;
	 int best;
	 int one;
	 int two;
	 int three;
	 int division;
	 int remainder;
	bool surprising;
};

Googler createGoogler()
{
	 int tempTotal; //ti
	
	scanf("%d", &tempTotal);
	
	Googler tempGoogler;	
	tempGoogler.total = tempTotal;
	tempGoogler.best = 0;	
	
	tempGoogler.remainder = tempTotal%3;
	tempGoogler.division = tempTotal/3;
	
	tempGoogler.one = tempGoogler.division;
	tempGoogler.two = tempGoogler.division;
	tempGoogler.three = tempGoogler.division;
	
	return tempGoogler;
}

bool operator <(const Googler& x, const Googler& y)
{
	return (x.total < y.total);
}

int main()
{
	 int T, N, S, p, caseNum, numOfBest = 0;
	vector<Googler> Googlers;
	vector<Googler>::iterator it = Googlers.begin();
	
	scanf("%d", &T);
	
	for (caseNum = 1; caseNum <= T; caseNum++)
	{
		scanf("%d", &N);
		scanf("%d", &S);
		scanf("%d", &p);
		
		for ( int count = 0; count < N; count++)
			Googlers.push_back(createGoogler());
		
		sort(Googlers.begin(), Googlers.end());
		 int bound = (p*3)-4;
		 if (bound < 0) bound = 1;
		 if (p == 0) bound = 0;
		
		for (it = Googlers.begin(); it != Googlers.end(); it++)
		{
			if (it->total >= bound)
			{
				if (it->total >= bound + 2)
					numOfBest++;
				else if (it->total == bound && S != 0)
				{
					numOfBest++;
					S--;
				}
				else if (it->total == bound+1  && S != 0)
				{
					numOfBest++;
					S--;
				}
				else if (it->total == 0 && p == 0 && S == 0)
					numOfBest++;
				
				/*if (it->remainder != 0 && it->remainder != 2)
					numOfBest++;
				else if ((it->remainder == 0 && it->one == p && it->two == p && it->three == p))//  && it->total != 0 || (it->remainder == 0 && it->division+1 == p && it->total != 0)
					numOfBest++;
				else if (S != 0)
				{
					S--;
					numOfBest++;
				}*/				
			}			
		}

		printf("Case #%d: %d\n", caseNum, numOfBest);
		numOfBest = 0;
		Googlers.clear();
		it = Googlers.begin();
	} // caseNum for end
	
	return 0;
}
