#include<iostream>
#include<fstream>
using namespace std;

void main()
{
	ifstream infile("input.txt");
	ofstream outfile("output.txt");
	int T,R,K,N,g[10];
	int i,j,k;
	int E;
	int x,y,z;
	infile>>T;
	for(i=0;i<T;i++)
	{
		infile>>R>>K>>N;
		z=0;
		for(j=0;j<N;j++)
		{
			infile>>g[j];
			z+=g[j];
		}
		if(z<=K)E=z*R;
		else
		{
			E=0;
			x=0;y=0;
			for(k=0;k<R;k++)
			{
				z=0;
				while(z<=K)
				{
					z+=g[y];
					if(y==N-1)y=0;
					else y++;
				}
				if(y==0)y=N-1;
				else y--;
				z-=g[y];
				E+=z;
			}
		}
		outfile<<"Case #"<<i+1<<": "<<E<<endl;
	}
}

