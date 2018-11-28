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

int diamond[202][202];

int part[1002][1002];

int main(int argc, char* argv[])
{
//#ifdef _DEBUG
	freopen("Test.in", "r", stdin);
//#endif

	int T;
	scanf("%d", &T);

	int vis = 1000;

	for (int nTest = 1; nTest <= T; nTest++)
	{		
		int K;
		scanf("%d", &K);

		int x = 0, y = 0;

		for (int i = 1; i <= K; i++)
		{
			for (int j = 0; j < i; j++)
			{

				scanf("%d", &diamond[i - 1 - j][0 + j]);
				
			}
		}
		for (int i = K - 1; i >= 1; i--)
		{
			for (int j = 0; j < i; j++)
			{				
				int line = K - 1 - i + 1;

				scanf("%d", &diamond[K - 1 - j][line + j]);
			}
		}

		

		int sza = -1;
		for (int sz = K; sz <= 4 * K + 1; sz++)
		{
			bool ok = true;

			for (int y = 0; y + K <= sz; y++)
			{
				for (int x = 0; x + K <= sz; x++)
				{
					vis += 20;
					for (int i = 0; i < K; i++)
					{
						for (int j = 0; j < K; j++)
						{
							part[y + i][x + j] = vis + diamond[i][j];
						}
					}

					ok = true;
					
					for (int i = 0; i < sz; i++)
					{
						for (int j = 0; j < sz; j++)
						{
							if (part[i][j] >= vis)
							{
								if (part[j][i] >= vis && part[j][i] != part[i][j])
								{
									ok = false;
									break;;
								}

								if (part[sz - 1 - j][sz - 1 - i] >=  vis && part[sz - 1 - j][sz - 1 - i] != part[i][j])
								{ 
									ok = false;
									break;;
								}
							}
						}
					}
				

					if (ok)
					{
						sza = sz;
						goto found;
					}
				}
			}
			
		}

	found:
		assert (sza != -1);
		int res = sza * sza - K * K;


		printf("Case #%d: %d\n", nTest, res);
		fflush(stdout);
	} 


	return 0;
}


