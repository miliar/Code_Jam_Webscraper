#include<iostream>
#include<fstream>
using namespace std;

void descending(int *a,int n)
{
	long int temp;
	for(int i=0;i<n;i++)
	{
		for(int j=i;j<n;j++)
		{
			if(a[i]<a[j])
			{
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}
	}
}

int main()
{
	ifstream fin;
	fin.open("A-small-attempt0.in");
	ofstream fout;
	fout.open("outfile.txt");
	
	int N;
	fin>>N;
	
	for(int z=0;z<N;z++)
	{
		int P,K,L;
		fin>>P>>K>>L;
		
		int *freq=new int[L];
		for(int i=0;i<L;i++)
		fin>>freq[i];
		
		descending(freq,L);
		
		int k=0;
		int count=0;
		int mul=1;
		bool soln=1;
		for(int i=0;i<L;i++)
		{
			if(k<K)
			{
				count+=mul*freq[i];
				k++;
			}
			else
			{
				k=0;
				mul++;
				i--;
				if(mul>P)
				soln=0;	
			}
		}
		delete [] freq;
		
		if(soln)
		fout<<"Case #"<<z+1<<": "<<count<<endl;
		else
		fout<<"Case #"<<z+1<<": Impossible"<<endl;
	}
    cout<<endl;
    system("pause");
    return 0;
}
