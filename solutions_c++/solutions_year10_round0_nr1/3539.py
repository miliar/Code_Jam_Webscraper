#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
	ifstream in("A-small.in");
	ofstream out("A-small.out");
	int T, n, k;
	bool bulbon = false;
	in >> T;
	for(int t = 0; t < T; t++)
	{
		in >> n >> k;
		if(k == 0) bulbon = false;
		else if(k == (pow(2, n)-1)) bulbon = true;
		else if(((k-((int)pow(2,n)-1)) % (int)pow(2,n)) == 0) bulbon = true;
		
		if(bulbon)
			out << "Case #" << t+1 << ": ON" << endl;
		else 
			out <<  "Case #" << t+1 << ": OFF" << endl;
		bulbon = false;
	}

	in.close();
	out.close();

	return 0;
}