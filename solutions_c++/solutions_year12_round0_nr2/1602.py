#include<stdio.h>
#include<iostream>

using namespace std;

int array[102];

void merge(int beg,int mid, int end)
{
	int temp[102];
	int i,j,k=beg, var = mid+1;
	for(i=beg, j=mid+1;(i<=mid&&j<=end); k++)
	{
		if(array[i] > array[j])
		{
			temp[k] = array[i];
			i++;
		}
		else
		{
			//printf("%d %d %d\n",i, var,j);
			temp[k] = array[j];
			//ans += var-i;
			j++;
		}
	}
	while(i<=mid)
	{
		temp[k] = array[i];
		i++;
		k++;
	}
	while(j<=end)
	{
		temp[k] = array[j];
		j++;
		k++;
	}
	
	for(i=beg; i<=end; i++)
	{
		array[i] = temp[i];
	}
}



int mergesort(int beg, int end)
{
	int mid;
	if(end > beg)
	{
		mid = (beg+end)/2;
		mergesort(beg, mid);
		mergesort(mid+1, end);
		merge(beg, mid, end);
	}
	return 0;
}



int main()
{
	int i, count = 0, ans;
	int T, N, S, p;
	scanf("%d", &T);
	
	while(T--)
	{	
		ans = 0;
		count++;
		scanf("%d", &N);
		scanf("%d", &S);
		scanf("%d", &p);	
		mergesort(0, 5);

		for(i=0; i<N; i++)
		{
			scanf("%d", &array[i]);
		}
		mergesort(0, N-1);
		
		for(i=0; i<N; i++)
		{
			if((array[i]+2)/3 >= p)
				ans++;
			else
				break;
		}
		
		for(; i<N; i++)
		{
			if((array[i]+4)/3 >= p && S>0 && array[i]>=2)
			{
				ans++;
				S--;
			}
			else
				break;
		}
				
		cout<<"Case #"<<count<<": "<<ans<<"\n";
	}
	
	return 0;
}