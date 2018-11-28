#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int N; // number of commands

typedef struct t_bot {
	
	char color; // O or B
	int currpos; //1 : 100
	int at_button;
	int direction; // -1 or 1
	int next;
} bot;

int sign(int x)
{
	if (x >=0 ) return 1;
	if (x < 0 ) return -1;
}

typedef struct t_order
{
	char color;
	int position;
} order;

bot Orange;
bot Blue;

order * orders;
int currentOrder;


int next_B_order(int size)
{
	int i;
	for (i=currentOrder+1;i<size;i++)
		if (orders[i].color == 'B')
			return orders[i].position;

	return -1;
}

int next_O_order(int size)
{
	int i;
	for (i=currentOrder+1;i<size;i++)
		if (orders[i].color == 'O')
			return orders[i].position;

	return -1;
}



int main(int argc, char * argv[])
{
	
	FILE * in, * out;
	int i,j,k,l;
	int count;
	int tasks;
	
	char name_in[256],name_out[256];

	char c;
	int pos;

	char command_str[500]; // each command takes 4, max 100 commands plus spare
	int globaltime;

	scanf("%s %s",name_in,name_out);

	in = fopen(name_in,"r");
	out = fopen(name_out,"w+");
	fscanf(in,"%d",&tasks);

	Orange.color='O';
	Orange.at_button=0;
	Orange.currpos=1;
	Orange.direction=1;

	Blue.color='B';
	Blue.at_button=0;
	Blue.currpos=1;
	Blue.direction=1;
	


	for (count=0;count<tasks;count++)
	{
		Orange.color='O';
		Orange.at_button=0;
		Orange.currpos=1;
		Orange.direction=1;

		Blue.color='B';
		Blue.at_button=0;
		Blue.currpos=1;
		Blue.direction=1;
		
		
		globaltime=0;
		fscanf(in,"%d",&N);
		orders = (order * ) malloc(N*sizeof(order));
		currentOrder=0;
		
		for (i=0;i<N;i++) {
			fscanf(in," %c %d",&c,&pos);
			orders[i].color=c;
			orders[i].position=pos;
#ifdef prettyprint
		printf("color %c\t position %d\n",orders[i].color,orders[i].position);
#endif
		}
		
		
		while (currentOrder < N)
		{
			if (orders[currentOrder].color=='O')
			{
				if (next_B_order(N) != -1) {
				if(Blue.currpos != next_B_order(N)) {
					Blue.currpos+=sign(next_B_order(N)-Blue.currpos);
#ifdef prettyprint
					printf("Blue moves toward button %d at time %d\n",next_B_order(N),globaltime);
#endif 
				}
				else
				{
#ifdef prettyprint
					printf("Blue stays in place %d at time %d\n",Blue.currpos,globaltime);
#endif 
				}
				}

				if (Orange.currpos == orders[currentOrder].position)
				{
#ifdef prettyprint
					printf("Orange bot pressing button %d at time %d\n",orders[currentOrder].position,globaltime);
#endif 
				   currentOrder++;
				  			   
				}
				else
				{
					Orange.currpos+=sign(orders[currentOrder].position-Orange.currpos);
#ifdef prettyprint
					printf("Orange moves toward button %d at time %d\n",orders[currentOrder].position,globaltime);
#endif 
				}

			}

/**** 
* Blue
*
*
*****/



			else if (orders[currentOrder].color=='B')
			{
				if (next_O_order(N) != -1) {
				if(Orange.currpos != next_O_order(N)) {
					Orange.currpos+=sign(next_O_order(N)-Orange.currpos);
#ifdef prettyprint
					printf("Orange moves toward button %d at time %d\n",next_O_order(N),globaltime);
#endif 
				}
				else
				{
#ifdef prettyprint
					printf("Orange stays in place %d at time %d\n",Orange.currpos,globaltime);
#endif 
				}
				}

				if (Blue.currpos == orders[currentOrder].position)
				{
#ifdef prettyprint
					printf("Blue bot pressing button %d at time %d\n",orders[currentOrder].position,globaltime);
#endif 
				   currentOrder++;
				  			   
				}
				else
				{
					Blue.currpos+=sign(orders[currentOrder].position-Blue.currpos);
#ifdef prettyprint
					printf("Blue moves toward button %d at time %d\n",orders[currentOrder].position,globaltime);
#endif 
				}

			}


			globaltime++;
			
		}

#ifdef prettyprint
					printf("Orders done in %d\n",globaltime);
#endif 
	
		fprintf(out,"Case #%d: %d\n",count+1,globaltime);
		free(orders);
	}
	
	fclose(in);
	fclose(out);
	

	return 0;
}