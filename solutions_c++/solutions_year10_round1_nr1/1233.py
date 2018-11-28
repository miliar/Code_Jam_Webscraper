#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;


int main()
{
	ifstream fi("credit.in");
	ofstream fo("credit.out");

	int t,k,n;

	fi>>t;
	char mat[50][50];
	int count[50];

	int vert[50][50];
	int posdiag[50][50];
	int negdiag[50][50];

	for(int c=1; c<=t; c++)
	{
		fo<<"Case #"<<c<<": ";

		for(int i=0; i<50; i++)
			for(int j=0; j<50; j++)
			{
				mat[i][j]=' ';
				vert[i][j]=posdiag[i][j]=negdiag[i][j]=0;
			}

		fi>>n>>k;
		for(int i=0; i<n; i++)
		{
			count[i]=0;
			for(int j=0; j<n; j++)
			{
				fi>>mat[i][j];
				if(mat[i][j]!='.')
					count[i]++;
			}
		}

		for(int i=0; i<n; i++)
		{
			int pos=n-1;
			for(int j=n-1; j>=0; j--)
			{
				if(mat[i][j]!='.')
				{
					if(j!=pos)
					{
						mat[i][pos]=mat[i][j];
						mat[i][j]='.';
					}
					pos--;
					if(pos==n-count[i]-1)
						break;
				}
			}
		}

		/*for(int i=0; i<n ;i++)
		{
			for(int j=0; j<n; j++)
				fo<<mat[i][j];
			fo<<endl;
		}*/
		bool red,blue;
		red=blue=false;
		for(int j=n-1; j>=n-count[n-1]; j--)
		{
			mat[n-1][j]=='R'?vert[n-1][j]=posdiag[n-1][j]=negdiag[n-1][j]=1:vert[n-1][j]=posdiag[n-1][j]=negdiag[n-1][j]=-1;
		}

		for(int i=n-1; i>=0; i--)
		{
			int left=n-count[i]-1;
			int horizon=0;
			
			for(int j=n-1; j>left; j--)
			{
				char tmp=mat[i][j];
				if(tmp=='R')
				{
					horizon>0?horizon++:horizon=1;
					if(i+1<n)
					{
						vert[i+1][j]>0?vert[i][j]=vert[i+1][j]+1:vert[i][j]=1;		//vertical

						if(j+1<n)			//positive diagnol
						{
							posdiag[i+1][j+1]>0?posdiag[i][j]=posdiag[i+1][j+1]+1:posdiag[i][j]=1;
						}
						else posdiag[i][j]=1;

						if(j-1>-1)		//negative 
						{
							negdiag[i+1][j-1]>0?negdiag[i][j]=negdiag[i+1][j-1]+1:negdiag[i][j]=1;
						}
						else negdiag[i][j]=1;
					}
					if(horizon==k||posdiag[i][j]==k||negdiag[i][j]==k||vert[i][j]==k)
						red=true;
				}
				else if(tmp=='B')
				{
					horizon<0?horizon--:horizon=-1;
					if(i+1<n)
					{
						vert[i+1][j]<0?vert[i][j]=vert[i+1][j]-1:vert[i][j]=-1;		//vertical

						if(j+1<n)			//positive diagnol
						{
							posdiag[i+1][j+1]<0?posdiag[i][j]=posdiag[i+1][j+1]-1:posdiag[i][j]=-1;
						}
						else negdiag[i][j]=-1;

						if(j-1>-1)		//negative 
						{
							negdiag[i+1][j-1]<0?negdiag[i][j]=negdiag[i+1][j-1]-1:negdiag[i][j]=-1;
						}
						else negdiag[i][j]=-1;
					}
					if(horizon==-k||posdiag[i][j]==-k||negdiag[i][j]==-k||vert[i][j]==-k)
						blue=true;
				}
			}
		}

		if(blue&&red)
			fo<<"Both"<<endl;
		else if(blue&&!red)
			fo<<"Blue"<<endl;
		else if(!blue&&red)
			fo<<"Red"<<endl;
		else fo<<"Neither"<<endl;


	}
}


