#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void shiftl(unsigned long * q,unsigned long N)
{
	unsigned long temp=q[0];
	for(unsigned long i=0;i<N-1;i++)
		q[i]=q[i+1];
	q[N-1]=temp;
}
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("D://a.in");
	fout.open("D://output2.txt");
	unsigned long c,R,k,N,sum,sum2;
	fin>>c;
	for(unsigned long count=1;count<=c;count++)
	{
	fin>>R>>k>>N;
	sum=0;
	sum2=0;	
	unsigned long *q=new unsigned long[N];
	for(unsigned long i=0;i<N;i++)
		fin>>q[i];
	for(unsigned long i=0;i<N;i++)
		sum2+=q[i];
	for(unsigned long i=0;i<R;i++)
	{
		unsigned long ktemp=k;
			while(q[0]<=ktemp&&((k-ktemp)<sum2))
			{
				ktemp-=q[0];
				sum+=q[0];
				shiftl(q,N);
			}
			
	}
	cout<<"Case #"<<count<<": "<<sum<<endl;
	fout<<"Case #"<<count<<": "<<sum<<endl;
	}
	cin.get();
	cin.get();
	return 0;
}