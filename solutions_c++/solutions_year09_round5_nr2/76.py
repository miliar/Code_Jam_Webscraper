#include <iostream>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
#include <functional>
#include <queue>
#include <bitset>
#include <sstream>
#include <vector>
using namespace std;

#define	sz(v)	(int)v.size()
#define	rep(i,n)	for((i)=0;(i) < (n); (i)++)
#define	rab(i,a,b)	for((i)=(a);(i) <= (b); (i)++)
#define	Fi(N)		rep(i,N)
#define	Fj(N)		rep(j,N)
#define	Fk(N)		rep(k,N)

#define	MOD	10009	

char	s[10000];

int	freq[26];
int	wfreq[20][26];
int	N;

int	total;

int addsum()
{
	int	term = 1;
	int	sum = 0,curr = 0;
	int	i;

	//Fi(26) printf(" %d",freq[i]);

	for(i =0; s[i]; i++)
	{
		if(s[i] == '+' || s[i] == '-')
		{
			sum = (sum + term + MOD) % MOD;
			if(s[i] == '-') term = -1;
			else term = 1;
		}
		else
			term = ((term * freq[s[i] - 'a']) % MOD + MOD) % MOD;
	}

	sum = (sum + term + MOD) % MOD;

	total = (total + sum + MOD) % MOD;
}

void backtrack(int rem)
{
	if(rem == 0)
	{
		addsum();
		return;
	}

	int	i,j,n;

	Fi(N)
	{
		Fj(26) freq[j] += wfreq[i][j];
		backtrack(rem - 1);
		Fj(26) freq[j] -= wfreq[i][j];
	}
}


int main()
{
	int	T,cs;
	int	K;

	scanf("%d",&T);

	rab(cs,1,T)
	{
		scanf("%s %d",s,&K);
		scanf("%d",&N);

		memset(wfreq,0,sizeof(wfreq));
		int	i,j;

		Fi(N)
		{
			char	w[10000];

			scanf("%s",w);

			for(j = 0; w[j]; j++) wfreq[i][w[j] - 'a']++;
		}

		printf("Case #%d:",cs);
		for(int i = 1; i <= K; i++)
		{
			total = 0;
			backtrack(i);

			printf(" %d",total);
		}
		printf("\n");
	}
	return 0;
}
