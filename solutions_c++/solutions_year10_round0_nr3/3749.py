#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long int int64;
typedef unsigned long long int uint64;

void setArray(int64 *index, int64 *g, int *score, int n, int k)
{
     for(int i=0;i<n;i++)
     {
             int64 temp = 0;
             int j=i;
             bool op = false;
             while(true)
             {
                  if(op)
                  {
                          index[i] = temp;
                          --j;
                          if(j == -1) j=n-1;
                          score[i] = j;
                          break;
                  }
                  temp += g[j];
                  if(temp > k)
                  {
                          temp -= g[j];
                          index[i] = temp;
                          score[i] = j;
                          break;
                  }
                  ++j;
                  if(j == n) j=0;
                  if(j == i) op = true;
             }
     }
}

int64 getResult(int64 *index, int *score, int r)
{
    int i = 0;
    int result = 0;
    while(r > 0)
    {
            result += index[i];
            i = score[i];
            --r;
    }
    return result;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	
	int testcase,r,k,n;
	int64 *g, *index;
    int *score;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d:",caseId);
		scanf("%d",&r);
		scanf("%d",&k);
		scanf("%d",&n);
		g = (int64*)malloc(sizeof(int64)*n);
		index = (int64*)malloc(sizeof(int64)*n);
		score = (int*)malloc(sizeof(int)*n);
		for(int j=0;j<n;j++)
              scanf("%llu", &g[j]);
        setArray(index,g,score,n,k);
        printf(" %llu\n", getResult(index,score,r));
		fflush(stdout);
		free(g);
		free(index);
		free(score);
	}
	return 0;
}
