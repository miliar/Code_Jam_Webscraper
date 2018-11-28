#include <vector>
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int length(int n)
{
	int l = 0;
	for( ; n != 0 ; n/=10, l++);
	return l;
}

//n le nombre
//sizeN = length(n)
//nMove = le nombre à move
int move(int n, int sizeN, int nMove)
{
	int sizeRest = (sizeN - nMove);
	int p10 = pow(10, nMove);
	int p10Rest = pow(10, sizeRest);
	int res = n % p10 * p10Rest + n / p10;
	return res;
}

int resolved(int a, int b)
{
	int count = 0;
	int moved;
	int l;
	//probleme : 1212 => 2121 en deplacant 1 ou 3
	vector<int> ok;
	bool test;
	for(int na = a ; na < b ; na++)
	{
		l = length(na);
		for(int i = 1 ; i < l ; ++i)
		{
			moved = move(na, l, i);
			if(moved > na && moved <= b)
			{
				test = true;
				for(unsigned int k = 0 ; k < ok.size() ; ++k)
					if(ok[k] == moved)
						test = false;
				if(test)
				{
					ok.push_back(moved);
					count++;
				}
			}
		}
		ok.clear();
	}

	return count;
}

int main(int argc, char *argv[])
{
	int numberOfTest;
	int a, b;

	cin >> numberOfTest;
	for(int i = 0 ; i < numberOfTest ; ++i)
	{
		cerr << (i+1) << endl;
		cin >> a;
		cin >> b;
		cout << "Case #" << (i+1) << ": " << resolved(a, b) << endl;
	}

	return 0;
}
