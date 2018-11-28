#include<stdio.h>
#include<conio.h>
#include<iostream.h>
#include<math.h>
int solve(int,long int);
int main()
{
	int n;
	long int k;
	FILE *fout,*fin;
	int temp;
	int case_n,i,j;
	fin=fopen("input.in","r");
	fout=fopen("output.in","w");

	if(fin==0)
		cout<<"File not found..";
	fscanf(fin,"%d",&case_n);
	for(i=0;i<case_n;i++)
	{
		fscanf(fin,"\n%d %ld",&n,&k);
		cout<<"\n";
		temp=solve(n,k);
		if(temp==0)
			fprintf(fout,"Case #%d: ON\n",i+1);
		else
			fprintf(fout,"Case #%d: OFF\n",i+1);
	}
	fclose(fin);
	fclose(fout);
	return(0);

}
int solve(int n,long int k)
{
	int i,j,t;
	long int p;
	p=pow(2,n);
	t=(k+1)%p;
	return(t);
}