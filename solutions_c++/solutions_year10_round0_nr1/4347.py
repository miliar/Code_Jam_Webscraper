//Made Using Visual C++ 6.0
//Convert Input file to name A-small.txt and save in the same folder as the program, Output.txt will be created after execution.
#include<fstream.h>
#include<conio.h>
void main()
{ int i=0,t,g,N,j,a[30];
static int k;
char ch;
	ifstream fin("A-small.txt");
	fin.seekg(0);
	fin>>t;
	fin.get(ch);
	ofstream fout("Output.txt");
	for(g=1;g<=t;g++)
	{
		fin>>N;
		fin.get(ch);
		fin>>k;
		fin.get(ch);
		a[0]=1;
		for(i=1;i<N;i++)
			a[i]=0;
		for(i=1;i<=k;i++)
		{
			if(a[0]==1)
				a[0]=2;
			else
				a[0]=1;
			for(j=1;j<N;j++)
			{ 
				if((a[j-1]==1 && a[j]==2)||(a[j-1]==0 && a[j]==2))
					a[j]=0;
				else if((a[j-1]==2 && a[j]==1)||(a[j-1]==2 && a[j]==3))
					a[j]=2;
				else if((a[j-1]==1 && a[j]==1)||(a[j-1]==0 && a[j]==1))
					a[j]=3;
				else if(a[j-1]==2 && a[j]==0)
					a[j]=1;
				else
					continue;
			}
		}
		
		if(a[N-1]==2)
			fout<<"Case #"<<g<<": ON\n";
		else
			fout<<"Case #"<<g<<": OFF\n";
	}
	cout<<"\n\n";
}