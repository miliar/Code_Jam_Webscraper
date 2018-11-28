#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <cmath>
using namespace std;
long false_add(long a,long b);
int main()
{
	ifstream infile;
	infile.open("D:\\codejam\\C-small.in",ios::binary);
	freopen("D:\\codejam\\C-small.out","wt",stdout);
	int T;
	long long ptr;
	infile>>T;
	for (int i=1;i<=T;i++)
	{
		int N;
		long false_sum=0,num=0,sum=0,smallest;
		infile>>N;
		ptr=infile.tellg();
		for (int j=1;j<=N;j++)
		{
			infile>>num;
			false_sum=false_add(false_sum,num);
			if(j==1) smallest=num;
			smallest=smallest<num?smallest*1:num;
		}
		if(!false_sum) 
		{
			infile.seekg(ptr,ios::beg);
			for( int j=1;j<=N;j++)
			{
				infile>>num;
				sum=sum+num;
			}
			sum=sum-smallest;
			cout<<"Case #"<<i<<": "<<sum<<endl;
		}
		else cout<<"Case #"<<i<<": NO"<<endl;

	}
	return 0;
}
long false_add(long a,long b)
{
	int abit=0, bbit=0;
	long sum=0;
	for(int i=0;a||b;i++)
	{
	abit=a%2; a=a/2;
	bbit=b%2; b=b/2;
	if(abit+bbit==1)
	sum=sum+pow(float(2),float(i));
	}
	return sum;
}