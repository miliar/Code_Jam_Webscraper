#include<iostream.h>
#include<fstream.h>

void main()
{
	ifstream infile("A-small-attempt2.in");
	ofstream outfile("A.out");
	
	int temp;
	int cases,min,sum,pro;
	int n;
	int v1[8],v2[8];
	infile>>cases;
	cout<<cases<<endl;
	for(int i=0;i<cases;i++)
	{
		infile>>n;
		cout<<endl<<n<<endl;
		for(int j=0;j<n;j++)
		{
			infile>>v1[j];
			cout<<v1[j]<<' ';
		}
		for(j=0;j<n-1;j++)
			for(int k=0;k<n-1;k++)
			{
				if(v1[k]>v1[k+1])
				{
					temp=v1[k];
					v1[k]=v1[k+1];
					v1[k+1]=temp;
				}
			}
			sum=0;
			for(j=0;j<n;j++)
			{
				infile>>v2[j];
				cout<<v2[j]<<' ';
			}
			cout<<endl;
			for(j=0;j<n-1;j++)
				for(int k=0;k<n-1;k++)
				{
					if(v2[k]<v2[k+1])
					{
						temp=v2[k];
						v2[k]=v2[k+1];
						v2[k+1]=temp;
					}
				}
				for(j=0;j<n;j++)
				{
					cout<<v1[j]<<' ';
				}
				cout<<endl;
				for(j=0;j<n;j++)
				{
					cout<<v2[j]<<' ';
				}
				sum=0;
				for(j=0;j<n;j++)
				{
					pro=v1[j]*v2[j];
					sum+=pro;
				}
				cout<<endl<<sum<<endl;

		outfile<<"Case #"<<i+1<<": "<<sum<<"\n";	
			
	}
	
		
	
}