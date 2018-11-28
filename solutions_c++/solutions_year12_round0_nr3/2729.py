#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LEN 7
#define MAX 2000000

unsigned long val, list_c, pairs, a, b, cnt, list[MAX];
unsigned char len, used[MAX], temp;

int main()
{
	unsigned short t, x;
	unsigned long c, pos;
	unsigned char d;
	char num[LEN];
	FILE *in, *out;

	in = fopen("C-small.in", "r");
	out = fopen("out.txt", "w");

	if(in == 0 || out == 0)
		return -1;

	fscanf(in, "%hd%c", &t, &x);
	for(x = 0; x < t; x++)
	{
		for(cnt = 0; cnt < MAX; cnt++)
			used[cnt] = 0;
		
		pairs = 0;
		fscanf(in, "%d %d", &a, &b);
		if(b > 10)	//can't make any pairs if b <= 10
		{
			for(c = a; c <= b; c++)
			{
				ltoa(c, num, 10);
				len = strlen(num);
				
				list_c = 1;
				list[0] = c;
				
				for(cnt = len - 1; cnt > 0; cnt--)
				{
					temp = num[len - 1];
					for(d = len - 1;  d > 0; d--)
						num[d] = num[d - 1];
					num[0] = temp;
					
					if(num[0] == '0')	//starts with 0; not a candidate
						continue;
					
					val = atol(num);
		
					if(val >= a && val <= b)
					{
						for(pos = 0; pos < list_c; pos++)
							if(list[pos] == val)
								break;
						if(pos == list_c)	//new number
							list[list_c++] = val;
					}
						
				}
				
				if(!used[c - 1])
				{
					for(cnt = 0; cnt < list_c; cnt++)
						used[list[cnt] - 1] = 1;
					pairs += list_c * (list_c - 1) / 2;
				}
			}
		}
		fprintf(out, "Case #%d: %d\n", x + 1, pairs);
	}

	fclose(in);
	fclose(out);

	return 0;
}
