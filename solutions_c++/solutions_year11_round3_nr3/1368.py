#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	int t,j,k,n;
	long low,high,*given;

    ifstream ifs ( "d" , ifstream::in );

    ofstream myfile;
	myfile.open ("example.txt");

  	ifs>>t;
    for(int i=0;i<t;i++)
    {
		ifs>>n;
		given=new long[n];
		
		ifs>>low;
		ifs>>high;
	    for(j=0;j<n;j++)
	    	ifs>>given[j];

		myfile<<"Case #"<<i+1<<": ";
			    	
	    for(j=low;j<=high;j++)
	    {
		    for(k=0;k<n;k++)
		    {
		    	if(given[k]>j && given[k]%j!=0)	//this number j not possible
		    		break;
	    		if(given[k]<j && j%given[k]!=0)
	    			break;
		    }
		    if(k==n)
		    {
		    	myfile<<j<<'\n';
		    	break;
		    }
		}
		if(j==high+1)
			myfile<<"NO\n";

		delete given;
    }
    
    return 0;
}
