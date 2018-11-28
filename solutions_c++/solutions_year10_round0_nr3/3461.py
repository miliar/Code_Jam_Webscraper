#include <fstream>
#include <iostream>
#include <queue>

using namespace std;

#define mInt unsigned long int

mInt fillRollerCoaster(long long int k, queue<mInt> &q)
{
queue<mInt> auxq;
long long int oldk = k, euro = 0;

	while ((!q.empty()) && (k >= 0))
	{
		k -= q.front();
		
		if (k >= 0)
		{
			auxq.push(q.front());
			q.pop();
		}
	}
	
	while (!auxq.empty())
	{
		q.push(auxq.front());
		euro += auxq.front();
		auxq.pop();
	}
	
	return euro;
}

mInt calcEuro(mInt R, long long int k, queue<mInt> &q)
{
mInt i, euro = 0, j;
long long int aux;

	for (i=0; i<R; i++)
		euro += fillRollerCoaster(k, q);
	
	return euro;
}

int main()
{
ifstream in;
unsigned long int T, R, N, g;
unsigned long int i, j;
long long int k;

	in.open("C.in");
	if (!in.is_open())
	{
		std::cout << "error opening file\n" << std::endl;
		return 1;
	}

	in >> T;
	for (i=1; i<=T; i++)
	{
	queue<mInt> q;
	
		in >> R;
		in >> k;
		in >> N;
		for (j=0; j<N; j++)
		{
			in >> g;
			q.push(g);
		}
		
		std::cout << "Case #" << i << ": " << calcEuro(R, k, q) << std::endl;
	}
}
