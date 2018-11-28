#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	int t,j,k,row,col;
	bool** given,imp;
	char** changed;
	char ch; 

    ifstream ifs ( "c" , ifstream::in );

    ofstream myfile;
	myfile.open ("example.txt");

  	ifs>>t;
    for(int i=0;i<t;i++)
    {
    	imp=false;
		ifs>>row;
		ifs>>col;
		given=new bool*[row];
	    for(k=0;k<row;k++)
			given[k]=new bool[col];
			
		changed=new char*[row];
	    for(j=0;j<row;j++)
	    {
			changed[j]=new char[col];
			for(k=0;k<col;k++)
				changed[j][k]='.';
		}
		
	    for(j=0;j<row;j++)
   		    for(k=0;k<col;k++)
   		    {
   		    	ifs>>ch;
   		    	if(ch=='#')
   		    		given[j][k]=true;
   		    	else
   		    		given[j][k]=false;
   		    }

   		for(j=0;j<row-1;j++)
   		    for(k=0;k<col-1;k++)
			{
				if(given[j][k]==true)
				{
					if(given[j+1][k]==true && given[j][k+1]==true && given[j+1][k+1]==true)
					{
						given[j+1][k]=false;
						given[j][k+1]=false;
						given[j+1][k+1]=false;
						changed[j][k]='/';
						changed[j][k+1]='\\';
						changed[j+1][k]='\\';
						changed[j+1][k+1]='/';
					}
					else
					{
						imp=true;
						break;
					}
				}
			}
		if(!imp)
		{
			for(j=0;j<row;j++)
				if(given[j][col-1]==true)
				{
					imp=true;
					break;
				}				
	
			if(!imp)
				for(j=0;j<col;j++)
					if(given[row-1][j]==true)
					{
						imp=true;
						break;
					}										
		}
			
		myfile<<"Case #"<<i+1<<":\n";
		if(imp)
			myfile<<"Impossible\n";
		else
			for(j=0;j<row;j++)
			{
	   		    for(k=0;k<col;k++)
	   		    	myfile<<changed[j][k];
	   		    myfile<<'\n';
	   		}

	   	for(k=0;k<row;k++)
			delete given[k];
		delete given;	   		
	   	for(k=0;k<row;k++)
			delete changed[k];
		delete changed;
    }
    
    return 0;
}
