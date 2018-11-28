#include <iostream>
#include <map>

#define MAXN 1000

using namespace std;

typedef long long INT;

struct CACHE
{
	CACHE(){}
	CACHE(INT v,int s){val=v;nextState=s;}
	INT val;
	int nextState;
};

int r,k,n;
INT raw[MAXN],sumRaw[MAXN];
map<int,CACHE> cache[MAXN]; //<round used, money gain>

//just use cache
INT solve(int state, int roundLeft)
{
	if(roundLeft == 0)return 0;
	map<int,CACHE>::iterator i = --cache[state].upper_bound(roundLeft);
	return i->second.val + solve(i->second.nextState, roundLeft - i->first);
}

inline INT sum(int index) // [0, index]
{
	return sumRaw[index % n] + (INT(index / n)) * sumRaw[n-1];
}

int main()
{
	freopen("output.txt","wt",stdout);
	freopen("input.txt","rt",stdin);

	int nTest;
	scanf("%d",&nTest);
	for(int i = 1; i <= nTest; i++)
	{
		scanf("%d %d %d",&r,&k,&n);
		for(int j = 0; j < n; j++)
		{
			scanf("%lld",raw + j);
			sumRaw[j] = raw[j] + ((j == 0)? 0 : sumRaw[j-1]);
			cache[j].clear();
		}

		if(k > sumRaw[n-1])k = sumRaw[n-1];

		//Populate cache for round = 1 first... [need to do this fast]
		for(int j = 0; j < n; j++)
		{
			INT target = ((j==0)? 0:sum(j-1)) + k, val = 0;
			int left = j, right = k + left, ind;
			while(left <= right)
			{
				int mid = (left + right) >> 1;
				INT candidate = sum(mid);
				if(candidate < target)
				{
					left = mid + 1;
					if(val < candidate) {val = candidate;ind= mid;}
				}
				else if(candidate > target)right = mid - 1;
				else 
				{
					val = target;
					ind = mid;
					break;
				}
			}
			val -= ((j==0)? 0:sum(j-1));
			cache[j][1]=CACHE(val,(ind + 1) % n);
		}

		//Populate round = 2^i
		for(int round = 1; round * 2 < r; round *= 2)
			for(int j = 0; j < n; j++)
			{
				CACHE x = cache[j][round];
				CACHE y = cache[x.nextState][round];
				y.val += x.val;
				cache[j][round*2] = y;
			}

		printf("Case #%d: %lld\n",i,solve(0,r));
	}
	return 0;
}


/* a
#define MAXN 30

typedef unsigned State;

int main()
{
	freopen("output.txt","wt",stdout);
	freopen("input.txt","rt",stdin);

	int nTest,n,k;
	scanf("%d",&nTest);
	for(int i = 1; i <= nTest; i++)
	{
		scanf("%d %d",&n,&k);
		printf("Case #%d: %s\n",i,(((1<<n)-1) == (k&((1<<n)-1)))? "ON" : "OFF");
	}
	return 0;
}
*/