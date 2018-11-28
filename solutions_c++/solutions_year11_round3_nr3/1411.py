#include<iostream>
using namespace std;
int main()
{

int t,total;
	FILE * fp,*fp1;
	fp=fopen("C-small-attempt2.in","r");
	fp1=fopen("OUTPUT c-small2.txt","w");
	
	fscanf(fp,"%d",&t);
	
	total=t;


	while(t--)
	{
		int n,l,h,i,j,flag;

		fscanf(fp,"%d",&n);

		fscanf(fp,"%d",&l);
		fscanf(fp,"%d",&h);
		int *freq=new int[n];
		for(i=0;i<n;i++)
		{
			fscanf(fp,"%d",&freq[i]);
		}


		for(i=l;i<=h;i++)
		{
			flag=0;
			for(j=0;j<n;j++)
			{
				if(i>freq[j])

				{
					if(i%freq[j]!=0)
					{
					flag=1;
					break;
					}
				}
				else
				{
					if(freq[j]%i!=0)
					{
					flag=1;
					break;
					}

				}
			}

			if(flag==0)
			{
				break;
			}
		}

		
		fprintf(fp1,"Case #%d: ",total-t);
		if(i==h+1)
		{
			fprintf(fp1,"NO\n");
		}
		else
		{
			fprintf(fp1,"%d\n",i);
		}



	}
	return 0;
}