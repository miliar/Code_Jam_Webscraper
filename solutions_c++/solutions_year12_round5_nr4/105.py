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

bool A[36][36];

int index(char c)
{
	if(c >= '0' && c <= '9')
		return c - '0';
	else
		return c - 'a' + 10;
}

char transform(char c)
{
	if(c == 'o')
		return '0';
	if(c == 'i')
		return '1';
	if(c == 'e')
		return '3';
	if(c == 'a')
		return '4';
	if(c == 's')
		return '5';
	if(c == 't')
		return '7';
	if(c == 'b')
		return '8';
	if(c == 'g')
		return '9';
	return c;
}

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int TESTs;
	scanf("%d",&TESTs);
	for(int test = 1; test <= TESTs; test++)
	{
		printf("Case #%d: ",test);
		int K;
		scanf("%d",&K);
		string s;
		cin >> s;
		mem0(A);

		for(int i = 0; i < s.size() - 1; i++)
		{
			char c1 = s[i];
			char c2 = transform(c1);

			char c3 = s[i+1];
			char c4 = transform(c3);
			
			A[index(c1)][index(c3)] = true;
			A[index(c2)][index(c3)] = true;
			A[index(c1)][index(c4)] = true;
			A[index(c2)][index(c4)] = true;

		}

		int kst = 1;
		for(int i = 0; i < 36; i++)
			for(int j = 0; j < 36; j++)
				if(A[i][j])
					kst++;
		int delta1 = 0;
		int delta2 = 0;
		for(int i = 0; i < 36; i++)
		{
			int kst1 = 0;
			int kst2 = 0;
			for(int j = 0; j < 36; j++)
			{
				if(A[i][j])
					kst1++;
				if(A[j][i])
					kst2++;
			}
			if(kst2 > kst1)
			{
				delta2 += kst2 - kst1;
			}
			if(kst1 < kst2)
			{
				delta1 -= kst1 - kst2;
			}
		}
		kst += max(delta1, delta2);
		if(delta1 != 0)
			kst--;
		printf("%d", kst);
		printf("\n");
	}
	return 0;
}