#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>





void main()
{

	clrscr();
	long i,j,k,p,l,t,temp,count,x,f;
	long ans;
	long a[500];


	FILE *fp1,*fp2;


	fp1=fopen("ram.txt","r");
	fp2=fopen("rama.txt","w");

	if(fp1==NULL)
	{
		printf("Cannot find source file\n");
		exit(1);

	}

	if(fp2==NULL)
	{
		printf("Cannot open target file\n");
		exit(2);
	}

	fscanf(fp1,"%ld", &count);
	for(i=1;i<=count;i++)
	{
		t=1;
		ans=0;
		fscanf(fp1,"%ld %ld %ld",&p,&k,&l);
		for(j=0;j<l;j++)
			fscanf(fp1,"%ld", &a[j]);

		for(j=0;j<l;j++)
		{
			for(x=j+1;x<l;x++)
			{
				if(a[j]<a[x])
				{
					temp=a[j];
					a[j]=a[x];
					a[x]=temp;
				}
			}
		}



		for(j=0,f=1;j<l;j++,f++)
		{
			if(f>k)
			{
				f=1;
				t++;
			}
			ans=ans+a[j]*t;
		}
		fprintf(fp2,"Case #%d: ",i);
		fprintf(fp2,"%ld\n",ans);

	}
	getch();
}