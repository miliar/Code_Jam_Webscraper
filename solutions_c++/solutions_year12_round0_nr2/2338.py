#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>

#define MN 101
#define NEG 20

using namespace std;

vector<int> total;
vector<int> bestResult;

int main()
{
	int t, s, p, n, result;
	scanf("%d", &t);
	for(int c=1; c<=t; c++)
	{
		scanf("%d %d %d", &n, &s, &p);
		//init
		total=vector<int> (n);
		bestResult=vector<int> (n);
		result=0;
		//
		for(int i=0; i<n; i++)
			scanf("%d", &total[i]);
		sort(total.begin(), total.end());

		//with no surprise
		for(int i=0; i<n; i++)
		{
			bestResult[i]=total[i]/3;
			if(total[i]%3>=1)
				bestResult[i]+=1;
			if(bestResult[i]>=p)
			{
				bestResult[i]=NEG;
				result++;
			}
			else if(total[i]%3==1)
				bestResult[i]=NEG;
		}

		int surprise=0;
		for(int i=0; i<n; i++)
			if(bestResult[i]!=NEG)
				if(((total[i]%3==0 && total[i]/3>0) || total[i]%3==2) && bestResult[i]+1>=p)
					surprise++;
		result+=min(surprise, s);
		printf("Case #%d: %d\n", c, result);
	}
	return 0;
}
