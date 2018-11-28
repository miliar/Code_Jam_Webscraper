#include <stdio.h>

int main(void)
{
/*
	int R = 5;
	int k = 5;
	int N = 10;
	int g[1000] = {2,4, 2, 3, 4, 2, 1, 2, 1, 3};
*/

	/*
	int R = 100;
	int k = 10;
	int N = 1;
	int g[1000] = {1};
*/
	int T;

	int R = 4;
	int k = 6;
	int N = 4;
	int g[1000] = {1,4,2,1};

	int pos = 0;
	int last_pos;
	int count;
	__int64 euro = 0;

	int euro_table[1000];
	int jump_table[1000];

	FILE *fp = fopen("C-large.in", "r");
	fscanf(fp, "%d", &T);

	FILE *fpout = fopen("C-large.txt", "w");

	for( int t = 0; t < T; t++ ){
		pos = 0;
		euro = 0;

		fscanf(fp, "%d %d %d", &R, &k, &N);
		for( int i = 0; i < N; i++ ){
			fscanf(fp, "%d", &g[i]);
		}
		
		for( int i = 0; i < N; i++ ){
			count = 0;
			last_pos = i;
			pos = i;
			while( 1 ){
				if( count + g[pos] <= k ){
					count += g[pos++];
					if( pos == N ){
						pos = 0;
					}
					if( last_pos == pos ){
						break;
					}
				}
				else {
					break;
				}
			}

			euro_table[i] = count;
			jump_table[i] = pos;
		}

		pos = 0;
		for( int i = 0; i < R; i++ ){
			euro += euro_table[pos];
			pos = jump_table[pos];
		}

		fprintf(fpout, "Case #%d: %I64d\n",t + 1, euro);
	}

}