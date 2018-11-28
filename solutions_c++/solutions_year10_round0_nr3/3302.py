#include <stdio.h>
#include <stdlib.h>

int profit(int R, int K, int* queue, int length);
void rotate(int* q, int l) ;

int main(int argc, char *argv[]) 
{
	FILE *in=NULL,*out=NULL;
	int i=0, j=0, N, K, R, T, euros;
	int* queue;

	in   = fopen(argv[1],"r");
	out = fopen(argv[2],"w");
	if(!in || !out){    /*file opening failed*/
		return -1;
	}
	
	fscanf(in,"%d \n",&T);
	for (i=1; i<=T; ++i)
	{
		fscanf(in,"%d %d %d \n",&R,&K,&N);
		queue = (int*)malloc(sizeof(int)*N);
		for (j=0; j<N; ++j) 
		{
			fscanf(in,"%d", &(queue[j]));
		}
		fscanf(in,"\n");
		euros = profit(R, K, queue, N);
		fprintf(out,"Case #%d: %d\n", i, euros);
	}
    return 0;
}

int profit(int R, int K, int* queue, int length)
{	
	int sum=0, Ktemp=K, i=0;

	if (R == 0) return 0;

	while(Ktemp-queue[0] >= 0 && i<length) 
	{
		Ktemp -=queue[0];
		sum	  +=queue[0];
		++i;
		rotate(queue,length);
	}
	return sum+profit(R-1, K, queue, length);
}

void rotate(int* q, int l) 
{
	int i, tmp=q[0];
	for (i=0; i<l-1; ++i) 
	{
		q[i] = q[i+1];
	}
	q[l-1] = tmp;

}