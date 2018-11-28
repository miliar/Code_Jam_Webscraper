#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		int N;
		scanf("%d ", &N);
		
		int O_position = 1;
		int B_position = 1;
		int O_time = 0;
		int B_time = 0;
		for (int i = 0; i < N; i++)
		{
			char R;
			int P;
			scanf("%c %d ", &R, &P);
			
			//printf("%c going to %d\n", R, P);
			
			if (R == 'O')
			{
				O_time = max(B_time + 1, O_time + abs(P - O_position) + 1);
				O_position = P;
			}
			else
			{
				B_time = max(O_time + 1, B_time + abs(P - B_position) + 1);
				B_position = P;
			}
			//printf("O_time = %d; B_time = %d\n", O_time, B_time);
		}
		printf("Case #%d: %d\n", Ti, max(O_time, B_time));
	}
	return 0;
}