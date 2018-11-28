#include <stdio.h>
#include <queue>

using namespace std;

int main()
{
	int T, R, k, N, num = 1, tk, i;
	int euro, data, groupcount;
	queue<int> group;
	
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	scanf("%i", &T);
	while(T--)
	{
		while(!group.empty())
			group.pop();

		euro = 0;
		scanf("%i %i %i", &R, &k, &N);
		for(i = 0; i < N; i++)
		{
			scanf("%i", &data);
			group.push(data);
		}
		
		while(R--)
		{
			tk = k;
			groupcount = 0;
			while(true)
			{
				data = group.front();
				if(tk < data) // not enough capacity
					break;
				else if(groupcount == N) // if all group are in roller coaster
					break;
				else
				{
					group.pop(); // put this group in roller coaster
					group.push(data);
					tk -= data;
					euro += data;
					groupcount++;
				}
			}
		}

		printf("Case #%i: %i\n", num++, euro);
	}

	return 0;
}