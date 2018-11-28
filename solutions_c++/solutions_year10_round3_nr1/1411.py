#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <list>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <fstream>
using namespace std;

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A.txt");
	int T, N;
	cin >> T;
	int A[1000],B[1000];
	int i,j,d;
	double k;
	
	for(int q = 1; q <= T; q++)
	{    
	    d = 0;
		cin >> N;
		//cout << "R=" << R << "k=" << k << "N=" << N << endl;
		for (i=0; i<N; i++)
		{
		    cin >> A[i];
		    cin >> B[i];
		    //cout << "g[" << i << "]=" <<g[i] << endl;
		}
		
		for (i=0; i<N-1;i++)
		{
		   for (j=i+1;j<N;j++)
		   {
		     k = (double)(B[j]-B[i])/(A[j]-A[i]);
		    // cout << "B(1)=" << B[j] << "B(0)=" << B[i] << endl;
		    // cout << "A(1)=" << A[j] << "A(0)=" << A[i] << endl;
		    // cout << "k=" << k << endl;
		     
		     if (k<0)
		        d ++;
		   }
		}
		cout << "Case #" << q << ": " << d << endl;  	
	}
	return 0;
}
