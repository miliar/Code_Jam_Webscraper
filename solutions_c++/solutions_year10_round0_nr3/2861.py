#include<fstream.h>
#include<conio.h>
void main()
{
	int t;
	unsigned long money_[50];
	ifstream fin("c-small.in");
	ofstream fout("cc.txt");
	unsigned long R,k,N;
	unsigned long q[10000];
	fin>>t;
	for(int x=1;x<=t;x++)
	{
		unsigned int i=0;
		unsigned long money=0;
		fin>>R;
		fin>>k;
		fin>>N;
		for(long y=0;y<N;y++)
			fin>>q[y];
		for(y=1;y<=R;y++)
		{
			unsigned sum=0;
			unsigned int c=0;
			while((sum+q[i])<=k && c<N)
			{
				cout<<q[i]<<'+';
				sum+=q[i];
				i++;
				c++;
				i%=N;
			}
			cout<<endl;
			money+=sum;
		}
		money_[x-1]=money;
	}
	for(x=1;x<=t;x++)
	{
		fout<<"Case #"<<x<<": "<<money_[x-1]<<endl;
	}
	getch();
}
