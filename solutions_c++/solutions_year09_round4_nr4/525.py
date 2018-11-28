#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

double X[50];
double Y[50];
double C[50];

double dist(int i, int j)
{
	return sqrt(double (X[i]-X[j])*(X[i]-X[j]) + (Y[i]-Y[j])*(Y[i]-Y[j]));
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int N;
	cin >> N;
	for (int I=0; I<N; I++)
	{
		cout << "Case #" << I+1 <<": ";
		int n;
		cin >> n;
		for (int i=0; i<n; i++)
			cin >> X[i] >> Y[i] >> C[i];
		if (n == 1)
			cout << C[0] << endl;
		else if (n == 2)
			cout << max(C[0],C[1]) << endl;
		else
		{
			double rad = -1;
			for (int i=0; i<n; i++)
				for (int j=i+1; j<n; j++)
					if (rad == -1)
						rad = dist(i,j) + C[i] + C[j];
					else if (rad > dist(i,j) + C[i] + C[j])
						rad = dist(i,j) + C[i] + C[j];
			rad /=2;
			for (int i=0; i<3; i++)
				rad = max(rad, (double)C[i]);
			cout << rad << endl;
		}
	}
	return 0;
}