#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <stack>

using namespace std;

int main(int argc, char **argv)
{
	int T;
	freopen("D-large.in", "rb", stdin);
	freopen("D-large.out", "wb", stdout);

	scanf("%d", &T);

	for(int t = 0; t < T; t++)
	{
		int N;
		scanf("%d", &N);
		vector< int > edges(N);
		for(int i = 0; i < N; i++)
		{
			scanf("%d", &edges[i]);
			edges[i]--;
		}


		int answer = 0;

		vector<int> marked(N);
		for(int i = 0; i < N; i++)
		{
			if(marked[i])
			{
				continue;
			}

			int t = 0;
			int q = i;
			while(!marked[q])
			{
				marked[q] = 1;
				t++;

				q = edges[q];
			}

			if(t > 1)
				answer += t;
		}
		
		printf("Case #%d: %0.6f\n", t + 1, (float)answer);
	}

	return 0;
}