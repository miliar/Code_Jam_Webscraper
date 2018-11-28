#include<iostream>
int partition(int p,int q,int *a)
{
	int element=a[q]; 
	for(int i=p;i<q;i++)
	{
		if(a[i]<=element)
		{
			int temp=a[p];
			a[p]=a[i];
			a[i]=temp;
			p++;
		}
	}
	int temp=a[p];
	a[p]=a[q];
	a[q]=temp;
	return p;
}
void quickImp(int p,int q,int *a)
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
	FILE *inFile=fopen("inputG.txt","r");
	FILE *outFile=fopen("output.txt","w");
	int T=0;
	fscanf(inFile,"%d",&T);
	for(int i=1;i<=T;i++)
	{
		int N=0;
		fscanf(inFile,"%d",&N);
		int *original=new int[N];
		int *sorted=new int[N];
		int hits=0;
		for(int j=0;j<N;j++)
		{
			fscanf(inFile,"%d",&original[j]);
			sorted[j]=original[j];
		}
		quickImp(0,N-1,sorted);
		for(int j=0;j<N;j++) if(sorted[j]!=original[j]) hits++;
		fprintf(outFile,"Case #%d: %f\n",i,(double)hits);
	}
	fclose(inFile);
	fclose(outFile);
}