#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool freeCell[1000000];

int p;

int res = 0;

int q;

int order[1000];

void release(int num)
{
	freeCell[num] = true;
	for (int i = num - 1; i >= 1 && !freeCell[i]; i--)
		res++;
	for (int i = num + 1; i <= p && !freeCell[i]; i++)
		res++;
}



int var()
{
	memset(freeCell, 0, p+1);
	res = 0;
	for (int i = 0; i < q; i++)
		release(order[i]);
	return res;
}

int main()
{
	ifstream input("Input.txt");
	ofstream output("output.txt");
	int tt;
	input >> tt;
	for (int ttt = 1; ttt <= tt; ttt++)
	{
		input >> p;
		memset(freeCell, 0, p);
		input >> q;
		res = 0;
		for (int i = 0; i < q; i++)
		{
			input >> order[i];
		}
		sort(order, order + q);
		int mx = 1000000000;
		do
		{
			mx = min(mx, var());
		} while (next_permutation(order, order + q));
		output << "Case #" << ttt << ": " << mx << '\n';

	} 

	return 0;
}