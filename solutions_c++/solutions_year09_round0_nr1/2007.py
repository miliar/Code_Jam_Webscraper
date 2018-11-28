#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

char buf[5000][15];

int L;
int D;
int N;

int checking(char*buffer)
{
	int k;
	int i;
	int x;
	char temp;
	int ans;
	int check;
	for( k = 0,ans = 0; k < D; k++)
	{
		check = 1;
		for( i = 0,x = 0; i < L ; i++)
		{
			//printf("%c %c\n",temp,buffer[x]);
			temp = buf[k][i];
			if(buffer[x] == '(')
			{
				while(buffer[x] != ')')
				{
					//printf("%c %c\n",temp,buffer[x]);
					if( temp == buffer[x] )
						break;
					x++;
				}
				if(buffer[x] == ')')
					check = 0;
				else
					while(buffer[x] != ')')
						x++;
				x++;
			}
			else if( temp == buffer[x] )
			{
				x++;
				continue;
			}
			else
				check = 0;

			if( check == 0 )
				break;
		}
		if( check == 1 )
			ans++;
	}
	return ans;
}

int main()
{
	FILE *out, *in;
	in = fopen("A-small-attempt1.in","r");
	//in = fopen("in.txt","r");
	out = fopen("output.txt","w");

	fscanf(in,"%d",&L);
	fscanf(in,"%d",&D);
	fscanf(in,"%d",&N);
	int k;
	
	char buffer[10000];
	for(k = 0; k < D; k++)
	{
		fscanf(in,"%s",buffer);
		strcpy(buf[k],buffer);
	}
	int val;
	for( k = 0; k < N; k++)
	{
		fscanf(in,"%s",buffer);
		val = checking(buffer);
		fprintf(out,"Case #%d: %d\n",k+1,val);
	}
	system("pause");
}