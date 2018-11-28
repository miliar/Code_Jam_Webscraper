//#include "stdlib.h"
#include "stdio.h"

#define N 100



int calculate(int *o, int *b, int oMax, int bMax, int *Key)
{
	int time = 0;
	int i = 0, j = 0;
	int oStep = 0,bStep = 0;
	bool push = false;
	bool stop = true;
	int indexKey = 0;

	while(oMax != 0 || bMax != 0)
	{
		if ( oMax )
		{
			if( oStep == o[i] )
			{
				if( push == false && Key[indexKey] == 0 )
				{
					i++;
					oMax--;
					indexKey++;
					push = true;
				}
			}
			else
			{
				if( oStep < o[i])
					oStep++;
				else
					oStep--;
			
			}
		}
		//-----------------------------------------	
		if ( bMax )
		{
			if( bStep == b[j] )
			{
				if( push == false && Key[indexKey] == 1 )
				{
					
					j++;
					bMax--;
					indexKey++;
					push = true;
				}
			}
			else
			{
				if( bStep < b[j])
					bStep++;
				else
					bStep--;
			
			}
		}
		time++;
		push = false;
			
	}

	return time;
}


void main()
{
	FILE *in, *out;
	int *orange = new int[N];
	int *blue	= new int[N];
	int T = 0;
	int time;

	for( int i = 0; i < N; i++)
	{
		orange[i] = blue[i] = 0;
	}

	in = fopen("test.in","r");
	out= fopen("test.out","w");
	fscanf(in,"%d", &T);

	for(int i = 0; i < T; i++)
	{
		int oCount=0,bCount=0;
		int sizeCode;
		fscanf(in,"%d", &sizeCode);
		int *Key = new int[sizeCode];

		for(int j = 0; j < sizeCode; j++)
		{
			char type;
			int number;
			
			do
			{
			fscanf(in,"%c",&type);
			}
			while(type == ' ');
			if ( type == 'O' )
			{
				fscanf(in,"%d", &number);
				orange[oCount] = number-1;
				oCount++;
				Key[j] = 0;
			}
			if ( type == 'B' )
			{
				fscanf(in,"%d", &number);
				blue[bCount] = number-1;
				bCount++;
				Key[j] = 1;
			}		
		}
		time = calculate(orange,blue,oCount,bCount,Key);
		fprintf(out,"Case #%d: %d\n",i+1,time);
	}
	fclose(in);
	fclose(out);
}