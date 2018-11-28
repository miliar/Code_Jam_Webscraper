// Aline Numbers.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string.h>
#include <assert.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

int findmax(int f,const vector<long> & a,const int &len)
{//找mod最大,返回其符号
	if(f<0)
	{
		long t=0;
		int j=-1;
		for(int i=0;i<len;i++)
		{
			if(a[i]<t)
			{
				t=a[i];
				j=i;
			}
		}
		return j;	
	}
	if(f>0)
	{
		long t=0;
		int j=-1;
		for(int i=0;i<len;i++)
		{
			if(a[i]>t)
			{
				t=a[i];
				j=i;
			}
		}
		return j;	
	}
}

int findmin(int f,const vector<long> & a,const int &len)
{//找mod最大,返回其符号
	if(f>0)
	{
		long t=100000;
		int j=-1;
		for(int i=0;i<len;i++)
		{
			if(a[i]>0 && a[i]<t)
			{
				t=a[i];
				j=i;
			}
		}
		return j;	
	}
	if(f<0)
	{
		long t=-100000;
		int j=-1;
		for(int i=0;i<len;i++)
		{
			if(a[i]<0 && a[i]>t)
			{
				t=a[i];
				j=i;
			}
		}
		return j;	
	}
}
long findzero(const vector<long> a,const int len)
{
	for(int i=0;i<len;i++)
	{
		if(0==a[i]) return i;
	}
	return  -1;	
}

void test_i(ofstream &outFile,
			const long tm,//第i个用例
			vector<long> &a,
			vector<long> &b,
			int &len   //len3进制
			)
{
	outFile<<"Case #"<<tm<<": ";
	/////////////////////////////
	long sum=0;
	int i,j;
	while(len)
	{
		if(1==len)
		{
			sum+=a[0]*b[0];
			break;
		}
		i=findmax(1,a,len);
		if(i!=-1)
		{
			j=findmax(-1,b,len);
			if(j!=-1)
			{
				sum+=a[i]*b[j];
				a.erase(a.begin()+i);
				b.erase(b.begin()+j);
				len--;
				continue;
			}
			else
			{
				j=findzero(b,len);
				if(j!=-1)
				{
					a.erase(a.begin()+i);
					b.erase(b.begin()+j);
					len--;
					continue;
				}
				else
				{
					j=findmin(1,b,len);
					sum+=a[i]*b[j];
					a.erase(a.begin()+i);
					b.erase(b.begin()+j);
					len--;
					continue;
				}				
			}
		}
		else
		{
			i=findmax(-1,a,len);
			if(i!=-1)
			{
				j=findmax(1,b,len);
				if(j!=-1)
				{
					sum+=a[i]*b[j];
					a.erase(a.begin()+i);
					b.erase(b.begin()+j);
					len--;
					continue;
				}
				else
				{
					j=findzero(b,len);
					if(j!=-1)
					{
						a.erase(a.begin()+i);
						b.erase(b.begin()+j);
						len--;
						continue;
					}
					else
					{
						j=findmin(-1,b,len);
						sum+=a[i]*b[j];
						a.erase(a.begin()+i);
						b.erase(b.begin()+j);
						len--;
						continue;
					}				
				}
			}
			else
				break;
		}
		
	}
//	outFile.setf(ios::dec);
	char buf[10]={0};
	itoa(sum,buf,10);
	
	outFile<<buf<<endl;
}


long _tmain(long argc, _TCHAR* argv[])
{
	locale loc = locale::global(locale(""));
	ifstream inFile("C:\\Documents and Settings\\Administrator\\桌面\\GOOGLE_JAM\\a.in");
	if(!inFile)
	{
		cerr<<"ifstream error!"<<endl;
		return 1;
	}
	ofstream outFile("C:\\Documents and Settings\\Administrator\\桌面\\GOOGLE_JAM\\out.txt");
	if(!outFile)
	{
		cerr<<"ofstream error!"<<endl;
		return 1;
	}
	locale::global(loc);

	long N;
	inFile>>N;


	long i=1;
	for(;i<=N;i++)
	{
		int wei;
		inFile>>wei;
		vector<long> a;
		vector<long> b;
		int j;
		long t;
		for(j=0;j<wei;j++)
		{		
			inFile>>t;
			a.push_back(t);			
		}
		for(j=0;j<wei;j++)
		{
			inFile>>t;
			b.push_back(t);	
		}
		::test_i(outFile,i,a,b,wei);
	}	
	return 0;
}


