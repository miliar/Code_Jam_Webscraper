#include<iostream.h>
#include<fstream.h>
#include<string.h>
void main()
{
	ifstream infile("A-large.in");
	ofstream outfile("Asfia.out");
	
	int cases;
	int Q;
	int S;
	char *se[101];
	char *qe[1002];
	infile>>cases;
	for(int i=0;i<cases;i++)
	{
		infile>>S;
		for(int j=0;j<=S;j++)
		{
			se[j]=new char[101];
			infile.getline(se[j],101);
		}
		infile>>Q;
	
		cout<<Q<<endl;
		for(j=0;j<=Q;j++)
		{
			qe[j]=new char[101];
			infile.getline(qe[j],101);
		}
		int *count;
		count=new int[S+1];
		int lcount=1;
		int index=1;
		int switch1=0,ind=1;
abc:
		for(j=1;j<=S;j++)
		{
			count[j]=Q+1;
			for(int k=ind;k<=Q;k++)
			{
				if(!(strcmp(se[j],qe[k])))
				{
					count[j]=k;
					break;
				}
			}
			if(j==1)
				lcount=count[j];
			else
			if(count[j]>lcount)
			{
				lcount=count[j];
			}
			
		}
		if(lcount!=(Q+1))
		{
			switch1++;
			ind=lcount;
			goto abc; 
		}
		outfile<<"Case #"<<i+1<<": "<<switch1<<"\n";
	}
}