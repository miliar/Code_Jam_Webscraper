#include <stdio.h>
#include <conio.h>
#include <memory.h>

#define MAX_SNAPPER 10000

/* ON or OFF state of snapper */
int state[MAX_SNAPPER];
/* has nth snapper power */
int power[MAX_SNAPPER];
/* how many snappers we have */
int cnt_snapper;


void init()
{
	cnt_snapper = 0;
	memset( state, 0, sizeof(int) * MAX_SNAPPER );
	memset( power, 0, sizeof(int) * (MAX_SNAPPER+1) );
	power[0] = 1;
}


int snap()
{
	int i;
	int j;
	int v;


	v = 1;
	for( i=cnt_snapper-1; i>=0; i-- )
	{
		if( power[i] )
		{
			state[i] = !state[i];
		}


		v &= state[i];
	}

	for( i=0; i<cnt_snapper; i++ )
	{
		if( power[i] && state[i] )
			power[i+1] = 1;
		else
			power[i+1] = 0;
	}


	//for( i=0; i<cnt_snapper; i++ )
	//	printf("%d ", state[i]);
	//printf("\n");
	return v;
}


int main( void )
{
	int cnt_snap;
	int i;
	int j;
	int v;
	int input;
	int n,k,l;
	int res;


	scanf("%d", &input);
	
	for( l=0; l<input; l++ )
	{
		init();
		scanf("%d %d", &cnt_snapper, &cnt_snap );

		for( i=0; i<cnt_snap; i++ )
		{
			if( res = snap() )
			{
				//printf("%d\n",i+2);
				break;
			}
		}

		if( (cnt_snap+1) % (i+2) == 0 )
			res = 1;
		else
			res = 0;


		if( res )
			printf("Case #%d: ON\n", l+1 );
		else
			printf("Case #%d: OFF\n", l+1 );
	}
	//getch();
	return 0;
}