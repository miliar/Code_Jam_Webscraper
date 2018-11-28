//CODEJAM - A

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

int main()
{
	//vars
	ifstream f ("A-large.in");
	ofstream g ("A.out");
	int t,tt,n,a;
	long double tot;
	long double x[805],y[805];
	cout << fixed << setprecision(0);
	g << fixed << setprecision(0);
	//testcase loop
	f >> tt;
		for (t=1; t<=tt; t++)
		{
			//input
			f >> n;
				for (a=0; a<n; a++)
					f >> x[a];
				for (a=0; a<n; a++)
					f >> y[a];
			//sort
			sort(x,x+n);
			sort(y,y+n);
			//add
			tot=0;
				for (a=0; a<n; a++)
					tot+=x[a]*y[n-a-1];
			//output
			cout << "Case #" << t << ": " << tot << endl;
			g << "Case #" << t << ": " << tot << endl;
		}
	return(0);
}