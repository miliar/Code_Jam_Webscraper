#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int Recycle(int min, int max)
{
	char buf[7];
	int counter = 0;
	if(min == max)
		return counter;

	for(int test=min; test<=max; test++)
	{
		memset(buf, 0, sizeof(buf));
		sprintf(buf, "%d", test);
		
		int size = strlen(buf);

		for (int j=0; j<size; j++)
		{
			char top = buf[0];
			for(int i=1; i<size; i++)
			{
				buf[i-1] = buf[i];
			}
			buf[size-1] = top;

			int num = atoi(buf);

			if(num < min | num > max | num == test)
				continue;
			counter++;

			//cout<<test<<" : "<<num<<endl;
		
		}
	}
	

	return counter/2;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int T;
	scanf("%d", &T);
	
	for(int i=0; i<T; i++)
	{
		int min;
		scanf("%d", &min);
		int max;
		scanf("%d", &max);

		int counter = Recycle(min, max);
		printf("Case #%d: %d\n", (i+1), counter);
		
	}

	return 0;
}