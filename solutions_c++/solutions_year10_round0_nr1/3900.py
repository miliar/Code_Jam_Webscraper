#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()	{
	ifstream fin ("inp");
	ofstream fout ("out.txt");
	int T , n , k , cas=1 , t;
	fin>>T;
	while ( T-- )	{
		fin>>n>>k;
		t = (int) floor( pow(2,n)+0.2) ;
		fout<<"Case #"<<cas++<<": ";
		if ( (k+1)%t == 0 ) fout<<"ON\n";
		else fout<<"OFF\n";
	}
	return 0;
}
