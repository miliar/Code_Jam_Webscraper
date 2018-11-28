
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <math.h>
#include <vector>
#include <stdlib.h>
using namespace std;
/*
 * 
 */


long int gcd(long int m,long int n)
{
       long int p,q,r,gcd;
       p=m,q=n;
       while(n!=0)
       {
               r=m%n;
               m=n;
               n=r;
       }

       return m;
}

int main(int argc, char** argv) {

    ifstream in;
    in.open(argv[1]);
    if(!in) {
        cout <<"Error opening file!";
        exit(1);
    }

    int ntestcases;

    in >> ntestcases;
    for(int i=0; i<ntestcases; i++) {
      int N;
	long int first,T=0,y;
	in >> N;
	in >> first;
	for(int j = 0; j < N-1; j++)
	{
	 long int temp;
	 in >> temp;
	 temp = abs(first-temp);
	 T=gcd(T,temp);
	}
	if(first%T==0) y = 0;
	else y = T-(first%T);
	cout << "Case #"<<i+1<<": "<<y<<endl;
     }

	
    return (EXIT_SUCCESS);
}

