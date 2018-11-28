#pragma comment(linker, "/STACK:65777216")

#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <ctime>
#include <memory.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define mem0(a) memset(a, 0, sizeof(a))
#define mem1(a) memset(a, -1, sizeof(a))
#define pb push_back

double gen(double a, double b)
{
	double p = rand();
	p = (double)p / (double)RAND_MAX;
	p *= (b - a);
	p += a;
	p *= 1000;
	p = floor(p);
	p /= 1000;
	return p;
}

struct people
{
	int r;
	int id;
}tempp;

struct round
{
	double x, y;
	double r;
	int id;
}temp;

bool comparator1(const people &a, const people &b)
{
	return a.r > b.r;
}

bool comparator2(const round &a, const round &b)
{
	return a.id < b.id;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int TESTs;
	scanf("%d",&TESTs);
	for(int test = 1; test <= TESTs; test++)
	{
		printf("Case #%d: ",test);
		int N,W,L;
		vector<people> r;
		scanf("%d%d%d",&N,&W,&L);
		for(int i = 0; i < N; i++)
		{
			int p;
			scanf("%d",&p);
			tempp.id = i;
			tempp.r = p;
			r.push_back(tempp);
			
		}
		sort(r.begin(), r.end(), comparator1);
		
		vector<round> all;

		for(int i = 0; i < N; i++)
		{
			while(true)
			{
				double x = gen(0, (double)W);
				double y = gen(0, (double)L);
				bool flag = true;
				for(int j = 0; j < all.size(); j++)
				{
					if( (all[j].x - x) * (all[j].x - x) + (all[j].y - y) * (all[j].y - y) < (all[j].r + r[i].r) * (all[j].r + r[i].r))
					{
						flag = false;
						break;
					}
				}
				if(flag)
				{
					temp.r = r[i].r;
					temp.x = x;
					temp.y = y;
					temp.id = r[i].id;
					all.push_back(temp);
					break;
				}
			}
		}
		sort(all.begin(), all.end() ,comparator2);
		for(int i = 0; i < N; i++)
			printf(" %0.3lf %0.3lf", all[i].x, all[i].y);





		printf("\n");
	}
	return 0;
}