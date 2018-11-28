#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

typedef unsigned long long ull;

const int SIZE = 2000;
const int MAX = 10000;

ull rank[SIZE], p[SIZE];

void makeset(ull i) {
	p[i] = i;
	rank[i] = 0;
}

void link(ull i, ull j) {
	if(rank[i] > rank[j])
	    p[j] = i;
	else    {
		p[i] = j;
		if(rank[i] == rank[j])
		    rank[j]++;
	}
}

ull findset(ull i)  {
	if(i != p[i])
	    p[i] = findset(p[i]);
	return p[i];
}

void UNION(ull i, ull j)    {
	link(findset(i), findset(j));
}

ull gcd(ull a, ull b)   {
	while(b != 0)   {
		ull c = a%b;
		a = b;
		b = c;
	}
	return a;
}

ull max_prime(ull d)    {
	ull m = floor(sqrt(d));
	for(ull i = 2; i <= m; i++) {
		while(d%i == 0) d /= i;
		m = floor(sqrt(d));
		if(m == 1)  return i;
	}
	return d;
}

int main()
{
	ofstream out("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\a.out");
	ull C, otest;
	ull A, B, P, S;
	ull i, j, k, d;
    cin >> C;
    for(otest = 0; otest < C;)  {
		S = 0;
		cin >> A >> B >> P;
		for(i = A; i <= B; i++)
			makeset(i-A);
		for(i = A; i <= B; i++)  {
			for(j = i+1; j <= B; j++)   {
				d = max_prime(gcd(i, j));
				if(d >= P) UNION(i-A, j-A);
			}
		}
		for(i = A; i <= B; i++)
		    if(p[i-A] == i-A) S++;
        out << "Case #" << ++otest << ": " << S << endl;

	}
	return 0;
}

