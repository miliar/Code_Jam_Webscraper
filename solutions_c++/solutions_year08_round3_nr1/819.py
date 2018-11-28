#include<stdio.h>
#include<iostream.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

int *lk;

void display(int l)
{
	for(int i=0;i<l;i++)
		printf("  %d",lk[i]);
}

void mysort(int l)
{
	int temp;
	for(int i=0;i<l;i++)
	{
		for(int j=0;j<l;j++)
		{
			if(lk[i]>lk[j])
			{
				temp = lk[i];
				lk[i]=lk[j];
				lk[j]=temp;
			}
		}
	}
}

int main()
{
	int i,n,p,k,l;
	int kc=0;
	FILE *ptr = NULL;
	
	if((ptr=fopen("Result.txt","w+"))==NULL)
	{
		cout<<"File opening Error\n";
		return -1;
	}
	
	scanf("%d",&n);

	for(i=0;i<n;i++)
	{
		scanf("%d%d%d",&p,&k,&l);
		lk = new int[l];
		for(int j=0;j<l;j++)
			scanf("%d",&lk[j]);
		mysort(l);
		display(l);

		int r=0;
		kc=0;

		for( j=1;j<=l;j++)
		{
			//if(j%k==0)
			//	r=1;
			//else
				r=j/k;
				if(j%k!=0)
					r++;

			kc = kc + lk[j-1]* r;
			printf("key %d\n",kc);

		}
		
		fprintf(ptr,"Case #%d: %d\n",(i+1),kc);
	}
	
	fclose(ptr);
	return 0;
}