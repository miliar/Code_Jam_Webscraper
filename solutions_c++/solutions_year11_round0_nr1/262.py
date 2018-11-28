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
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

int type[200];
int buttonIndex[200];

int main(int argc, char* argv[])
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
#endif
	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		
		int N;
		scanf("%d", &N);

		for (int i = 0; i < N; i++)
		{
			char c;
			scanf(" %c", &c);
			type[i] = c == 'O';

			scanf("%d", &buttonIndex[i]);
		}

		int pos[2] = {1, 1};
		int time = 0;

		for (int i = 0; i < N; i++)
		{ 
			int nextIndex = 1;
			for (int j = i + 1; j < N; j++)
			{
				if (type[j] != type[i])
				{
					nextIndex = buttonIndex[j];
					break;
				}
			}

			while (pos[type[i]] != buttonIndex[i])
			{
				if (buttonIndex[i] < pos[type[i]])
					pos[type[i]]--;
				else
					pos[type[i]]++;

				if (nextIndex != pos[1 - type[i]])
				{
					if (nextIndex < pos[1 - type[i]])
						pos[1 - type[i]]--;
					else
						pos[1 - type[i]]++;
				}
				
				time++;				
			}
			if (nextIndex != pos[1 - type[i]])
			{
				if (nextIndex < pos[1 - type[i]])
					pos[1 - type[i]]--;
				else
					pos[1 - type[i]]++;
			}
			time++;
		}


		printf("Case #%d: %d\n", nTest, time);
		fflush(stdout);
	} 


	return 0;
}


