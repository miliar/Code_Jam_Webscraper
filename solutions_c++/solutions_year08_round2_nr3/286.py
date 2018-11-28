#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <deque>
#include <list>
#include <map>
#include <bitset>
#include <functional>
#include <numeric>
#include <string>
#include <iterator>
#include <limits>
#include <sstream>
#include <iostream>
#include <conio.h>
using namespace std;

int main()
{
	ifstream In("C.in");
	ofstream Out("C.out");
	int Cases = 0;
	In >> Cases;
	for(unsigned int i = 0; i < Cases; ++i)
	{
		int Cards = 0;
		In >> Cards;
		
		int Required = 0;
		In >> Required;

		vector<int> RequiredIndices;
		for(unsigned int j = 0; j < Required; ++j)
		{
			int t;
			In >> t;
			RequiredIndices.push_back(t);
		}

		vector<int> Deck;
		Deck.resize(Cards);
		fill(Deck.begin(), Deck.end(), -1);
		int Index = 0;
		for(unsigned int j = 0; j < Cards; ++j)
		{
			int Count = 0;
			while(true)
			{
				if(Count > Cards)
				{
					cout << "Something wrong!";
					getch();
				}
				if(Index == Cards)
					Index = 0;
				if(Deck[Index] != -1)
				{
					++Index;
					continue;
				}
				else
				{
					if(Count == j)
					{
						Deck[Index] = j;
						break;
					}
					else
					{
						++Index;
						++Count;
					}
				}
			}
		}
		if(find(Deck.begin(), Deck.end(), -1) != Deck.end())
		{
			cout << "Something wrong!";
			getch();
		}
		if(i != 0)
			Out << endl;
		Out << "Case #" << i+1 << ":";
		for(unsigned int j = 0; j < RequiredIndices.size(); ++j)
		{
			Out << " " << Deck[RequiredIndices[j] - 1] + 1;
		}
	}
	return 0;
}