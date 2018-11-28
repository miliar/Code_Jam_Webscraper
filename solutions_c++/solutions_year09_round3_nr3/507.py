#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int MAX = 105;

char visited[MAX][MAX];
int val[MAX][MAX];

int numbers[MAX];
int P,Q;

int process(int low, int high)
{
	if(low >= high)
		return 0;

	if(visited[low][high] != 0)
		return val[low][high];

	int mini = 2000000000;
	int i, v1, v2;

	for(i=0; i<Q; i++)
	{
		if(numbers[i] >= low && numbers[i] <= high)
		{
			v1 = process(low, numbers[i]-1);
			v2 = process(numbers[i]+1, high);

			if((high-low+v1+v2)<mini)
			{
				mini = high-low+v1+v2;
			}
		}
	}

	if(mini == 2000000000)
		mini = 0;
	
	visited[high][low] = 1;
	val[high][low] = mini;

	return mini;
}


int main(void)
{	
	//freopen("c:\\IO\\C-small-attempt0.in", "rt", stdin);
	//freopen("c:\\IO\\C-small-attempt0_out.out", "wt", stdout);

	int i, j, t;
	int res;

	scanf(" %d " ,&t);

	for(i=1; i<=t; i++)
	{
		memset(visited, 0, sizeof(visited));
		scanf( " %d %d" ,&P ,&Q);

		for(j=0; j<Q; j++)
		{
			scanf(" %d" ,&numbers[j]);
		}

		sort(numbers, numbers+Q);

		res = 0;

		res = process(1, P);

		printf("Case #%d: %d\n" ,i ,res);
	
	}


	return 0;
}


