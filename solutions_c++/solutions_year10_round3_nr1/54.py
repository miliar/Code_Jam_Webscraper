#include<fstream>
#include<iostream>
#include<cmath>
#include<limits>
#include<vector>
#include<algorithm>
#include<deque>
#include<list>
using namespace std;

ifstream lettura ("input.txt");
ofstream scrittura ("output.txt");

int t, n;
vector< pair<int,int> > wires;

void leggi ()
{
	wires.clear();
	lettura >> n;
	wires.reserve (n);
	
	int a, b;
	for (int i = 0; i < n; i++)
	{
		lettura >> a >> b;
		wires.push_back (make_pair (a, b));
	}
}

int elabora ()
{
	sort (wires.begin(), wires.end());
	int result = 0;
	for (int i = 1; i < n; i++)
	{
		for (int j = 0; j < i; j++)
		{
			if (wires[j].second > wires[i].second)
				result ++;
		}
	}
	return result;
}

int main ()
{
	lettura >> t;
	for (int i = 0; i < t; i++)
	{
		leggi ();
		scrittura << "Case #" << (i+1) << ": " << elabora () << endl;
	}
}
