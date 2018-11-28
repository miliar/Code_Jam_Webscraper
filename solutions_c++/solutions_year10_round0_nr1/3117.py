#include<iostream>
#include<algorithm>
#include<list>
#include<fstream>
#include<vector>
#include<cstdlib>
#include<cmath>

using namespace std;

int main()
{
    	    unsigned long int no_cases,devi,snap;

	    unsigned long int r_snap,test,x;
	    
	    ifstream fin;
	    fin.open("A-large.in",ios::in);
	    
	    ofstream fout;
	    fout.open("A-large.out",ios::out);

	    fin>>no_cases;



	    for( int i = 0; i < no_cases; i++)
	    {
	     	   fin>>devi;
		   fin>>snap;

		   r_snap = 1;

		   for( int j = 0; j < devi; j++)
		   	  r_snap *= 2;

		    

		   x = (snap + 1)/r_snap - 1;

		   test = r_snap*(x+1) - 1;

		   if(test == snap)
		   {
		    	     fout<<"Case #"<<i+1<<": "<<"ON"<<"\n";
		   }
		   else
		   {
		    	     fout<<"Case #"<<i+1<<": "<<"OFF"<<"\n";
		   }



		   
	    }

}
