#include <fstream>
#include <cmath>
using namespace std;

int main()
{
ifstream fin;
ofstream fout; 
fin.open("A-large.in");
fout.open("test.out");

int tc_count;
int snapper; 
int toggle;
int n =0;
int x ; 
fin>>tc_count;
while(n < tc_count)
{
	fin>>snapper>>toggle;
	x = pow((double)2, snapper);

	if(toggle%x == x-1)
		fout<<"Case #"<<n+1<<": ON"<<endl;
	else
		fout<<"Case #"<<n+1<<": OFF"<<endl;
	
n++; 
}


return 0;
}