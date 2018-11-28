#include <fstream>
using namespace std;

int main()
{
	ifstream inf;
	ofstream outf;
	inf.open("A-large.in");
	outf.open("A-large.out");
	int i,j,k,L,D,N,t,count,flag;
	char array[5000][15];
	int b[5000];
	char pattern[421];
	inf>>L>>D>>N;
	for(i=0;i<D;i++)
		for(j=0;j<L;j++)
			inf>>array[i][j];
	for(i=0;i<N;i++)
	{
		inf>>pattern;
		for(j=0;j<D;j++)	b[j]=0;
		t=count=flag=0;
		while(count<L)
		{
			if(pattern[t]=='(')
			{t++;flag=1;continue;}
			else if(pattern[t]==')')
			{t++;flag=0;count++;continue;}
			else{
				for(j=0;j<D;j++)
				if(array[j][count]==pattern[t]) b[j]++;
				if(flag==0) count++;
			}
			t++;
		}
		count=0;
		for(j=0;j<D;j++)
			if(b[j]==L)	count++;
		outf<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}
