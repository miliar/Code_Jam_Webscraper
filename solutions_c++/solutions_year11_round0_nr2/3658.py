#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
//#define prettyprint
#define MAX_INP_LEN 100
int C,D,N;

typedef struct t_combine
{
	char elem1,elem2,elem3;
} combine;

typedef struct t_destroy
{
	char elem1,elem2;
} destroy;


combine * combs;
destroy * dests;

char input_elems[MAX_INP_LEN+1];

char output_elems[MAX_INP_LEN+1];

char do_combine(char e1,char e2)
{
	int i;
	for (i=0;i<C;i++)
		if (((combs[i].elem1==e1) && (combs[i].elem2==e2)) ||
			((combs[i].elem1==e2) && (combs[i].elem2==e1)))
			return combs[i].elem3;

	return 0;

}

char do_destroy(char e1,char e2)
{
	int i;
	for (i=0;i<D;i++)
		if (((dests[i].elem1==e1) && (dests[i].elem2==e2)) ||
			((dests[i].elem1==e2) && (dests[i].elem2==e1)))
			return 1;

	return 0;

}

int should_clear(int size)
{
	int i,j;
	if (size == 0 || size == 1)
		return 0;
	for (i=0;i<size-1;i++)
		for (j=i+1;j<size;j++)
			if (do_destroy(output_elems[i],output_elems[j]))
				return 1;
	
	return 0;
}




int main(int argc, char * argv[])
{
	
	FILE * in, * out;
	int i,j,k,l;
	int count;
	int tasks;
	
	char name_in[256],name_out[256];

	char c1,c2,c3;

	char c;
	int pos;

	char command_str[500]; // each command takes 4, max 100 commands plus spare
	int globaltime;

	scanf("%s %s",name_in,name_out);

	in = fopen(name_in,"r");
	out = fopen(name_out,"w+");
	fscanf(in,"%d",&tasks);



	for (count=0;count<tasks;count++)
	{
		pos=0;
		C=D=N=0;
		combs=NULL;
		dests=NULL;
		strcpy(input_elems,"");
		

		fscanf(in, " %d",&C);
		if (C != 0) 
		{
			combs= (combine *)malloc(C*sizeof(combine));
			for (i=0;i<C;i++)
			{
				
				fscanf(in, " %c%c%c",&c1,&c2,&c3);
				combs[i].elem1=c1;
				combs[i].elem2=c2;
				combs[i].elem3=c3;
#ifdef prettyprint
			printf("%c and %c combine to %c\n", c1,c2,c3);
#endif
			}
		}
		
		fscanf(in, " %d",&D);	
		if (D != 0)
		{
			dests= (destroy *)malloc(D*sizeof(destroy));
		for (i=0;i<D;i++)
		{
			
			fscanf(in, " %c%c",&c1,&c2);
			dests[i].elem1=c1;
			dests[i].elem2=c2;
#ifdef prettyprint
			printf("%c and %c destroy each other\n", c1,c2);
#endif
			
		}	
		}

		fscanf(in, " %d %s",&N,input_elems);	
#ifdef prettyprint
			printf("%s elements, %d amount\n", input_elems,N);
#endif
		for (j=0;j<50;j++)
			output_elems[j]='\0';

		for (i=0;i<N;i++)
		{
		
			output_elems[pos]=input_elems[i];
			while (pos > 0 && do_combine(output_elems[pos-1],output_elems[pos]) )
				{
					output_elems[pos-1]=do_combine(output_elems[pos-1],output_elems[pos]);
					pos--;
				}
			
			if (should_clear(pos+1))
			{
				pos=0;
				for (j=0;j<50;j++)
			output_elems[j]='\0';
			}
			else
				pos++;
		}
		
		fprintf(out,"Case #%d: [",count+1);for(i=0;i<pos-1;i++) fprintf(out,"%c, ",output_elems[i]);
		if (pos>0)
			fprintf(out,"%c]\n",output_elems[pos-1]);
		else
			fprintf(out,"]\n");

		if (combs != NULL)
			free(combs);
		if (dests!=NULL)
			free(dests);

			
		}


	fclose(in);
	fclose(out);

	return 0;
}