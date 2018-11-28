#include <iostream>
#include <string>
#include <fstream>
using namespace std;

bool test(int a,int b)
{
	int i,j,k,z,l;
	int x[7];
	int y[7];
	for(i=0;a>0;i++)
	{
		x[i]=a%10;
		a/=10;
	}
	for(i=0;b>0;i++)
	{
		y[i]=b%10;
		b/=10;
	}
	i--;
	for(j=0;j<i;j++)
	{
		for(k=0,z=0;k<=i;k++)
		{
			l=i-j+k;
			if(i-j+k>i)
			{
				l=l-i-1;
			}
			if(x[k]==y[l])z++;
			else break;
		}
		if(z==i+1)return true;
	}
	return false;

}
main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	int total;
	fin>>total;
	int i,j,k,result;
	int x,y;
	for(i=1;i<=total;i++)
	{
		result=0;
		fin>>x>>y;
		for(j=x;j<=y;j++)
		{
			for(k=x;k<=y;k++)
			{
				if(k>=j)break;
				if(test(j,k))
				{
					result++;				
				}
			}
		}
		fout<<"Case #"<<i<<": "<<result<<endl;
	}
	return 0;
}