#include<stdio.h>
#include<string.h>

int counter = 0;
char sent[20];
char line[500];
int values[500];
int lenght = 0;
int rec(int,int);
int main()
{
	sprintf(sent,"%s","welcome to code jam");
	FILE *fin = fopen("small.in","r");
	FILE *fout = fopen("small.out","w");
	int cases = 0;
	fscanf(fin,"%d\n",&cases);
	for(int i = 0; i < cases;i++)
	{
		counter = 0;
		for(int x = 0;x < 500;x++)
			values[x] = 0;
		int j;
		for(j = 0;;j++)
		{
			char x;
			fscanf(fin,"%c",&x);
			if (x != '\n')
			{
				line[j] = x;
			}
			else
			{
				break;
			}
		}
		line[j] = '\0';
		lenght = strlen(line);
		rec(0,0);
		int number = 0;
		number = counter%10000;
		fprintf(fout,"Case #%d: %04d\n",i+1,counter);
	}
}

int rec(int position,int next)
{
	if (next == 19)
	{
		counter ++;
		return 0;
	}
	if (position == lenght)
		return 0;
	if (line[position] == sent[next])
	{
		rec(position + 1,next + 1);
		rec(position + 1,next);
	}
	else
		rec(position + 1,next);
}