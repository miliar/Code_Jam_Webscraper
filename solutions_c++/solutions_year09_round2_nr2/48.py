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

int main(int argc, char* argv[])
{ 
	freopen("Test.in", "r", stdin);
	//freopen("C:\\out", "w", stdout);

	int caseCount;
	scanf("%d", &caseCount);

	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		string s;
		cin >> s;

		if (!(next_permutation(s.begin(), s.end())) || s[0] == '0')
		{
			s += '0';
			sort(s.begin(), s.end());			
			int p = 0;
			while (s[p] == '0')
				p++;
			
			char c = s[p];
			s.erase(s.begin() + p);

			s = c + s;	
		}

		
		printf("Case #%i: %s\n", nCase, s.c_str());
		fflush(stdout);
	}
 

	return 0;
}


