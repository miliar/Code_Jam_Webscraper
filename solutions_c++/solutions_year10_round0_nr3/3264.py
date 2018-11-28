/*
 * main.cpp
 *
 *  Created on: 8/Mai/2010
 *      Author: Bisc8
 */

#include <iostream>
#include <vector>
#include <math.h>
#include <queue>

using namespace std;

/*void print(queue<int> fila)
{
	 while (!fila.empty())
	 {
		 cout << fila.front() << " ";
		 fila.pop();
	 }

	cout << endl;
}*/

long totalPeople(queue<int> fila)
{
	long total = 0;

	 while (!fila.empty())
	 {
		 total += fila.front();
		 fila.pop();
	 }

	 return total;
}


long problemB(int R, int K, queue<int> fila)
{
	long total = 0;

	if(fila.size() == 1 && fila.front() <= K)
	{
		return fila.front() * R;
	}

	long t = totalPeople(fila);

	if(t <= K)
	{
		return t * R;
	}

	for(int i = 0; i < R; i++)
	{
		long ride = 0;
		int size = fila.size();

		while((ride + fila.front()) <= K && size != 0)
		{
			ride = ride + fila.front();
			fila.push(fila.front());
			fila.pop();
			size--;
		}

		total = total + ride;
	}

	return total;
}

int main()
{
	int T,K,R,N;

	string filename = "C-small-attempt0";
	freopen((filename+".in").c_str(), "r", stdin);
	freopen((filename+".out").c_str(), "w", stdout);

	cin >> T;

	for(int i = 0; i < T; i++)
	{
		queue<int> fila;

		cin >> R;
		cin >> K;
		cin >> N;

		for(int j = 0; j < N; j++)
		{
			int g = 0;
			cin >> g;
			fila.push(g);
		}

		cout << "Case #" << (i+1) << ": " << problemB(R,K,fila) << endl;
	}

	return 0;
}
