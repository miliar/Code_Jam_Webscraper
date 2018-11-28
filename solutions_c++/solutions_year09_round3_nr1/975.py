#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;

char N[62];
double answer;

void init()
{
	for (int x=0; x < 62; x++) {
		N[x] = '\0';
	}
	answer = 0;
	scanf("%s",N);
	
}
void solve()
{
	int b=-1;
	char S[62];
	int CB[62];
	
	for (int x=0; x < 62; x++) {
		S[x] = '\0';
		CB[x] = -1;
	}
	
	for (int x=0; x< strlen(N); x++)
	{
		int found = 0;

		for (int y=0; y < strlen(S); y++)
		{
			if (N[x] == S[y])
			{
				found = 1;
			}
		}
		if (found == 0)
		{
			S[strlen(S)] = N[x];
		}
	}

	b = strlen(S);
	if (b <= 1)
	{
		b = 2;
	}
	
	CB[0] = 1;
	CB[1] = 0;
	if (b >= 2)
	{
		for (int x=2; x < b;  x++)
		{
			CB[x] = x;
		}
	}
	
	int last_cb = 0;
	char last_char = '\0';
	for (int x=0; x < strlen(N); x++) 
	{
		if (N[x] != last_char && N[x] != '!')
		{
			last_char = N[x];
			for (int y=0; y < strlen(N); y++) 
			{
				if (N[y] == last_char) 
				{
					N[y] = '!';
					answer = answer + CB[last_cb] * pow((double)b,(double)(strlen(N) - y - 1));
				}	
			}
			last_cb ++;
			
			if (CB[last_cb] == -1) 
			{
				break;
			}
		}
	}
	
	
	
}

int main()
{
	
	//	freopen("..\\A.in","r",stdin);
	    freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	//	freopen("..\\A-small-attempt1.in","r",stdin);freopen("..\\A-small-attempt1.out","w",stdout);
	//  freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		
		init();
		solve();
		
		printf("Case #%d: %0.0f",caseId,answer);
		
		if(caseId+1<=testcase){
			printf("\n");
		}
		
		fflush(stdout);
	}
	return 0;
}


