#include<cstdlib>
#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

int main()
{
	ifstream ifile;
	ofstream ofile;

	char cc[1000],m[51][51];
	int tc,flag=0;
	char *x;
	int i,j,k,r,c;

	ifile.open("in");
	ofile.open("out",ios::out);
	
	ifile.getline(cc,1000,'\n');			

	tc=atoi(cc);
	for(k=0;k<tc;k++)
	{flag=0;
		cout<<"\n************case"<<k+1<<"*****************\n\n";
		ifile.getline(cc,1000,'\n');
		x = strtok(cc," ");
		r=atoi(x);
		x = strtok(NULL," ");
		c=atoi(x);
		
		for(i=0;i<r;i++)
		{
			ifile.getline(cc,1000,'\n');
			for(j=0;j<c;j++)
			{
				if(cc[j]=='#')m[i][j]='#';
				else if(cc[j]=='.')m[i][j]='.';
			}
		}
		for(i=0;i<r;i++)
		{cout<<"\n";
			for(j=0;j<c;j++)
				cout<<m[i][j]<<" ";
		}

		for(i=0;i<r-1;i++)
		{
			for(j=0;j<c-1;j++)
			{
				if(m[i][j]=='#' && m[i+1][j]=='#' && m[i][j+1]=='#' && m[i+1][j+1]=='#')
				{
					m[i][j]='/';
					m[i+1][j]='\\';
					m[i][j+1]='\\';
					m[i+1][j+1]='/';
				}
			}
		}
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
				if(m[i][j]=='#')
					{flag=1;break;}
		}
		if(flag==1)
			ofile<<"Case #"<<k+1<<": \nImpossible\n";
		else
		{ofile<<"Case #"<<k+1<<": \n";
			for(i=0;i<r;i++)
			{
				for(j=0;j<c;j++)
					ofile<<m[i][j];
				ofile<<"\n";
			}
		}
	}
	
	
	ofile.close();
	ifile.close();

	return 0;
}
