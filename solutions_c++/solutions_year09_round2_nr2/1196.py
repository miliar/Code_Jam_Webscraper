#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int compare(const void *arg1, const void *arg2)
{
	int k = *(char*)arg1-'0'-(*(char*)arg2-'0');
	return k;
}

int main(int argc, char* argv[])
{
	FILE* is = freopen(argv[1], "r", stdin);
	FILE* os = freopen(argv[2], "w", stdout);

	int t;

	scanf("%d", &t);
	

	for (int i = 1; i <= t; i++)
	{
		char num[22];
		memset(num,0,sizeof(num));
		scanf("%s",num);

		int len=strlen(num);

		for (int k = len - 2; k >= 0; k--)
		{
			char d = num[k];
			for (int j = len - 1; j > k; j--)
			{
				if ((d-'0')<(num[j]-'0'))
				{
				 num[k]=num[j];
				 num[j]=d;
				 
				qsort(num+k+1, len-k-1, sizeof(char), compare);
				 goto outs;
				};
			}
			

		}
		char num2[22];
		memset(num2,0,sizeof(num2));
		
		int t;
		t = 0;
		for (k = len - 1; k >= 0; k--)
		{
			if (num[k]=='0')
				t++;
			else
				break;
		}
		len -= t;
		for (k = len - 1 ; k >= 0; k--)
		{
			num2[k] = num[len-1-k];			
		}

		char num3[23];
		memset(num3,0,sizeof(num3));
		
		num3[0]=num2[0];
		for (k = 0; k < t + 1; k++)
		{
			num3[k+1] = '0';
		}

		int index;
		index = strlen(num3);
		memcpy(num3+index, num2+1, strlen(num2)-1);

		printf("Case #%d: %s\n", i, num3);
		continue;		
	outs: printf("Case #%d: %s\n", i, num);
	
	}
	fclose(is);
	fclose(os);
	return 0;
}