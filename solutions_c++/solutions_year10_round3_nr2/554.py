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
line myli[10000]; 
long long l,p,c;
int main()
{

	ifstream fin("google.in");
	ofstream fout("google.out");
	
	int t;
	fin>>t;
	for(int i=0;i<t;i++)
	{
		fin>>l>>p>>c;
		int al=0;
		if(l*c>=p)
			al=0;
		else
		{
			int temp=0;
			while(l*pow((float)c,temp)<p)
			{
				temp++;
			}
			temp--;
			al=log((float)temp)/log(2.0)+1;
		}
		fout<<"Case #"<<i+1<<": "<<al<<endl;
	}
	return 1;
}
