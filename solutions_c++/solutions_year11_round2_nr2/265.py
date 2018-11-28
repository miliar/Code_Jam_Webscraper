#include<iostream>
#include<stdio.h>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;

/*
 * This program reads from stdin and writes to stdout.
 * Run it with
 *     program < input.txt > output.txt
 */

int C , D;
long double P[400];
int V[400];

bool place(long double M)
{
	long double l = -1e14;
	for(int i = 0 ; i < C ; i++)
	{
		l = max(P[i] - M , l + D) + (V[i] - 1.0) * D;
		if(l - P[i] > M + 1e-7)
		{
			//cerr << "- " << M << "\n";
			return false;
		}
	}
	//cerr << "+ " << M << "\n";
	return true;
}

int main()
{
	int T;
	cin >> T;
	for(int t = 0 ; t < T ; t++)
	{
		cerr << "Test " << t << "\n";
		cin >> C >> D;
		for(int i = 0 ; i < C ; i++)
			cin >> P[i] >> V[i];
		long double l , r , m;
		l = 1e-7;
		r = l * 2;
		while(!place(r))
			r *= 2;
		while(r - l > 1e-7)
		{
			m = (l + r) / 2.0;
			if(place(m))
				r = m;
			else
				l = m;
		}
		printf("Case #%d: %.10lf\n" , t + 1 , (double)r);
	}
}









