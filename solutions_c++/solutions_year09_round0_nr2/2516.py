#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	ifstream fin("B-large.in",ios::in);
	ofstream fout("output.txt",ios::out);
	int i,j,k;
	int t,h,w;
	bool changed;
	int alt[100][100];
	char rlt[100][100];
	int sinkdir;
	int maxdiv;
	int value;
	fin>>t;
	for(i=0;i<t;i++)
	{
		fout<<"Case #"<<i+1<<": "<<endl;
		//input
		fin>>h;
		fin>>w;
		for(j=0;j<h;j++)
		{
			for(k=0;k<w;k++)
			{
				fin>>alt[j][k];
				rlt[j][k]=0;
			}
		}
		//process
		rlt[0][0]=1;
		value=1;
		changed=true;
		while(changed)
		{
			changed=false;
			for(j=0;j<h;j++)
			{
				for(k=0;k<w;k++)
				{
					maxdiv=0;
					sinkdir=0;
					if(j>0)	//north
					{
						if((alt[j][k]-alt[j-1][k])>maxdiv)
						{
							maxdiv=alt[j][k]-alt[j-1][k];
							sinkdir=1;
						}
					}
					if(k>0)	//west
					{
						if((alt[j][k]-alt[j][k-1])>maxdiv)
						{
							maxdiv=alt[j][k]-alt[j][k-1];
							sinkdir=2;
						}
					}
					if(k<w-1)	//east
					{
						if((alt[j][k]-alt[j][k+1])>maxdiv)
						{
							maxdiv=alt[j][k]-alt[j][k+1];
							sinkdir=3;
						}
					}
					if(j<h-1)	//south
					{
						if((alt[j][k]-alt[j+1][k])>maxdiv)
						{
							maxdiv=alt[j][k]-alt[j+1][k];
							sinkdir=4;
						}
					}
					if(sinkdir!=0)
					{
						switch(sinkdir)
						{
						case 1:
							if(rlt[j][k]!=0&&rlt[j-1][k]==0)
							{
								rlt[j-1][k]=rlt[j][k];
								changed=true;
							}
							else if(rlt[j-1][k]!=0&&rlt[j][k]==0)
							{
								rlt[j][k]=rlt[j-1][k];
								changed=true;
							}
							break;
						case 2:
							if(rlt[j][k]!=0&&rlt[j][k-1]==0)
							{
								rlt[j][k-1]=rlt[j][k];
								changed=true;
							}
							else if(rlt[j][k-1]!=0&&rlt[j][k]==0)
							{
								rlt[j][k]=rlt[j][k-1];
								changed=true;
							}
							break;
						case 3:
							if(rlt[j][k]!=0&&rlt[j][k+1]==0)
							{
								rlt[j][k+1]=rlt[j][k];
								changed=true;
							}
							else if(rlt[j][k+1]!=0&&rlt[j][k]==0)
							{
								rlt[j][k]=rlt[j][k+1];
								changed=true;
							}
							break;
						case 4:
							if(rlt[j][k]!=0&&rlt[j+1][k]==0)
							{
								rlt[j+1][k]=rlt[j][k];
								changed=true;
							}
							else if(rlt[j+1][k]!=0&&rlt[j][k]==0)
							{
								rlt[j][k]=rlt[j+1][k];
								changed=true;
							}
							break;
						}
					}
				}
			}
			if(!changed)
			{
				for(j=0;j<h;j++)
				{
					for(k=0;k<w;k++)
					{
						if(rlt[j][k]==0)
						{
							rlt[j][k]=++value;
							changed=true;
							break;
						}
					}
					if(changed)
					{
						break;
					}
				}
			}
		}
		//out
		for(j=0;j<h;j++)
		{
			for(k=0;k<w;k++)
			{
				if(rlt[j][k]==0)
				{
					rlt[j][k]=++value;
				}
				if(k!=0)
				{
					fout<<' ';
				}
				fout<<(char)(rlt[j][k]-1+'a');
			}
			fout<<endl;
		}
	}
	fin.close();
	fout.close();
	system("pause");
	return 0;
}