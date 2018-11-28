#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int main()
{

ifstream infile("C-small.in");
ofstream outfile("out.txt");

unsigned int caseno,casecnt=0,i;
unsigned long int dayruns,peoplerun,groups, moneymade,peoplein,groupsin;
infile >> caseno;
while(casecnt<caseno)
{
outfile << "Case #" << ++casecnt << ": ";
infile >> dayruns >> peoplerun >> groups;
vector<unsigned long int> groupsize(groups);
for(i=0;i<groups;i++)
{
	infile >> groupsize[i];
}
moneymade=0;

// Have all data needed, group vector in place.
// Iterate runs:
while(dayruns--)
{
	peoplein=0;
	groupsin=0;
	while( (peoplein+groupsize.front()) <= peoplerun && groupsin<groups)
	{
		peoplein+=groupsize.front();
		groupsize.push_back(groupsize.front());
		groupsize.erase(groupsize.begin());	
		groupsin++;		
	}
	moneymade+=peoplein;
}
outfile << moneymade << endl;

}


return 0;

}
