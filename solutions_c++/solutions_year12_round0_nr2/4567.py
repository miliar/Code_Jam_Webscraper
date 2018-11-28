#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int T,N,S,count,p,i,j,k,flag=0;
	int *trip;
	ifstream ip("B-large.in");
	ofstream op("write.txt");
	ip>>T;
	for(i=0;i<T;i++)
	{
		ip>>N;
		ip>>S;
		ip>>p;
		trip=new int[N];
		for(j=0;j<N;j++)
			ip>>trip[j];
		count=0;
		if(p==0)
			count=N;
		else
		{
			for(j=0;j<N;j++)
			{
				if(trip[j]>=p*3-2 && trip[j]>0)
					count++;
				else if(trip[j]>=p*3-4 && trip[j]>0 && S>0)
				{
					count++;
					S--;
				}
			}
		}
		op<<"Case #"<<i+1<<": "<<count<<endl;
	}
	ip.close();
	op.close();
	return 0;
}
