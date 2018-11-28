#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

ifstream lettura ("one.in");
ofstream scrittura ("one.out");

int main ()
{
	int t;
	lettura >> t;
	for (int i = 1; i <= t; i++)
	{
		int n, k;
		lettura >> n >> k;
		scrittura << "Case #" << i << ": ";
		if (pow (2, n) - 1 <= k)
			scrittura << "ON";
		else
			scrittura << "OFF";
		scrittura << endl;
	}
}
