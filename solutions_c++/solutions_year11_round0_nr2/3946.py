#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;
char change[36][4];
char destroy[28][3];
char in[100];
char temp[105];
main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int i,j,k,l,m,n,o,p,changeno,destroyno,wordsno,cases,x,y;
	fin>>n;
	for(cases=0;n>0;n--)
	{
		fin>>changeno;
		for(i=0;i<changeno;i++)
		{
			fin>>change[i];
		}
		fin>>destroyno;
		for(i=0;i<destroyno;i++)
		{
			fin>>destroy[i];
		}
		fin>>wordsno;
		fin.getline(temp,105);
		for(i=0,o=1;o<=wordsno;i++,o++)
		{
			in[i]=temp[o];
			if(changeno!=0)
			{
				for(y=0;y<changeno;y++)
				{
				for(x=0;x<changeno;x++)
				{
					for(j=0;j<i;j++)
					{
						if(in[j]==change[x][0]&&in[j+1]==change[x][1]||in[j]==change[x][1]&&in[j+1]==change[x][0])
						{
							in[j+1]='\0';
							i=j;
							in[j]=change[x][2];
						}
					}
				}
				}
			}
			if(destroyno!=0)
			{
				for(y=0;y<destroyno;y++)
				{
					for(j=0,k=-1;j<=i;j++)
					{
						if(in[j]==destroy[y][0])
						{
							k=j;break;
						}
					}
					if(k!=-1)
					{
						for(j=0;j<=i;j++)
						{
							if(in[j]==destroy[y][1]&&j!=k)
							{
								i=-1;
								in[i+1]='\0';
								break;
							}
						}
					}
				}
			}
		}
		cases++;
		fout<<"Case #"<<cases<<": [";
		for(j=0;j<i;j++)
		{
			if(j!=i-1)
			fout<<in[j]<<", ";
			else fout<<in[j];
		}
		fout<<"]"<<endl;
		
	}
}