#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	int T,N;
	ifstream in("input.txt");
	ofstream out("output.txt");		
	out.precision(7);
	out.setf(ios::showpoint);
	in>>T;
	for(int k=0; k<T; k++)
	{
		in>>N;
		vector<int> c(N);
		for(int i=0; i<N; i++)
			in>>c[i];
		
		double m=0;
		for(int i=0; i<N; i++)
			if (c[i]!=i+1)
				m++;
		out<<"Case #"<<(k+1)<<": "<<m<<endl;
	}
	return 0;
}



