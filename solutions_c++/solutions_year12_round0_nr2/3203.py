#include<iostream>
#include<fstream>
using namespace std;

int main()
{
int testcase=0,n=0,s=0,p=0,arr[100],q=0,count=0,flag=0,scount=0,k=0;

FILE *fp,*fp1;
fp=fopen("B-large.in","r");
fp1=fopen("ok.txt","w");

fscanf(fp,"%d\n",&testcase);
while(testcase--)
{
	fscanf(fp,"%d %d %d ",&n,&s,&p);
	scount=0;
	for(int z=0;z<n-1;z++)
	{
		fscanf(fp,"%d ",&arr[z]);
	}
	fscanf(fp,"%d\n",&arr[n-1]);
	for(int i=0;i<n;i++)
	{
	   if((arr[i]+1)%3==0)
		{
			q=(arr[i]+1)/3;
			if(q>=p)
			{	count++;			
				flag=1;
			}
		}
		else if((arr[i]-1)%3==0)
		{
			q=(arr[i]-1)/3;
			if(q+1>=p)
			{	count++;			
				flag=1;
			}
		}
		else if((arr[i])%3==0)
		{
			q=(arr[i])/3;
			if(q>=p)
			{	count++;			
				flag=1;
			}
		}
		if(flag==0 &&scount<s)
		{
			if((arr[i]+2)%3==0)
			{
				q=(arr[i]+2)/3;
				if(q>=p)
				{
					count++;
					scount++;
				}
				
			}
			else if((arr[i]-2)%3==0)
			{
				q=(arr[i]-2)/3;
				if(q+2>=p)
				{
					count++;
					scount++;
				}
				
			}
			else if((arr[i]-3)%3==0)
			{
				q=(arr[i]-3)/3;

				if(arr[i]==0 && p>0)
				{
					continue;
				}
				else if(q+2>=p)
				{
					count++;
					scount++;
				}
				
			}
		}
		flag=0;

	}
	k++;
	fprintf(fp1,"Case #%d: %d\n",k,count);
	count=0;

}
	//cin>>testcase;
	return 0;
}
