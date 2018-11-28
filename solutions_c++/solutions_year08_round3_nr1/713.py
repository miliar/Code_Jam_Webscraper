#include<stdio.h>

#define MCHAR 1000
#define MKEYS 1000
#define MALPHA 1000
/*
void quicksort(int index[MKEYS], int data[MKEYS], int head, int tail)
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
*/
int getMin(int data[MALPHA], int keys, int alpha)
{
	int sum=0, i=1, j=0, k=0;
	for(j=0; j<alpha; j++)
	{
		sum+=i*data[j];
		k++;
		if(k==keys)
		{
			k=0;
			i++;
		}
	}
	return sum;
}

void bubble(int data[MKEYS], int size)
{
	int i, j, temp;
	for(i=size-1; i>=0; i--)
	{
		for(j=0; j<i; j++)
		{
			if(data[j]<data[j+1])
			{
				temp=data[j];
				data[j]=data[j+1];
				data[j+1]=temp;
			}
		}
	}
}

void minKeyhit(int trial)
{

	int i, chars, size, alphabet, keydata[MALPHA];
	scanf("%d %d %d", &chars, &size, &alphabet);
	for(i=0; i<alphabet; i++)	scanf("%d", &keydata[i]);
	bubble(keydata, alphabet);
	if(chars*size<alphabet)		printf("Case #%d: Impossible\n", trial+1);
	else printf("Case #%d: %d\n", trial+1, getMin(keydata, size, alphabet));
}

int main()
{
	int i, n;
	scanf("%d", &n);
	for(i=0; i<n; i++)	minKeyhit(i);
	return 0;
}