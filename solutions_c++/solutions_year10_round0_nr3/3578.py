//Visual C++ 6.0
//Convert Input file to name A-small.txt and save in the same folder as the program, Output.txt will be created after execution.
#include<fstream.h>
#include<conio.h>
void main()
{ 
  int t,j,R,k,N,h,p=0,i=0,c=0,v=0;
  static int a[100000000];
	ifstream fin("A-small.txt");
	fin.seekg(0);
	fin>>t;
	ofstream fout("Output.txt");
	for(j=1;j<=t;j++)
	{
		fin>>R;
		fin>>k;
		fin>>N;
		a[N]=0;
		for(h=0;h<N;h++)
		{
			fin>>a[h];	
		}
	while(v<R)
	{
		for(i=0;(i<N && v<R);i++)
		{
			p=a[i]+p;
			if ((i+1)==N)
			{
				if((p+a[0])>k)
			{
				c=c+p;
				p=0;
				v++;
			}
			}

			else if((p+a[i+1])>k)
			{
				c=c+p;
				p=0;
				v++;
			}
			if(i==N-1 && v==0)
			{
				c=p*R;
				break;
			}
			
		}
		if(i==N-1 && v==0)
			{
				break;
			}
	}
	fout<<"Case #"<<j<<": "<<c<<"\n";
	c=0;
	v=0; p=0;
	}
}



