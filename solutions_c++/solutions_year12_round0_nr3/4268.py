#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <map>
#include <utility>
using namespace std;

ifstream in("input.in");
ofstream out("output.txt");

int powN(int n , int a)
{
	if (a == 0)
		return 1;
	else if (a%2 == 0)
		return powN(n,a/2)*powN(n,a/2);
	else
		return n*powN(n,a/2)*powN(n,a/2);
}

int numDigitos(int n)
{
	return floor(log10(static_cast<float>(n)))+1;
}

int rotar(int n,int d)
{
	int r = n%10;
	n /= 10;
	n+=r*powN(10,d-1);
	return n;
}

int main ()
{
	int T,A,B;
	map<pair<int,int>,bool> m;
	/*
	while (true)
	{
	cin >> A;
	cout << A << endl;
	A = rotar(A,numDigitos(A));
	cout << A << endl;
	A = rotar(A,numDigitos(A));
	cout << A << endl;
	A = rotar(A,numDigitos(A));
	cout << A << endl;
	A = rotar(A,numDigitos(A));
	cout << A << endl;
	A = rotar(A,numDigitos(A));
	cout << A << endl;
	}*/
	
	in >> T;
	
	for (int i = 1; i <=T ; ++i)
	{
		in >> A >> B;
		int res = 0;
		int digitos = max(numDigitos(A),numDigitos(B));
		m.clear();
		for (int j = A; j < B; ++j)
		{
			for (int k = 0,curr = j; k < digitos-1; ++k)
			{
				curr = rotar(curr,digitos);
				if (curr > j && curr <=B)
				{
					if (m[make_pair(j,curr)] || m[make_pair(j,curr)])
					{
						//out << "\\\\o" << j << " " << curr << endl;
					}
					else
						res++;
					m[make_pair(j,curr)] = 1;
					
				}
			}
		}
		out << "Case #" << i << ": " << res << '\n';
	}

	return 0;
}