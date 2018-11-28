#include<iostream>
using namespace std;
#include<stdio.h>
#include<cstdio>
#include<string.h>

char _c[37][3];
char _d[28][3];
char str[101];
char final[101];
int T, C, D, N;

int combine(int k)
{
	for(int i = 0; i < C; i ++)
	{
		if((str[k] == _c[i][0] && str[k + 1] == _c[i][1])
			|| (str[k] == _c[i][1] && str[k + 1] == _c[i][0]))
		{
			return i;
		}
	}
	return -1;
	
}

int combine_back(int k)
{
	for(int i = 0; i < C; i ++)
	{
		if((str[k] == _c[i][0] && str[k - 1] == _c[i][1])
			|| (str[k] == _c[i][1] && str[k - 1] == _c[i][0]))
		{
			return i;
		}
	}
	return -1;	
}

int clear(int k)
{
	for(int i = 0; i < D; i ++)
	{
		if(str[k] == _d[i][0])
		{
			for(int j = k + 1; j < N; j ++)
			{
				if(str[j] == _d[i][1])
				{
					int com = combine_back(j);
					if(com == -1)
					{
						return j;
					}
				}
			}
		}

		if(str[k] == _d[i][1])
		{
			for(int j = k + 1; j < N; j ++)
			{
				if(str[j] == _d[i][0])
				{
					int com = combine_back(j);
					if(com == -1)
					{
						return j;
					}
				}
			}
		}
	}

	return -1;
}


void work()
{
		int index = 0;
		
		memset(final,'\0',sizeof(final));

		for(int k = 0; k < N; )
		{
			int com = combine(k);
			if(com != -1)
			{
				final[index] = _c[com][2];
				index ++;
				k ++;
				k ++;
				continue;
			}
			int cle = clear(k);
			if(cle != -1)
			{
				memset(final,'\0',sizeof(final));
				index = 0;
				k = cle + 1;
			}
			else
			{
				final[index] = str[k];
				k ++;
				index ++;
			}
		}
}


int main()
{

	FILE *fp = fopen("B-small-attempt2.in","r");
	FILE *fpw = fopen("B-small-attempt2.out","w");
	

	fscanf(fp, "%d", &T);
	for(int i = 1; i <= T; i ++)
	{
		

		fscanf(fp, "%d", &C);
		for(int c = 0; c < C; c ++)
		{
			fscanf(fp, "%s", _c[c]);
		}
		fscanf(fp, "%d", &D);
		for(int d = 0; d < D; d ++)
		{
			fscanf(fp, "%s", _d[d]);
		}
		fscanf(fp, "%d", &N);
		fscanf(fp, "%s", str);

		
		
		work();
			
		

		fprintf(fpw, "Case #%d: [", i);
		if(final[0] != '\0')
		{
			fprintf(fpw,"%c",final[0]);
		}
		for(int p = 1; final[p] != '\0'; p ++)
		{
			fprintf(fpw, ", %c", final[p]);
		}
		fprintf(fpw, "]\n");

		cout<<final<<endl;
	}

		


	return 0;
}

