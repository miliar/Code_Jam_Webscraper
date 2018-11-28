#include <stdio.h>
#include <string.h>

int ABS( int p )
{
	return ( p < 0  ? -p : p);
}

int main()
{
	int N, T, C, min, i, I, x, total;
	char ob[5];
	int pos;
	scanf("%d",&N);
	int last_b, last_o, min_b, min_o, p;
	char last;
	for(I=0; I<N; ++I)
	{
		last = ' ';
		last_b = last_o = 1;
		min_b = min_o = 0;
		// T steps
		scanf("%d",&T);
		for(i=0; i<T; ++i)
		{
			scanf("%s%d",ob,&p);
			if( ob[0] == 'O' )
			{
				if( last == 'O' )
				{
					min_o += ABS(last_o-p)+1;
					last_o = p;
				}
				else // from B
				{
					int save = ( min_o < min_b ? min_b - min_o : 0 );
					if ( ABS(last_o-p) <= save ) // if can reach within, just press
						min_o = min_b + 1; 
					else // cannot reach within save, move>save
						min_o = min_b + ABS(last_o-p) - save +1;
					//else
					//	min_o += ABS(last_o-p)+1;
					last_o = p;
				}
			}
			else // B
			{
				if( last == 'B' )
				{
					min_b += ABS(last_b-p)+1;
					last_b = p;
				}
				else
				{
					int save = ( min_b < min_o ? min_o - min_b : 0 );
					if ( ABS(last_b-p) <= save ) // if can reach within, just press
						min_b = min_o + 1; 
					else // cannot reach within save, move>save
						min_b = min_o + ABS(last_b-p) - save +1;
//					min_b = ABS(last_b-p)+1 - save;
					last_b = p;
				}
			}
			last = ob[0];
		}
		printf("Case #%d: ", I+1);
		printf("%d\n", (min_o>min_b?min_o:min_b));
	}
	return 0;
}