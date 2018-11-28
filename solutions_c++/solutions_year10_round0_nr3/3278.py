#include<iostream>
#include<fstream>
#include<cmath>
#include<deque>
using namespace std;

ifstream lettura ("three.in");
ofstream scrittura ("three.out");

deque<int> coda;
deque<int> carrello;

int r, k;

int elabora ()
{
	int result = 0;
	for (int i = 0; i < r; i++)
	{
		int size = 0;
		while (!coda.empty() && (size + coda.front() <= k))
		{
			size += coda.front();
			result += coda.front();
			carrello.push_back(coda.front());
			coda.pop_front();
		}
		while (!carrello.empty())
		{
			coda.push_back (carrello.front());
			carrello.pop_front();
		}
	}
	return result;
}

int main ()
{
	int t;
	lettura >> t;
	cout << t;
	for (int i = 1; i <= t; i++)
	{
		cout << "1" << endl;
		int n;
		lettura >> r >> k >> n;
		coda.clear();
		for (int j = 0; j < n; j++)
		{
			int a;
			lettura >> a;
			coda.push_back (a);
		}
		scrittura << "Case #" << i << ": ";
		scrittura << elabora ();
		scrittura << endl;
	}
}
