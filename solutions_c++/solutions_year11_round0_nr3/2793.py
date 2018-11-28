#include<iostream>
int partition(int p,int q,long *a)
{
	long element=a[q]; 
	for(int i=p;i<q;i++)
	{
		if(a[i]<=element)
		{
			long temp=a[p];
			a[p]=a[i];
			a[i]=temp;
			p++;
		}
	}
	long temp=a[p];
	a[p]=a[q];
	a[q]=temp;
	return p;
}
void quickImp(int p,int q,long *a)
{
	int position;
	if(p<q)
	{
		position=partition(p,q,a);
		quickImp(p,position-1,a);
		quickImp(position+1,q,a);
	}
}
void main()
{
	FILE *inFile=fopen("inputC.txt","r");
	FILE *outFile=fopen("output.txt","w");
	int T=0;
	fscanf(inFile,"%d",&T);
	for(int i=1;i<=T;i++)
	{
		int N=0;
		fscanf(inFile,"%d",&N);
		long *a=new long[N];
		for(int j=0;j<N;j++) fscanf(inFile,"%ld",&a[j]);
		quickImp(0,N-1,a);
		long max=0;
		long s=0,p=0;
		for(int j=0;j<N;j++)
		{
			s=0;
			p=0;
			long add=0;
			for(int m=0;m<=j;m++) p+=a[m];
			for(int k=j+1;k<N;k++)
			{
				add+=a[k];
				s^=a[k];
			}
			if(s==p && add>max) max=add;
		}
		if(max!=0) fprintf(outFile,"Case #%d: %d\n",i,max);
		else fprintf(outFile,"Case #%d: NO\n",i);
	}
	fclose(inFile);
	fclose(outFile);
}