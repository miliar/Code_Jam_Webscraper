#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef struct {
	char R;
	int  b;
} Move;
int main()
{
	int T, N, i, j, k, l, button, steps, move, m1, m2;
	char Robot;
	Move *Moves=NULL;
	int *O=NULL, *B=NULL;
	scanf("%d ", &T);
	for (i=1; i<=T; i++)
	{
		scanf("%d ", &N); 
		Moves = (Move *) malloc(N*sizeof(Move));
		O = (int *) malloc(N*sizeof(int));
		B = (int *) malloc(N*sizeof(int));
		k = l = 0;
		for (j=0; j<N; j++)
		{
			//printf("N=%d\n", N);
			scanf("%c %d ", &Robot, &button);
			Moves[j].R = Robot;
			Moves[j].b = button; //printf("%c --> %d\n", Moves[j].R, Moves[j].b);
			if (Robot == 'O') O[k++] = button;
			else if (Robot == 'B') B[l++] = button;
			Robot = 'a';
		}
		int flag1, flag2;
		k = l = 1;
		m1 = m2 = 0;
		steps = move = 0;
		while (move<N)
		{
//			printf("%d --> %c\n", move, Moves[move].R);
			flag1 = flag2 = 1;
			steps++;
//			printf("Step %d:\n---------------------\n", steps);
//			printf("flag1=%d, flag2=%d\n", flag1, flag2);
			if (k<O[m1]) 	  {k++;flag1 = 0;}
			else if (k>O[m1]) {k--;flag1 = 0;}
			if (l<B[m2])      {l++;flag2 = 0;}
			else if (l>B[m2]) {l--;flag2 = 0;}
//			printf("flag1=%d, flag2=%d, M=%c\n", flag1, flag2, Moves[move].R);
			if (Moves[move].R == 'O' && flag1) {
				if (k==O[m1]) { 
					m1++; 
					move++; 
				}
//				printf("Robot 1 pushes !\n");
			}
			else if (Moves[move].R == 'B' && flag2){
				if (l==B[m2]) { 
					m2++; 
					move++; 
				}
//				printf("Robot 2 pushes !\n");
			}
		}
		printf("Case #%d: %d\n", i, steps);
		free(O);
		free(B);
		free(Moves);
	}
	
	return 0;
}
