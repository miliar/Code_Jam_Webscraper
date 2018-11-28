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

int D;
double vndrs[1000008];
double koko[1000008];
int V;




bool test(double sol)
{
	rep(i,V)
		koko[i] = vndrs[i];
	koko[0] -= sol;
	for(int i=1;i<V;i++)
	{
		double desire = koko[i-1] + D;
		if(koko[i] < desire)
		{
			if((fabs(koko[i]-desire) - sol) > 0.000000001)
				return false;
			koko[i] = desire;
		}
		else
		{
			if((fabs(koko[i]-desire) - sol) > 0.000000001)
				koko[i] -= sol;
			else
				koko[i] = desire;
		}
	}
	sort(koko,koko+V);
	rep(i,V-1)
	{
		if(fabs(koko[i]-koko[i+1]) < D)
			return false;
	}
	return true;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("kokoGCJ2s.txt", "w", stdout);
	int K,C;
	cin >> K;
	rep(kase,K)
	{
		V = 0;
		cin >> C >> D;
		int tmp;
		int pnt;
		rep(i,C)
		{
			cin >> pnt >> tmp;
			rep(j,tmp)
			{
				vndrs[V++] = pnt;
			}
		}
		if(V == 1)
		{
			printf("Case #%d: %f\n",kase+1,0);
			continue;
		}
		double s=0,e=INT_MAX,nw;
		double z = INT_MAX;
		rep(iter,100)
		{
			nw = (s+e)/2;
			if(test(nw))
			{
				z = min(z,nw);
				//cout << nw << endl;
				e = nw;
			}
			else
			{
				s = nw;
			}
		}
		printf("Case #%d: %f\n",kase+1,z);

	}
	return 0;
}
