#include<iostream>
#include<cstdio>
#include<math.h>
#include<string.h>
#include<stdlib.h>

using namespace std;

int difference (int a,int b)
{
	if(a>=b)
		return a-b;
	else
		return b-a;
}


int main()
{
	int ch;
	cin>>ch;
	for(int z=1;z<=ch;z++)
	{
		int num;
		cin>>num;
		int arr[200];
		char brr[200];
		for(int i=1;i<=num;i++)
		{
			getchar();
			cin>>brr[i]>>arr[i];
		}
		//for(int i=1;i<=num;i++)
		//cout<<brr[i]<<" "<<arr[i]<<endl;
		int poso=1,posb=1;
		int currpos=1;
		int time=0;
		while(currpos<=num)
		{
			if(brr[currpos]=='O')
			{
				int bandwidth=difference(poso,arr[currpos]);
				time+=bandwidth+1;
				bandwidth++;
				poso=arr[currpos];
				for(int i=currpos+1;i<=num;i++)
				{
					if(brr[i]=='B')
					{
						int bandwidth2=difference(posb,arr[i]);
						if(bandwidth2<=bandwidth)
							posb=arr[i];
						else
						{
							if(arr[i]>posb)
								posb+=bandwidth;
							else
								posb-=bandwidth;
						}
						break;
					}
				}
			}
			if(brr[currpos]=='B')
			{
				int bandwidth=difference(posb,arr[currpos]);
				time+=bandwidth+1;
				bandwidth++;
				posb=arr[currpos];
				for(int i=currpos+1;i<=num;i++)
				{
					if(brr[i]=='O')
					{
						int bandwidth2=difference(poso,arr[i]);
						if(bandwidth2<=bandwidth)
							poso=arr[i];
						else
						{
							if(arr[i]>poso)
								poso+=bandwidth;
							else
								poso-=bandwidth;
						}
						break;
					}
				}
			}
			currpos++;
		}
		
			cout<<"Case #"<<z<<": "<<time<<endl;
		
	}
	return 0;
}
