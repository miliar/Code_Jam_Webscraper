#include <iostream>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath> 

#define fill_(x,v) memset(x,v,sizeof(x))
#define for_(i,a,b) for (__typeof(b) i=(a); i<(b); i++)
#define min(x,y) (((x)>(y)) ? (y) :(x))
#define max(x,y) (((y)>(x)) ? (y) :(x)) 
using namespace std;

map<long, int> is_happy[11];
vector<int> bases;

long cal(long input, int base)
{
	long m = input;
	long res;
	long total = 0;
	while ( m )
	{
		long res = m % base;
		total += res * res;
		m /= base;
	}
//	cout<<input<<" "<<base<<" "<<total<<endl;
	return total;
}

int getH( long input, int base)
{
//	cout<<1<<" "<<input<<" "<<base<<" "<< is_happy[base][input]<<endl;
	if (input == 1 )
		return 1;
	if ( is_happy[base][input] != 0 ) return is_happy[base][input];

	
    is_happy[base][input] = -1;
    is_happy[base][input] = getH (cal(input, base), base);
//	cout<<  is_happy[base][input] <<endl;

	return is_happy[base][input];
}

int main()
{
	int N;
    string inpstring;
	ifstream inp("e:\\A-small-attempt0.in");
	ofstream out("e:\\output.txt");
	inp>> N;
	getline(inp, inpstring);
	int i,j;
	for (int nn = 1; nn <= N; nn++)
	{
		bases.clear();

		getline(inp, inpstring);
		istringstream baseinput(inpstring);
		while (!baseinput.eof())
		{ int mm; baseinput>>mm; bases.push_back(mm);
		}

		j = 2;
		while(1)
		{
			bool finish = true;
			for ( int ii = 0; ii < bases.size(); ii ++ )
				if ( getH(j, bases[ii])!= 1 ) finish = false;
		    if (finish) break;
			j++;
		}


		out<<"Case #"<<nn<<": "<< j <<endl;
	}// end of nn

}