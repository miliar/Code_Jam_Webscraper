#include <fstream>
#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

int minim(int n)
{
	if(n==1) return 1;
	else return 2*minim(n-1)+1;
}
int main(){
	ifstream llegeix("A-large.in");
	ofstream escriu("sortidallarg.dat");
	int k,n,t;
	llegeix >> t;
	for(int i=0;i<t;i++)
		{	
			llegeix >> n;
			llegeix >> k;
			if(k%(minim(n)+1)==minim(n)) escriu << "Case #" << (i+1) << ": ON" << endl;
			else escriu << "Case #" << (i+1) << ": OFF" << endl;
			
		}
	escriu.close();
	llegeix.close();
		
}
		

	
	
