#include <stdio.h>
#include <string.h>
#include <math.h>
#define MAXSIZE 110
void main (void)
{
	int T, I;
	FILE* out;
	scanf("%d", &T);
	if(!( out=fopen("123.out", "w") ))
	{
		printf("open error\n");
	}
	for(I=1; I<=T; I++)
	{
		int count, i, n, step[2], temp, minus, position[2][MAXSIZE];	//Orange=0,Blue=1
		char color;
		memset(position, 0, sizeof(position) );
		scanf("%d", &n);
		//position[0][0]=position[1][0]=1;
		for(i=0; i<n; i++)
		{
			scanf(" %c", &color);
			scanf("%d", &position[color=='B'][i]);
		}
		color = 1;
		step[0] = step[1] = 1;
		minus = temp =0;
		count = 0;
		for(i=0; i<n; i++)
		{
			if(position[color][i]==0)
			{
				minus = temp;
				count += temp;
				temp = 0;

				color = !color;
			}
			temp += abs(position[color][i] - step[color]) - minus;
			minus = 0;
			if(temp<0) temp = 0;
			temp ++;
			step[color] = position[color][i];
		}
		count += temp;
		fprintf(out, "Case #%d: %d\n", I, count);
		printf("Case #%d: %d\n", I, count);
	}
}