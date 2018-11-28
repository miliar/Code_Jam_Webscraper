#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include <set>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("output.txt");

string str;

void addzero()
{
	int num[10]={0};
	for(int i=0;i<str.length();++i) num[str[i]-'0']++;
	num[0]++;
	int k=1;
	while(num[k]==0) ++k;
	fout<<k;
	--num[k];
	for(int i=0;i<10;++i)
		for(int j=0;j<num[i];++j) fout<<i;
	fout<<endl;
}

void work()
{
	int i;
	for(i=str.length()-1;i>0;--i) if(str[i]>str[i-1]) break;
	if(i==0)
	{addzero();
	return;
	}
	int j;
	for(j=str.length()-1;j>i-1;--j) if(str[j]>str[i-1]) break;
	char temp=str[j];
	str[j]=str[i-1];
	str[i-1]=temp;
	for(int j=i;j<str.length()-1-j+i;++j)
	{
		int temp=str[j];
		str[j]=str[str.length()-1-j+i];
		str[str.length()-1-j+i]=temp;
	}
	fout<<str<<endl;
}

int main()
{
	int t;
	fin>>t;
	for(int i=0;i<t;++i)
	{
		fout<<"Case #"<<i+1<<": ";
		fin>>str;
		work();
	}
}