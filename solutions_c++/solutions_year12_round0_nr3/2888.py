#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define SIZE 2000010
#define LEN	32

int main()
{
	int T,t;
	scanf("%d", &T);
	for(t = 1; t <= T; t++)
	{
		int a,b;
		char A[LEN], B[LEN];
		scanf("%d %d", &a, &b);
		sprintf(A, "%d", a);
		sprintf(B, "%d", b);

		int x;
		char X[LEN];
		int ans = 0;
		for(x = a; x <= b; x++)
		{
//			printf("x = %d\n", x);
//			visited[x] = 1;

			sprintf(X, "%d", x);

			int len = strlen(X);
			if( len == 1)
				continue;

			int visited[SIZE] = {0};


			char buffer[LEN] = {0}, tempx[LEN] = {0};
			int temp,i;
			for(i = 1; i < len; i++)
			{
				strcpy(tempx, X);
				strncpy(buffer, X, i);
				memset(tempx, '0', i);
				buffer[i] = 0;

//				for(int j = 0; j < LEN; j++)
//					printf("%c", tempx[j]);
//				printf("\n");


				strcat(tempx, buffer);

//				for(int j = 0; j < LEN; j++)
//					printf("%c", tempx[j]);
//				printf("\n");

				sscanf(tempx, "%d", &temp);
//				printf("%d\n", temp);
		
				if(visited[temp])
					continue;				
				
				visited[temp] = 1;
				if( temp > x && temp <= b)
				{
					ans++;
//					printf("(%d, %d)\n", x, temp);
				}
			}
//			printf("\n");

		}
		printf("Case #%d: %d\n", t, ans);
	}
}
