#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

int words[5000][15];
char pattern[100000];
int L, D, N;
int pat[15];


int calc()
{
	char* p = pattern;

	for (int i = 0; i < L; i++)
	{
		pat[i] = 0;
		if (*p == '(')
		{
			p++;
			while (*p != ')')
			{
				pat[i] |= 1 << (*p - 'a');
				p++;
			}
			p++;
		}
		else
		{	
			pat[i] |= 1 << (*p - 'a');
			p++;
		}
	}


	int cnt = 0;
	for (int i = 0; i < D; i++)
	{
		bool match = true;
		for (int j = 0; j < L; j++)
		{
			if ((words[i][j] & pat[j]) == 0)
			{
				match = false;
				break;
			}

		}
		if (match)
			cnt++;
	}
	return cnt;
}
char word[100];

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);
	//freopen("Test.out", "w", stdout);

	scanf("%d%d%d", &L, &D, &N);

	for (int i = 0; i < D; i++)
	{
		scanf("%s", word);
		for (int j = 0; j < L; j++)
		{
			words[i][j] = 1 << (word[j] - 'a');
		}
	}

	for (int i = 0; i < N; i++)
	{
		scanf("%s", pattern);

		int res = calc();

		printf("Case #%i: %i\n", i + 1, res);
	}



	return 0;
}


 