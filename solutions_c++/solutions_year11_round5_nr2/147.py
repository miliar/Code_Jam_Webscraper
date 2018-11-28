#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

#define Max 10005
using namespace std;

int arr[Max];
int ct[Max];
int arr2[Max];

int main()
{
	int z, zi, i, j, ans, n, an, t;
	
	scanf("%d", &z);

	for(zi=1;zi<=z;zi++)
	{
		scanf("%d", &n);

		memset(ct, 0, sizeof(ct));
		for(i=0;i<n;i++)
		{
			scanf("%d", &arr[i]);
			ct[ arr[i] ]++;
		}


		an = 0;
		for(j=1;j<Max;j++)
		{
			t = ct[j] - ct[j-1];

			while(t > 0)
				arr2[an++] = j, t--;

			while(t < 0)
				arr2[an++] = -j, t++;
		}

		/*for(i=0;i<an;i++)
			printf("%d ", arr2[i]);
		printf("\n");*/


		ans = n;
		for(i=0, j=0;i<an;i++)
		{
			if(arr2[i] < 0)
			{
				while(j<an && arr2[j] <= 0)
					j++;

				//cout<<"!!"<<arr2[i]<<" "<<arr2[j]<<"\n";
				//cout<<"!"<<j<<" "<<i<<"\n";

				ans = min(abs(arr2[i]) - abs(arr2[j]), ans);

				arr2[i] = arr2[j] = 0;
			}
		}
		printf("Case #%d: %d\n", zi, ans);
	}
}
