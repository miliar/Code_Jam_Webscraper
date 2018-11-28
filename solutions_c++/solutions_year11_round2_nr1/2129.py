#include<cstdlib>
#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

int main()
{
	ifstream ifile;
	ofstream ofile;

	char c[1000];
	int mat[101][101];
	int tc;
	char *x;
	int i,j,k,m,n,w,t;
	int ti,wi,ci;
	
	long double wp[101],owp[101],oowp[101],owpi,oowpi;

	ifile.open("in");
	ofile.open("out",ios::out);
	
	ifile.getline(c,1000,'\n');			

	tc=atoi(c);
	for(k=0;k<tc;k++)
	{
		cout<<"\n************case"<<k+1<<"*****************\n\n";
		ifile.getline(c,1000,'\n');
		n=atoi(c);
		for(j=0;j<n;j++)
		{
			ifile.getline(c,1000,'\n');
			for(i=0;i<n;i++)
			{
				if(c[i]=='.')mat[j][i]=-1;
				else if(c[i]=='1')mat[j][i]=1;
				else if(c[i]=='0')mat[j][i]=0;
			}
		}
		/*for(j=0;j<n;j++)
		{cout<<"\n";
			for(i=0;i<n;i++)
				cout<<mat[i][j];
		}*/
		for(j=0;j<n;j++)
		{
			w=0;t=0; ci=0;owpi=0;
			for(i=0;i<n;i++)
			{
				if(mat[j][i]==1 || mat[j][i]==0)
				{
					t++;
					if(mat[j][i]==1)
						w++;
					ci++;
					ti=0;wi=0;
					for(m=0;m<n;m++)
					{
						if(m!=j)
						{
							if(mat[i][m]==1 || mat[i][m]==0)
							{
								ti++;
								if(mat[i][m]==1)
									wi++;
							}
						}
					}
					owpi=owpi+wi/(ti*1.0);
				}
			}
			owp[j]=owpi/ci;
			wp[j]=w/(t*1.0);								
		}
		/*cout<<"\nwp->\n";
		for(j=0;j<n;j++)
			cout<<wp[j]<<" ";
		cout<<"\nowp->";
		for(j=0;j<n;j++)
			cout<<owp[j]<<" ";
		cout<<"\n";*/
		for(j=0;j<n;j++)
		{
			oowpi=0;ci=0;
			for(i=0;i<n;i++)
			{
				if(mat[j][i]==1 || mat[j][i]==0)
				{ci++;
					oowpi+=owp[i];
				}
			}
			oowp[j]=oowpi/ci;
		}
		/*cout<<"\noowp->";
		for(j=0;j<n;j++)
			cout<<oowp[j]<<" ";
		cout<<"\n";*/
		
		ofile<<"Case #"<<k+1<<": \n";
		for(j=0;j<n;j++)
		{
			ofile<<0.25*wp[j]+0.50*owp[j]+0.25*oowp[j]<<"\n";
		}

		
			
	}
	
	ofile.close();
	ifile.close();

	return 0;
}
