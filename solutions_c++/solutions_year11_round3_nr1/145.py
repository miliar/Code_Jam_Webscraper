#include <iostream>
#include <fstream>

using namespace std;
int r, c;
string a[100];


int main ()
{
	ifstream fin("A-large.in");
	ofstream fout("a.txt");
	int T;
	bool f;
	fin>>T; 
	for(int t=1; t<=T; ++t)
	{
		fin>>r>>c;
		for(int i=0; i<r; ++i)
			fin>>a[i];
		f=true;
		for(int i=0; i<r; ++i)
		{
			for(int j=0; j<c; ++j)
			{
				if (a[i][j]=='#')
				{
					if (i==r-1 || j==c-1)
					{
						f=false;
						break;	
					}
					if (a[i+1][j]=='.' || a[i][j+1]=='.' || a[i+1][j+1]=='.')
					{
						f=false;
						break;	
					}
					a[i][j]= a[i+1][j+1]='/';
					a[i+1][j]=a[i][j+1]='\\';
					
				}
			}	
			if (!f) break;
		}
		
		
		fout<<"Case #"<<t<<": "<<endl;
		if (f)
		{
			for(int i=0; i<r; ++i)
			{
				for(int j=0; j<c; ++j)
					fout<<a[i][j];	
				fout<<endl;
			}
		}
		else 
			fout<<"Impossible"<<endl;
	}
}	
