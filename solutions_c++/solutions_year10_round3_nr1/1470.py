/*
 * main.cpp
 *
 *  Created on: 23/Mai/2010
 *      Author: Bisc8
 */

#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main()
{
	int T,N;

	string filename = "A-large";
	freopen((filename+".in").c_str(), "r", stdin);
	freopen((filename+".out").c_str(), "w", stdout);

	cin >> T;

	for(int a = 0; a < T; a++)
	{
		cin >> N;

		vector< pair<int,int>  > pontos;

		for(int n = 0; n < N; n++)
		{
			int A, B;

			cin >> A;
			cin >> B;

			pair<int, int> p;
			p.first = A;
			p.second = B;

			pontos.push_back(p);
		}

		int count = 0;

		int i = 0;

		while(pontos.size() != 0)
		{
			pair<int, int> ponto1 = pontos[i];

			for(unsigned int j = 0; j < pontos.size(); j++)
			{
				pair<int,int> ponto2 = pontos[j];

				if((ponto2.first < ponto1.first && ponto2.second > ponto1.second) ||
					ponto2.first > ponto1.first && ponto2.second < ponto1.second)
				{
					count++;
				}
			}

			pontos.erase(pontos.begin() + i);
			i++;
		}

		cout << "Case #" << (a+1) << ": " << count << endl;
	}
}
