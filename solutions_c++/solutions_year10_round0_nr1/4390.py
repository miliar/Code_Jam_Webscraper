#include<iostream.h>
#include<string.h>
void main()
{
	unsigned long int k,count;
	int t,n,status[35],power[35];
	char outp[10010][5];
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n;
		cin>>k;
		for(int j=0;j<n;j++)
		{
			status[j]=0;
			power[j]=0;
		}
		power[0]=1;
		count=0;
		while(count<k)
		{
			j=0;
			while(power[j]==1)
			{
				if(status[j]==0)
					status[j]=1;
				else
					status[j]=0;
				j++;
			}
			j=0;
			while(status[j]==1)
			{
				power[j+1]=1;
				j++;
			}
			while(j<n)
			{
				power[j+1]=0;
				j++;
			}
			power[0]=1;
			count++;
			if(status[n-1]==1&&power[n-1]==1&&count<k)
			{
			      k=k%(count+1);
			      for(int j=0;j<n;j++)
			      {
				status[j]=0;
				power[j]=0;
			      }
			      power[0]=1;
			      count=0;
			}
		}
		if(status[n-1]==1&&power[n-1]==1)
			strcpy(outp[i],"ON");
		else
			strcpy(outp[i],"OFF");
	}
	for(i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": "<<outp[i]<<"\n";
	}
}