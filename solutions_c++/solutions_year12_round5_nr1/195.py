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

struct level
{
	int id;
	int seconds;
	int prob;
}temp;

bool comparator(const level &a, const level &b)
{
	double aExp = (((double)a.seconds) / (100.0 - (double)a.prob) + (double)b.seconds)/((double)b.prob);
	double bExp = (((double)b.seconds) / (100.0 - (double)b.prob) + (double)a.seconds)/((double)a.prob);
	if(fabs(aExp - bExp) > 1e-9)
		return aExp > bExp;
	else
		return a.id < b.id;
	
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int TESTs;
	scanf("%d",&TESTs);
	for(int test = 1; test <= TESTs; test++)
	{
		printf("Case #%d: ",test);
		int N;
		scanf("%d",&N);
		vector<level> Lv;
		Lv.resize(N);
		for(int i = 0; i < N; i++)
		{
			Lv[i].id = i;
			scanf("%d",&Lv[i].seconds);
		}
		for(int i = 0; i < N; i++)
		{
			scanf("%d",&Lv[i].prob);
		}
		stable_sort(Lv.begin(), Lv.end(), comparator);
		for(int i = 0; i < N; i++)
			printf(" %d",Lv[i].id);
		printf("\n");
	}
	return 0;
}