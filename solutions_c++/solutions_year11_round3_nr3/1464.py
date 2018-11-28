#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include   <iomanip>
#include <algorithm>
#include <map>
using namespace std;
long long table[20000];
long long table1[20000];
long long table2[20000];
int cmp(const void  *a,const void *b)
{

	if((*(long long *)a-*(long long *)b)>0)
		return 1;
	else
		return -1;
}

long long gcd(long long x,long long y)//¹«Ô¼
{
	long long temp;
	if(x<y)temp=x,x=y,y=temp;
	if(x%y==0)return y;
	else
		return gcd(y,x%y);
}
long long getM(long long a,long long b)
{
	long long temp=gcd(a,b);
	a/=temp;
	return a*b;
}
bool isf(long long a,long long b)
{
	if(a%b==0||b%a==0)
		return true;
	return false;
}
int main() {
	ofstream fout ("test.out");
	ifstream fin ("test.in");
	int t;
	fin>>t;
	for(int z=0;z<t;z++)
	{
		long long result=10e17;
		long long n,l,u;
		fin>>n>>l>>u;
		for(long long i=0;i<n;i++)
		{
			fin>>table[i];
		}
		bool isr=true;
		for(long long i=l;i<=u;i++)
		{
			isr=true;
			for(int j=0;j<n;j++)
			{
				if(!isf(i,table[j]))
				{
					isr=false;
					break;
				}
			}
			if(isr==true)
			{
				result=i;
				break;
			}
		}
		if(isr==false)
			fout<<"Case #"<<z+1<<": NO"<<endl;
		else
			fout<<"Case #"<<z+1<<": "<<result<<endl;
		result=10e17;
		qsort(table,n,sizeof(table[0]),cmp);
		table1[0]=table[0];
		int h=0;
		for(long long i=1;i<n;i++)
		{
			table1[i]=getM(table[i],table1[i-1]);
			if(table1[i]<=0||table1[i]>10e16||table[i]>u)
			{
				break;
			}
			h=i;
		}
		table2[n-1]=table[n-1];
		for(long long i=n-2;i>=0;i--)
		{
			table2[i]=gcd(table[i],table2[i+1]);
		}
		for(long long i=0;i<=h;i++)
		{
			if(table2[i+1]%table1[i]==0&&table1[i]<table[i+1])
			{
				if(table1[i]>=l&&table1[i]<=u)
				{
					result=result>table1[i]? table1[i]:result;
				}
			}
		}
		if(table1[n-1]>=l&&table1[n-1]<=u)
			result=result>table1[n-1]? table1[n-1]:result;
		if(table2[0]>=l&&table2[0]<=u)
			result=result>table2[0]? table2[0]:result;

		//if(result==10e17)
		//	fout<<"Case #"<<z+1<<": NO"<<endl;
		//else
		//	fout<<"Case #"<<z+1<<": "<<result<<endl;

	}


	return 0;
}