#include<stdio.h>
#include<string.h>



int arr[100];


int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("out1.txt", "w", stdout);

	int t, i, j, n,cs=1;
	int sean, xor1, xor2, max;

	scanf("%d", &t);

	while(t--)
	{
		scanf("%d", &n);
		for(i=0; i<n; i++)
			scanf("%d", &arr[i]);

		max = -1;
		for(i=1; i<=(1<<n)-1; i++)
		{
			sean = xor1 = xor2 = 0;

			for(j=0; j<n; j++)
			{
				if((i&(1<<j)))
				{
					xor2 ^= arr[j];

				}
				else{
					sean += arr[j];
					xor1 ^= arr[j];
				}
			}
			if( (xor1 == xor2) && sean>max )
				max = sean;
		}
		if(max == -1)
			printf("Case #%d: NO\n", cs++);
		else
			printf("Case #%d: %d\n", cs++, max);
	}
	return 0;
}