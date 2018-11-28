#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include<ctype.h>
#include<math.h>
using namespace std;

ofstream fout ("smalla.out");
ifstream fin ("smalla.in");

int main()
{
	int T,i,j=0,m,flag;
	char lan[100];int a[200],b[150];
	fin>>T;
	
	for(m=0;m<T;m++)
	{
		fin>>lan;j=0,flag=1;
		for(i=0;i<200;i++)
			a[i]=-1;
		for(i=0;i<strlen(lan);i++)
		{
			if(a[int(lan[i])]==-1&&flag)
				{a[int(lan[i])]=1;flag=0;}
			if(a[int(lan[i])]==-1&&flag==0)
			{
				a[int(lan[i])]=j;
				if(j==0)j++;
				j++;
			}
		}
		for(i=0;i<strlen(lan);i++)
		{
			b[i]=a[int(lan[i])];
			cout<<b[i];
		}
		cout<<endl;
		long sum=0;int k=0;
		if(j==0)
			j=2;
		for(i=strlen(lan)-1;i>=0;i--)
		{
			
			sum+=b[i]*pow(j,k);
			k++;
		}
		fout<<"Case #"<<m+1<<": "<<sum<<endl;
	}
	return 0;
}
