#include <iostream>
#include<stdio.h>
using namespace std;
int main()
{

	int  T,N,K,i,j,Q[1000],R,k;
	long long sum=0;
	scanf("%d",&T);
	for (i=0 ;i < T ; i++)
	{
		sum =0;
		int index =0;
		scanf("%d%d%d",&R,&k,&N);
		for(j= 0; j< N;j++)
		{
			scanf("%d",&Q[j]);
		}
		for(j=0; j < R ;j++)
		{
			int b = 0;
			int startindex = index;
			bool first = 1;
			while(1)
			{
				if ( ((b + Q[index])  <= k)  && (( startindex != index) || first)) 
				{
					b += Q[index];
					index = (index + N+ 1) % N;
					first = 0;

				}
				else
				{
					sum += b;
					break;
				}
			}
			if( index == 0)
			{
				int chunk = R/(j+1);
				j=(chunk * (j+1))-1;
				sum *=chunk;
			}
		}
		cout<<"Case #"<<i+1<<":"<<" "<<sum<<endl;
	}
}
