#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	int N;
	
	scanf("%d\n", &N);
	for(int i = 0; i < N; i++)
	{
		int n, s, p, v;
		scanf("%d %d %d ", &n, &s, &p);
		
		int score = 0;
		for(int j = 0; j < n; j++)
		{
			scanf("%d ", &v);
			switch(v % 3)
			{
				case 0:
					if(v / 3 >= p)
						score++;
					else if(v / 3 + 1 == p && v / 3 >= 1 && s > 0)
						score++, s--;
					break;
				case 1:
					if(v / 3 + 1 >= p)
						score++;
					break;
				case 2:
					if(v / 3 + 1 >= p)
						score++;
					else if(v / 3 + 2 == p && v / 3 >= 0 && s > 0)
						score++, s--;
					break;
			}
		}
		
		printf("Case #%d: %d\n", i + 1, score);
	}
	
	return 0;
}
