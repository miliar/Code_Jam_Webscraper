/*the problem is that one person is getting on the ride 10 times at one
 time so i need to check if the number of groups already went*/

#include <iostream>
#include <list>
#include <fstream>
using namespace std;

int main (int argc, char * const argv[]) {
	ifstream infile;
	ofstream outputFile;
	outputFile.open("smallOutput.txt");
	infile.open("/Users/Ish/Downloads/C-small-attempt2.in");		//should include your location of the file
	
	int group[10];
	list<int> next;
	int t,k,r,n,loop1,seatRemaining,nextPerson;
	int money=0;
	int counter = 0;
	int case_Num=1;
	
	if (!infile) {
		cerr << "Unable to open file A-small.in";
		exit(1);   // call system to stop
	}
	
	infile >> t;
	for(int i=1;i<=t;i++)
	{
		infile >> r;
		infile >> k;
		infile >> n;
		for(loop1 = 0; loop1<n;loop1++)
		{
			infile >> group[loop1];
			next.push_back(group[loop1]);
		}
		
		while(r!=0)
		{
			do
			{
				if(counter == n)
					break;
				nextPerson = next.front();
				if(nextPerson > (k-seatRemaining))
				{
					break;
				}
				next.pop_front();
				seatRemaining += nextPerson;
				next.push_back(nextPerson);
				money += nextPerson;
				counter++;
				
			}while(seatRemaining<k);
			counter = 0;
			r--;
			seatRemaining = 0;
		}
		outputFile << "Case #" << case_Num << ": " << money << endl;		
		money=0;
		for(loop1 = 0; loop1<n;loop1++)
		{
			group[loop1]=0;
			next.pop_front();
		}
		case_Num++;
	}
		outputFile.close();
		
		return 0;
	
}
