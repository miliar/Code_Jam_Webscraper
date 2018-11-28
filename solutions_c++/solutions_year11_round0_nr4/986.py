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
	int outoforder;
	scanf("%d",&t);
	for(i = 1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		read();
		outoforder = 0;
		
		for(k=1;k<=n;k++)
			if(numbers[k-1]!=k)
				outoforder++;

		printf("%d", outoforder);	



		printf("\n");
	}
	return 0;
}
