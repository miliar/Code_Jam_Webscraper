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

char s[1000];
int S;

int mem[501][20];

char welcome[] = "welcome to code jam";
int W = 19;

int count(int pos, int w)
{
	if (w == W)
		return 1;

	int& res = mem[pos][w];
	if (res != -1)
		return res;

	res = 0;

	for (int i = pos; i < S; i++)
	{
		if (s[i] == welcome[w])
		{
			res = (res + count(i + 1, w + 1)) % 10000;
		}
	}

	return res;
}

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);
	//freopen("Test.out", "w", stdout);

	gets(s);

	int T;
	sscanf(s, "%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{
		gets(s);
		S = strlen(s);
		
		memset(mem, -1, sizeof(mem));
		int res = count(0, 0);		
		
		printf("Case #%i: %04d\n", nTest, res);
	}
 


	return 0;
}


