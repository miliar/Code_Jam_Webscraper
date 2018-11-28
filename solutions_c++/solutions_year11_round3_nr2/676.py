#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T;
	int N;
	int L;
	__int64 t;
	int C;
	int* dist=0;
	int* reserve=0;
	int* Achoose=0;
	ifstream fin;
	ofstream fout;
	fin.open("B-small.in");
	fout.open("Bsmall-answer.txt");
	fin>>T;
	dist=new int[2000000];
	reserve=new int[2000000];
	Achoose=new int[200000];
	for (int i=1;i<=T;i++)
	{
		fin>>L;
		fin>>t;
		fin>>N;
		fin>>C;
		
		for (int j=0;j<=C-1;j++)
		{
			fin>>Achoose[j];			
		}

		for (int k=0;k<=N/C;k++)
		{
			for (int j=0;j<=C-1;j++)
			{
				dist[k*C+j]=Achoose[j];
			}
		}

		for (int j=1;j<=N-1;j++)
		{
			dist[j]=dist[j-1]+dist[j];
		}

		if (t>=dist[N-1]*2)
		{
			fout<<"Case #"<<i<<": "<<dist[N-1]*2<<endl;
			continue;
		}

		int posi=-1;
		for (int j=N-1;j>=0;j--)
		{
			if (dist[j]*2<=t)
			{
				posi=j;
				break;
			}
		}

		reserve[posi+1]=dist[posi+1]-t/2;

		for (int j=posi+2;j<=N-1;j++)
		{
			reserve[j]=dist[j]-dist[j-1];
		}

		for (int j=posi+1;j<=N-2;j++)
		{
			int Big=reserve[j];
			int symbol=j;
			int temp;
			for (int k=j+1;k<=N-1;k++)
			{
				if (reserve[k]>Big)
				{
					Big=reserve[k];
					symbol=k;
				}
			}
			temp=reserve[j];
			reserve[j]=reserve[symbol];
			reserve[symbol]=temp;
		}
		int sum=2*dist[N-1];
		for (int p=0;p<=L-1;p++)
		{
			sum=sum-reserve[posi+1+p];
		}
		fout<<"Case #"<<i<<": "<<sum<<endl;
	}
	return 0;
}