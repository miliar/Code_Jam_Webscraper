#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include   <iomanip>
#include <algorithm>
#include <map>
using namespace std;
char table[100][100];
void mcopy(double *src,double *dst)
{
	for(int i=0;i<3;i++)
		dst[i]=src[i];
}
int main() {
	ofstream fout ("test.out");
	ifstream fin ("test.in");
	int t;
	fin>>t;
	for(int z=0;z<t;z++)
	{
		int m,n;
		int all=0;
		fin>>m>>n;
		bool right=true;
		fout<<"Case #"<<z+1<<":"<<endl;
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
			{
				fin>>table[i][j];
				if(table[i][j]=='#')
					all++;
			}
			if(all%4!=0)
			{
				fout<<"Impossible"<<endl;
				continue;
			}
			for(int i=0;i<m-1;i++)
			{
				for(int j=0;j<n-1;j++)
				{
					if(table[i][j]=='#')
					{
						table[i][j]='/';
						if(table[i+1][j]=='#')
						{
							table[i+1][j]='\\';
						}
						else
						{
							right=false;
							break;
						}
						if(table[i][j+1]=='#')
						{
							table[i][j+1]='\\';
						}
						else
						{
							right=false;
							break;
						}
						if(table[i+1][j+1]=='#')
						{
							table[i+1][j+1]='/';
						}
						else
						{
							right=false;
							break;
						}

					}
				}
				if(right==false)
					break;
			}
			if(right==0)
			{
				fout<<"Impossible"<<endl;
				continue;
			}
			else
			{
				for(int i=0;i<m;i++)
				{
					for(int j=0;j<n;j++)
					{
						fout<<table[i][j];
					}
					fout<<endl;
				}
			}
	}


	return 0;
}