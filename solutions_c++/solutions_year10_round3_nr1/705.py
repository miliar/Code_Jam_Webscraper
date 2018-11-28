#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
int n;
struct line
{

	int a,b;
};
int cmp(const void *a,const void *b)
{
	return (*(line *)a).a-(*(line *)b).a;
}
line myli[1000]; 

int main()
{

	ifstream fin("google.in");
	ofstream fout("google.out");
	
	int t;
	fin>>t;
	for(int i=0;i<t;i++)
	{
		fin>>n;
		for(int j=0;j<n;j++)
			fin>>myli[j].a>>myli[j].b;
		qsort(myli,n,sizeof(line),cmp);
		int al=0;
		for(int te=0;te<n;te++)
		{
			for(int te1=te+1;te1<n;te1++)
			{
				if(myli[te1].b<myli[te].b)
					al++;
			}
		}
		fout<<"Case #"<<i+1<<": "<<al<<endl;
	}
	return 1;
}
