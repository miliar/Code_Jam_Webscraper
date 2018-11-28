#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string.h>
#include <math.h>
int m,n;
using namespace std;

int main()
{
	int t;
	ifstream fin("in");
	ofstream fout("out");
	fin>>t;

	for(int i=0;i<t;i++)
	{
		fin>>m>>n;
		int sum=0;
		char temp[100];
		for(int j=m;j<=n;j++)
		{
			sprintf(temp,"%d",j);
			int len=strlen(temp);
			for(int k=1;k<len;k++)
			{
				int re=j%((int)pow(10,k));
				re*=pow(10,len-k);
				re+=j/pow(10,k);
				if(re>=m&&re<=n&&re>j)
				{
					sum++;	
				}
			}
		}
		fout<<"Case #"<<i+1<<": "<<sum<<endl;
	}
	return 1;
}
