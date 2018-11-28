#include<stdio.h>

#define MSIZE 100000

void quicksort(int data[MSIZE], int head, int tail)
{
	int current, target;
	int pivot, temp;
	if(head>=tail)	return;
	pivot=data[tail];
	current=target=head;
	while(current<tail)
	{
		if(data[current]<pivot)
		{
			temp=data[target];
			data[target]=data[current];
			data[current]=temp;
			target++;
		}
		current++;
	}
	data[current]=data[target];
	data[target]=pivot;
	quicksort(data, head, target-1);
	quicksort(data, target+1, tail);
}

int getMin(int va[MSIZE], int vb[MSIZE], int size)
{
	int i, sum=0;
	for(i=0; i<size; i++)	sum+=va[i]*vb[size-1-i];
	return sum;
}

void minPermute(int trial)
{

	int i, size, va[MSIZE], vb[MSIZE];
	scanf("%d", &size);
	for(i=0; i<size; i++)	scanf("%d", &va[i]);
	quicksort(va, 0, size);	
	for(i=0; i<size; i++)	scanf("%d", &vb[i]);
	quicksort(vb, 0, size);
	printf("Case #%d: %d\n", trial+1, getMin((va+1), (vb+1), size));
}

int main()
{
	int i, n;
	scanf("%d", &n);
	for(i=0; i<n; i++)	minPermute(i);
	return 0;
}