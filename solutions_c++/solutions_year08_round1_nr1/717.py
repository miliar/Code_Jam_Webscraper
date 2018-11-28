#include <cstdio>

int T, n;
int X[800];
int Y[800];
bool isUse[800];
int min;
int result;

void InputData()
{
	scanf("%d", &n);

	for(int i = 0; i < n; i++ ) scanf("%d", &X[i]);
	for(int i = 0; i < n; i++ ) scanf("%d", &Y[i]);
	for(int i = 0; i < n; i++ ) isUse[i] = false;

	min = 100000000;
	result = 0;
}

int GetResult(int index)
{
	if( index == n )
	{
		if( result < min ) min = result;
		return 0;
	}

	for(int i = 0; i < n; i++ )
	{
		if( isUse[i] == false )
		{
			isUse[i] = true;
			result += X[index] * Y[i];

			GetResult(index+1);

			result -= X[index] * Y[i];
			isUse[i] = false;
		}
	}

	return 1;
}

int main()
{
	int count = 1;

	scanf("%d", &T);

	while( T --> 0 )
	{
		InputData();
		GetResult(0);
		printf("Case #%d: %d\n", count, min);

		count++;
	}

	return 0;
}
