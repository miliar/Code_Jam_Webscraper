#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>
#include <complex>
#include <limits>
#include <string.h>
#include <fstream>
using namespace std;
#define rep(x,n) for(int x=0;x<n;x++)
#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define resetBit(code, i) (code & ~(1 << i))
#define mem(a, b) memset(a, b, sizeof(a))

long long L,t,N,C;
long long all[1005];

long long get(int indx)
{
	return all[indx%C];
}

int bosters[2];
bool hasBoster(int i)
{
	return (i==bosters[0] || i==bosters[1]);
}
long long addboster(int i,long long tm,long long dist)
{
	long long init = tm+(get(i)*2);
	long long tt = max(t,tm);
	long long tmp = dist+get(i);
	if((tm + (get(i)*2)) > tt)
	{
		dist += (tt-tm)/2;
		tm = tt;
		if(dist < tmp)
		{
			tm += (tmp - dist);
			dist = tmp;
		}
		return init-tm;
	}
	else
		return 0;
}
long long calc()
{
	long long tm = 0;
	long long dist = 0;
	int tt;
	rep(i,N)
	{
		
			tm += get(i)*2;
			dist += get(i);
	}
	return tm;
}
long long greed[1000008];
void main2()
{
	cin >> L >> t >> N >> C;
	rep(i,C)
		cin >> all[i];
	bosters[0] = bosters[1] = -1;
	long long init = calc();
	long long best = init;
	
	long long ttm = 0;
	long long dist = 0;
	long long sol;
	rep(i,N)
	{
		greed[i] = addboster(i,ttm,dist);
		ttm += get(i)*2;
		dist += get(i);
	}
	sort(greed,greed+N);
	reverse(greed,greed+N);
	rep(i,L)
	{
		best -= greed[i];
	}
	cout << best << endl;
}

int main()
{
	freopen("in.txt", "r", stdin);
	//freopen("3BIGF.txt", "w", stdout);
	//freopen("1big.txt", "w", stdout);
	int K;
	cin >> K;
	rep(kase,K)
	{
		printf("Case #%d: ",kase+1);
		main2();
	}
	return 0;
}
