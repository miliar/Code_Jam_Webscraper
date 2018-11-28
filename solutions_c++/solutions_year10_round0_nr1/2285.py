#include  <iostream>
#include <stdio.h>
#include <math.h>
#include <fstream>
using namespace std;
long n,k;
char *a[2]={"OFF","ON"};
bool pan()
{
	k++;
	long re=1;
	for(int i=0;i<n;i++)
		re*=2;
	re--;
	if(k>>n==0)
		return false;
	int temp=k&re;
	if(temp==0)
		return true;
	return false;
}
int main()
{
	ofstream fout ("google.out");
    ifstream fin ("google.in");
	int m;
	fin>>m;
	for(int i=0;i<m;i++)
	{
		fin>>n>>k;
		if(pan())
			fout<<"Case #"<<i+1<<": "<<a[1]<<endl;
		else
			fout<<"Case #"<<i+1<<": "<<a[0]<<endl;
	}
	return 1;
}