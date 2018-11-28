#include<iostream>
#include<fstream>
using namespace std;
int data[14];
long a,b;
long ans;
ofstream outfile2("out.txt");

void check(long k)
{
	int x=0;
	long y=k;
	while (k!=0)
	{
		data[x]=k % 10;
		k=k/10;
		x++;
	}
    for (int i=x;i<2*x;i++) data[i]=data[i-x];
	for (int i=1;i<x;i++)
	{
		long temp=0;
		for (int j=i+x-1;j>i-1;j--)
			temp=temp*10+data[j];
		if ((temp>=a)&&(temp<=b)&&(temp>y))
		{
			ans++;
			outfile2<<y<<" "<<temp<<endl;
		}
	}
}

int main()
{
	ifstream infile("input.txt");
	ofstream outfile("output.txt");
	int t;
	infile>>t;
	for (int i=0;i<t;i++)
	{
		ans=0;
		outfile<<"Case #"<<i+1<<": ";
		infile>>a>>b;
		for (long j=a;j<=b;j++)
			check(j);
		outfile<<ans<<endl;
	}
	infile.close();
	outfile.close();
//	system("pause");
	return 0;
}