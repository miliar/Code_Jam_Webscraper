#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>


using namespace std;

ifstream in("small.in");
ofstream out("small.out");

const int MAXH = 1000010;
const int MAXK = 1100000;

bool primes[MAXK];

int gcd(int a,int b)
{	
	if (a==0)
		return b;
	return gcd(b%a,a);
}

void siev()
{
	int i,k,max=MAXH;
	primes[1]=false;
	primes[2]=true;	
	for (i=3;i<max;i++)
		primes[i]=true;	
	for (i=2;i<max;i++)	
		if (primes[i])
			for (k=2*i;k<max;k+=i)		
				primes[k]=false;			
}
/*
long long minN(long long n)
{
	int i,ans = 0;
	for (i = 2; i <= n; ++i)
		if (primes[i])
			ans++;
	return ans;
}

long long maxN(long long n)
{	
	vector <int> v;
	int i,j,u,k,g;
	for (i = 2; i <= n; ++i)
		if (primes[i])
			v.push_back(i);
	int ans = 0;

	for (int u = 1; u <= n; ++u)
	{
		bool f = true;
		for (i = 2; i < u && f; ++i)
			for (j = i + 1; j < u && f; ++j)
				if (gcd(i,j) == 1 && i*j == u)
					f = false;

		for (i = 2; i < u && f; ++i)
			for (j = i + 1; j < u && f; ++j)
				for (k = j + 1; k < u && f; ++k)
					if (gcd(gcd(i,j),k) == 1 && i*j*k == u)
						f = false;

		for (i = 2; i < u && f; ++i)
			for (j = i + 1; j < u && f; ++j)
				for (k = j + 1; k < u && f; ++k)
					for (g = k + 1; g < u && f; ++g)
						if (gcd(gcd(gcd(i,j),k),g) == 1 && i*j*k*g == u)
							f = false;

		if (f)
			ans++;
	}
	
	return ans;
}*/

vector <long long> v;

int solve(long long n)
{
	if (n == 1)
		return 0;
	long long i;
	v.clear();
	for (i = 2; i < MAXH; ++i)
		if (primes[i])
			v.push_back(i);

	int answer = 1;

	for (i = 0; i < v.size(); ++i)
	{
		//cout << v[i] << endl;
		//if (v[i] > n)
		//	break;
		long long tiv = (long long)v[i];
		long long t = (long long)v[i];
		tiv = tiv *t;
		while (tiv <= n)
		{
			//out << tiv << endl;
			answer++;
			tiv *= t;
			if (tiv < 0)
				break;
		}
	}
	return answer;
}

int main()
{
	int test,t,i,j;

	siev();

	//long long n;

	//for (n = 1; n <= 100; ++n)
	//	cout << n << ": " << minN(n)  << " " << maxN(n) << " " << maxN(n) - minN(n) << " " << solve(n) << endl;

	long long n;

	in >> test;

	for (t = 1; t <= test; ++t)
	{
		in >> n;
		long long answer = 0;

		out << "Case #" << t << ": " << solve(n) << endl;
	}

	return 0;
}