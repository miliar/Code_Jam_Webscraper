#include<stdio.h>

int abs(int x)
{
	if(x<0)
		return -x;
	return x;
}

int max(int x, int y)
{
	if(x>y)
		return x;
	return y;
}

int main()
{
	//input and output
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	//reading the input
	int T;
	scanf("%d", &T);
	int O[100];
	int oi = 0, bi = 0;
	int B[100];
	for(int cases = 1; cases <= T; cases++)
	{
		int N;
		char letter; int position;
		int posO = 1, posB = 1;
		int lmO = 0, lmB = 0;
		int time = 0;
		scanf("%d", &N);
		int temp;
		for(int vecs = 0; vecs < N; vecs++)
		{
			scanf(" %c %d", &letter, &position);
			//printf("%c %d - ", letter, position);
			if(letter == 'O')
			{
				temp = abs(position - posO) - (time - lmO);
				time += max(temp, 0);
				time += 1;
				posO = position;
				lmO = time;
				//printf("O is pressed\n");
			}
			else
			{
				temp = abs(position - posB) - (time - lmB);
				time += max(temp, 0);
				time += 1;
				posB = position;
				lmB = time;
				//printf("B is pressed\n");
			}
			//printf("%d th iteration: the time is %d\n", vecs, time);
		}
		printf("Case #%d: %d\n", cases, time);
	}
	return 0;
}