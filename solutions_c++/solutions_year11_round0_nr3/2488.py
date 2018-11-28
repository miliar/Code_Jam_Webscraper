#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>

#define	N	1000

using namespace std;

/*getline(cin,s);
istringstream ss(s);
ss >> nrtest;*/

int main(void)
{
	string s;

	int impossible,sum;
	int nrtest,nrcandy;
	int candies[N];
	int cdivide[20][N];
	int ndivide[20];
	
	getline(cin,s);
	istringstream ss(s);
	ss >> nrtest;
	
	for(int i=0;i<nrtest;i++)
	{
		getline(cin,s);
		istringstream sss(s);
		sss >> nrcandy;
		
		getline(cin,s);
		istringstream ss(s);
		
		impossible=0;
		sum=0;
		
		for(int j=0;j<nrcandy;j++)
		{
			ss >> candies[j];
			impossible^=candies[j];
			sum+=candies[j];
		}
				
		if(impossible)
		{
			cout << "Case #" << i+1 << ": NO" << endl;
		}
		else
		{
			sort(candies,candies+nrcandy);
			
			sum-=candies[0];
			
			cout << "Case #" << i+1 << ": " << sum << endl;
		}
	}
}
