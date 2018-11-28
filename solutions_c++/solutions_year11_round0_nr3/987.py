#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;

const int maxn = 1000;
int numbers[maxn];
int n;

void read() {
	scanf("%d",&n);
//printf("n:%d\n",n);
	for (int i=0;i<n;i++)
	{
		scanf("%d", &numbers[i]);	
//printf("i:%d numbers[i]:%d\n",i,numbers[i]);
	}
}

int main()
{
	int i,t;
	int k;
	int working;
	int sum;
	int min;
	scanf("%d",&t);
	for(i = 1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		read();
		working = numbers[0];
		sum = numbers[0];
		min = numbers[0];

		for(k=1;k<n;k++)
		{
			working = working ^ numbers[k];
			sum = sum + numbers[k];
			if(numbers[k]<min)
				min = numbers[k];
//printf("w:%d s:%d m:%d\n",working, sum, min);
		}

		if(working!=0)
			printf("NO");	
		else
			printf("%d",sum-min);
		printf("\n");
	}
	return 0;
}
