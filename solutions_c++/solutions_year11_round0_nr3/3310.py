#include<iostream>
using namespace std;

int patrick(int* a,int s,int e)
{
	int i,sum=0;
	for(i=s;i<=e;i++)
		sum=sum^a[i];

	return sum;

}
int sean(int * a, int s, int e)
{
	int i,sum=0;
	for(i=s;i<=e;i++)
		sum=sum+a[i];

	return sum;

}
int main()
{
	int t,total,n,i,j;

	FILE * fp,*fp1;
	fp=fopen("C-large.in","r");
	fp1=fopen("OUTPUT C-large.txt","w");
	fscanf(fp,"%d",&t);
	
	total=t;
	
	while(t--)
	{
		fscanf(fp,"%d",&n);
		int max=0;
		int * a = new int[n];
		for(i=0;i<n;i++)
		{
			fscanf(fp,"%d",&a[i]);
		}
		
		for(i=0;i<n-1;i++)
			
		{
			if(patrick(a,0,i)==patrick(a,i+1,n-1))

			{
				int l= sean(a,0,i);
				int r = sean(a,i+1,n-1);
				int max1=l>r?l:r;
				if(max1>max)
					max=max1;

			}
		}


		for(i=0;i<n-2;i++)
			for(j=i+1;j<n-1;j++)
		{
			if(patrick(a,i+1,j)==(patrick(a,0,i)^patrick(a,j+1,n-1)))

			{
				int l= sean(a,i+1,j);
				int r = sean(a,0,i)+sean(a,j+1,n-1);
				int max1=l>r?l:r;
				if(max1>max)
					max=max1;

			}
		}

		
		if(max==0)
			fprintf(fp1,"Case #%d: NO\n",total-t);
		else

	fprintf(fp1,"Case #%d: %d\n",total-t,max);

	}
	fclose(fp);
	fclose(fp1);
	return 0;
}