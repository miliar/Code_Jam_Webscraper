#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

struct TCombine
{
	char a, b;
	char c;
};
struct TOppose
{
	char a, b;
};

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		int C;
    scanf("%d ", &C);
		vector<TCombine> combine;
		for (int i = 0; i < C; i++)
		{
			TCombine tc;
			scanf("%c%c%c ", &tc.a, &tc.b, &tc.c);
			combine.push_back(tc);
		}
		
		int D;
		scanf("%d ", &D);
		vector<TOppose> oppose;
		for (int i = 0; i < D; i++)
		{
			TOppose to;
			scanf("%c%c ", &to.a, &to.b);
			oppose.push_back(to);
		}
		
		int N;
		scanf("%d ", &N);
		
		int size = 0;
		char stack[109];

		for (int i = 0; i < N; i++)
		{
			scanf("%c", &stack[size]);
			size++;
			
			//combine
			if (size >= 2)
				for (int i = 0; i < C; i++)
					if (((stack[size - 1] == combine[i].a)
						&& (stack[size - 2] == combine[i].b))
						|| ((stack[size - 1] == combine[i].b)
						&& (stack[size - 2] == combine[i].a)))
					{
						size--;
						stack[size - 1] = combine[i].c;
						//printf("%c and %c make %c\n", combine[i].a, combine[i].b, combine[i].c);
						break;
					}
			
			//clear
			for (int i = 0; i < size; i++)
				for (int j = 0; j < size; j++)
					for (int k = 0; k < D; k++)
					{
						if ((stack[i] == oppose[k].a) && (stack[j] == oppose[k].b))
						{
							size = 0;
							//printf("Cleared.\n");
							break;
						}
					}
		}
		
		//output
		printf("Case #%d: [", Ti);
		for (int i = 0; i < size - 1; i++)
			printf("%c, ", stack[i]);
		if (size > 0) printf("%c", stack[size - 1]);
		printf("]\n");
		
		
	}
	return 0;
}