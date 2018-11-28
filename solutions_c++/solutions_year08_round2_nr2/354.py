// Was build with STL libraries of standard MS VisualStudio 2005 SP1
// Target application was console win 32 application with multibite character set setting. 
// Used software were licensed to Align Technology Inc

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#define M_PI       3.14159265358979323846

/////////////////////////////////////////////////////////////////

int hashMe(int X, int Y)
{
	return (X%3)+3*(Y%3);
}

int main(int argc, char* argv[])
{
	int numOfCases;
	scanf("%d", &numOfCases);
	for(int cn = 0; cn < numOfCases; cn++)
	{
		int A, B, P;
		scanf("%d%d%d", &A, &B, &P);
		std::vector<bool> set(B - A + 1, 0);
		std::set<int> pset;
		for(int i = P; i <= B/2; i++)
		{
			int j = 2;
			for(; j*j < i; j++)
				if(i%j == 0)
					break;
			if(j*j > i)
				pset.insert(i);
		}
		int count = 0;
		std::queue<int> aqueue;
		for(int i = 0; i < set.size(); i++)
		{
			if(set[i])
				continue;
			count++;
			set[i] = true;
			aqueue.push(i);
			while(!aqueue.empty())
			{
				int cur = aqueue.front();
				aqueue.pop();
				for(std::set<int>::iterator j = pset.begin(); j != pset.end(); ++j)
				{
					int p = *j;
					if((cur+A) % p == 0)
					{
						int minim = p*((A-1)/p+1);
						for(int k = minim; k <= B; k+=p)
						{
							if(!set[k-A])
							{
								set[k-A] = true;
								aqueue.push(k-A);
							}
						}
						j = pset.erase(j);
						if(j == pset.end())
							break;
					}
				}
			}
		}
		std::cout << "Case #" << (cn+1) << ": " << count << "\n";
	}
	return 0;
}

