#include<stdio.h>
#include<iostream.h>
#include<string.h>
//using namespace std;

int main(int argc, char *argv[])
{	
	FILE *fin,*fout;
	int cases;
		
	// Fetch # of Input...
	fin = fopen(argv[1],"r");
	if(fin==NULL)
	{cout<<"Unable to open INPUT File.";}
	fout = fopen(argv[2],"w");
	if(fout==NULL)
	{cout<<"Unable to open OUTPUT File.";}

	fscanf(fin,"%d",&cases);
	cout<<"cases="<<cases<<endl;

	double p,k,l;
	double fre[1000];
	int i,j,m;
	for(i=1;i<=cases;i++)
	{
		// Step_1: Input params..
		fscanf(fin, "%lf %lf %lf",&p,&k,&l);

		// Handle Special case...
		if(p*k<l)
		{
			fprintf(fout,"Case #%d: Impossible\n",i);
			continue;
		}

		// Step_2: Input frequencies...
		for(j=0;j<(int)l;j++)
		{
			fscanf(fin,"%lf",&fre[j]);
		}

		// Step_3: Sort array...
		for(j=0;j<(int)l;j++)
		{
			for(m=0;m<(int)l-1-j;m++)
			{
				if(fre[m]<fre[m+1])
				{
					double temp=fre[m];
					fre[m]=fre[m+1];
					fre[m+1]=temp;
				}
			}  cout<<fre[l-1-j]<<",";
		}


		// Get the sum...
		double ans=0.0;
		int count;
		count=(int)l/(int)k;
		cout<<"-->"<<count;
		for(j=0;j<count;j++)
		{
			for(m=1;m<=(int)k && (int)l>=j*(int)k+m;m++)
			{
				ans+=m*fre[j*(int)k+m-1];
				cout<<m*fre[j*(int)k+m-1]<<",";
			}
			cout<<endl;
		}


		// Step: Write to File
		fprintf(fout,"Case #%d: %.0lf\n",i,ans);
	}

	fclose(fin);
	fclose(fout);
	return 0;

}
