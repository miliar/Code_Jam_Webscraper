#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
int o,n;
char da[10900][1009];
int re(char *a,char *b)
{
	int l1=strlen(a);
	int l2=strlen(b);
	int i;
	bool m=false;
	for(i=0;i<l1&&i<l2;i++)
	{
		if(a[i]!=b[i])
		{
			m=true;
			break;
		}
	}
	if(m==false)
	{
		if(l2<l1)
		{
			if(a[i]==47)
				return 0;
			else
				return 1;
		}
		if(l2==l1)
			return 0;
		if(l2>l1)
		{
			int re=0;
			for(int j=i;j<l2;j++)
				if(b[j]==47)
					re++;
			if(b[i]!=47)
				re++;
			return re;
		}
	}
	else
	{
		int temp2=0;
		for(int j=i;j<l2;j++)
		{
			if(b[j]==47)
				temp2++;
		}
		return temp2+1;

	}
}

int main()
{

	ifstream fin("google.in");
	ofstream fout("google.out");
	int t;
	fin>>t;
	for(int i=0;i<t;i++)
	{	
		fin>>o>>n;
		for(int j=0;j<n+o;j++)
		{
			fin>>da[j];
		}
		int hou=0;
		for(int j=o;j<n+o;j++)
		{
			int temp=0;
			int le=strlen(da[j]);
			for(int z=0;z<le;z++)
				if(da[j][z]==47)
					temp++;

			for(int w=0;w<j;w++)
			{
				temp=temp>re(da[w],da[j])? re(da[w],da[j]):temp;
			}
			hou+=temp;
		}
		fout<<"Case #"<<i+1<<": "<<hou<<endl;
	}
	return 1;
}
