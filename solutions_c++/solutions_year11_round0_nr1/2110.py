#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define DB 0

vector<char> tasks;
vector<int> B;
vector<int> O;

int count(int now, int dest)
{
	return abs(now - dest);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		int N;
		scanf("%d", &N);
		getchar();

		for (int i = 0; i < N; i++)
		{
			char r;
			int p;
			scanf("%c", &r);
			scanf("%d", &p);
			getchar();
			tasks.push_back(r);
			if (r == 'B') B.push_back(p);
			if (r == 'O') O.push_back(p);
		}
		
		int B_pos, O_pos;
		B_pos = O_pos = 1;

		int B_index, O_index;
		B_index = O_index = 0;

		int B_size = B.size();
		int O_size = O.size();

		#if DB
		
		for (int i = 0; i < N; i++)
			printf("%c", tasks[i]);
		printf("\n");
		
		for (int i = 0; i < B_size; i++)
			printf("%d ", B[i]);
		printf("\n");

		for (int i = 0; i < O_size; i++)
			printf("%d ", O[i]);
		printf("\n");

		#endif

		int B_next, O_next;
		if (B_size > 0) B_next = count(1, B[0]);
		else B_next = 0;

		if (O_size > 0) O_next = count(1, O[0]);
		else O_next = 0;

		int result = 0;

		for (int i = 0; i < N; i++)
		{
			if (tasks[i] == 'B')
			{
				#if DB
					printf("B needs %d\n", B_next + 1);
				#endif
				
				B_next++;
				O_next = max(0, O_next - B_next);
				result += B_next;
				if (B_index >= B_size + 1) B_next = 0;
				else B_next = count(B[B_index], B[B_index + 1]);
				B_index++;
			}
			if (tasks[i] == 'O')
			{
				#if DB
					printf("O needs %d\n", B_next + 1);
				#endif
				O_next++;
				B_next = max(0, B_next - O_next);
				result += O_next;
				if (O_index >= O_size + 1) O_next = 0;
				else O_next = count(O[O_index], O[O_index + 1]);
				O_index++;
			}
		}

		printf("Case #%d: %d\n", Ti, result);
		B.clear();
		O.clear();
		tasks.clear();

	}
	return 0;
}

