#include<iostream.h>
#include<fstream.h>

void main()
{
	ifstream infile("A-small-attempt1.in");
	ofstream outfile("B.out");
	
	int cases;
	long P,K,L;
	infile>>cases;
	cout<<cases<<endl;
	long *abc,temp;
	long sum=0,pro;
	long tem,check=0;
	for(int i=0;i<cases;i++)
	{
		infile>>P;
		infile>>K;
		infile>>L;
		abc=new long[L];
		for(int j=0;j<L;j++)
		{
			infile>>abc[j];
			cout<<abc[j]<<' ';
		}
		cout<<endl;
		for(j=0;j<(L-1);j++)
		{
			for(int k=0;k<(L-1);k++)
			{
				if(abc[k]<abc[k+1])
				{
					temp=abc[k];
					abc[k]=abc[k+1];
					abc[k+1]=temp;
				}
			}
		}
		cout<<endl;
		for(j=0;j<L;j++)
		{
			cout<<abc[j]<<' ';
		}
		sum=0;
		tem=1;
		check=0;
		for(j=0;j<L;j++)
		{
			pro=abc[j]*tem;
			sum+=pro;
			check++;
			if(check==K)
			{
				tem++;
				check=0;
			}
		}
		cout<<sum<<endl;
		outfile<<"Case #"<<i+1<<": "<<sum<<"\n";	
		
	}
	
		
	
}