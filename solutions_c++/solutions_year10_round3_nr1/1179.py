#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

#define metafor(it, v) for ( it = v.begin(); it != v.end(); it++ )

#define X0 1
#define X1 10
#define EPSILON 0.0001

vector<pair<double, double> > toWiresMB(vector<pair<int, int> > wiresAB)
{
	vector<pair<double, double> > wiresMB;
	vector<pair<int, int> >::iterator it;
	metafor(it, wiresAB)
	{
		double m = (double)(it->first - it->second) / (double)(X0 - X1);
		double b = it->first - m * X0;
		wiresMB.push_back(make_pair(m,b));
	}
	return wiresMB;
}

int intersections(const vector<pair<double, double> > &wiresMB)
{
	int count = 0;
	vector<pair<double, double> >::const_iterator itI;
	metafor(itI, wiresMB)
	{
		double mi = itI->first, bi = itI->second;
		vector<pair<double, double> >::const_iterator itJ;
		for(itJ=itI+1; itJ != wiresMB.end(); ++itJ)
		{
			double mj = itJ->first, bj = itJ->second;
			if ( abs(mj - mi)  > EPSILON )
			{
				double xint = (bj-bi)/(mi-mj);
				if ( X0< xint && xint < X1 )
				{
					count++;
				}
			}

		}
	}
	return count;
}

int main()
{
	ifstream in("C:\\Users\\German\\Documents\\Visual Studio 2005\\Projects\\Problemas\\A-large.in");
	//ifstream in("sample.in");
	ofstream out("C:\\Users\\German\\Documents\\Visual Studio 2005\\Projects\\Problemas\\sol.out");

	int T;
	in >> T;
	for(int t=1; t<=T; t++)
	{
		int N;
		in >> N;
		vector<pair<int, int> > wiresAB(N);
		for(int i=0; i<N; i++)
		{
			int A,B;
			in>>A>>B;
			wiresAB[i] = make_pair(A,B);
		}
		vector<pair<double, double> > wiresMB = toWiresMB(wiresAB);
		int cant = intersections(wiresMB);

		out << "Case #" << t << ": " << cant<< endl;
		cout << "Case #" << t << ": " << cant << endl;
	}

	system("pause");
	return 0;
}
