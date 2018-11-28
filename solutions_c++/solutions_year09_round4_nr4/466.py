#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <stack>
#include <iomanip>
#include <queue>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <sstream>
#include <strstream>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

double x[5],y[5],r[5];

double hashiv(int i,int j,int p)
{
	double answer = (sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j])) + r[i] + r[j])/2.0;
	if (answer < r[p])
		return r[p];
	return answer;
}

int main()
{
	int test,t,i,j,n;
	in >> test;
	for (t=1;t<=test;t++)
	{
		double answer = 0.0;
		in >> n;
		if (n==1)
		{
			in >> x[0] >> y[0] >> r[0]; 
			answer = r[0];
		}
		if (n==2)
		{
			in >> x[0] >> y[0] >> r[0]; 
			in >> x[1] >> y[1] >> r[1];
			answer = r[0];
			if (r[1] > answer)
				answer = r[1];			
		}
		if (n==3)
		{
			in >> x[0] >> y[0] >> r[0]; 
			in >> x[1] >> y[1] >> r[1];
			in >> x[2] >> y[2] >> r[2];			

			answer = hashiv(0,1,2);
			if (answer > hashiv(0,2,1))
				answer = hashiv(0,2,1);
			if (answer > hashiv(1,2,0))
				answer = hashiv(1,2,0);
		}
		out << setiosflags(ios::fixed | ios::showpoint);
		out << "Case #" << t <<  ": " << setprecision(6) << answer << endl;
	}
	return 0;
}
