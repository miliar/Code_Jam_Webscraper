#include <fstream>
#include <iostream>
using namespace std;

int main()
{

ifstream infile("A-large.in");
ofstream outfile("outlarge.txt");

bool status;
unsigned long int caseno,i=0,j;
unsigned long int snappers,snaps;
infile >> caseno;
while(i<caseno)
{
outfile << "Case #" << ++i << ": ";
infile >> snappers >> snaps;
//cout << snappers << " ";
//cout << snaps << endl;
status=false;
for(j=0;j<snappers;j++)
{
	if((snaps & 1<<j)) 
	status=true;
	
	else {
	status=false;
	break;
	}

}

//cout << (snappers & snaps) << " ";
if(status) outfile << "ON" << endl;
else outfile << "OFF" << endl;
}

outfile << endl;

return 0;

}
