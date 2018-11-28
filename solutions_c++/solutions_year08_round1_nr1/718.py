#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("ans.txt");

void sort(long long a[],int n)
{
	int temp;
	for(int i=0;i<n;i++)
		for(int j=0;j<n-1-i;j++)
		{
			if(a[j] > a[j+1])
			{
				temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;
			}
		}
}

int main()
{
	int cas;
	while(fin>>cas)
	{
		for(int output=1;output<=cas;output++)
		{
			int n;
			fin>>n;
			long long a[n],b[n];
			for(int i=0;i<n;i++)
				fin>>a[i];
			for(int i=0;i<n;i++)
				fin>>b[i];
			sort(a,n);
			sort(b,n);
			long sum=0;
			for(int i=0;i<n;i++)
			{
				//cout<<a[i]<<" "<<b[n-1-i]<<endl;
				sum += a[i]*b[n-i-1];
			}
			fout<<"Case #"<<output<<": "<<sum<<endl;
		}
	}
	return 0;
} 
