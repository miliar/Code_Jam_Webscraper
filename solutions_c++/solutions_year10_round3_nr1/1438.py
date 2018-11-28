
#include "stdafx.h"

#include <fstream>
#include <string>
#include <iostream>
using namespace std;


int main(int argc, char* argv[])
{
int count=0;
	int k=0,jj=0;
	int left[1001];
	int right[1001];
	int t=0;
	int n=0;
	ifstream freadfile("A-large.in",ios::in);
	ofstream fwritetofile("output.txt",ios::out);
	
	freadfile>>t;
	for(int tt=0;tt<t;tt++)
	{
		count=0;
		freadfile>>n;
		for(jj=0;jj<n;jj++)
		{
			freadfile>>left[jj];
		     freadfile>>right[jj];
		}
		for(k=0;k<n;k++)
		    for(jj=k+1;jj<n;jj++)
			{
				if((left[k]>left[jj] && right[k]<right[jj])||
					(left[k]<left[jj] && right[k]>right[jj])) count++;

			}
		fwritetofile<<"Case #"<<tt+1<<": "<<count<<endl;

		
	}

	 freadfile.close();
    fwritetofile.close();
	return 0;
}
