#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
#include <deque>

#define forl(i,a,b) for(int i = a; i < b; ++i)

using namespace std;

int oP=1, bP=1;
deque<int> orange;
deque<int> blue;
deque<bool> next;


int iterate()
{
	int count = 0;
	int nextoP = orange.size()?orange.front():-1;
	if (nextoP != -1) orange.pop_front();
	int nextbP = blue.size()?blue.front():-1;
	if (nextbP != -1) blue.pop_front();
	bool nextbot = next.size()?next.front():false;
	next.pop_front();
	while (true)
	{
		bool pushed = false;
		if (nextoP == -1 && nextbP == -1) return count;
		count++;
		if (oP < nextoP) oP++; else if (oP > nextoP) oP--; else if (nextbot == false) {
			// Push the button
			if (nextoP != -1) pushed = true;
			if (orange.size())
			{
				nextoP = orange.front();
				orange.pop_front();
			}

			else nextoP = -1;
			if (next.size()) {
			nextbot = next.front();
			next.pop_front(); }
		}
			
		if (bP < nextbP) bP++; else if (bP > nextbP) bP--; else if (nextbot == true){
			if (pushed) { pushed = false; continue; }
			if (blue.size())
			{
				nextbP = blue.front();
				blue.pop_front();
	
			}

			else nextbP = -1;
			if (next.size()) {
			nextbot = next.front();
			next.pop_front(); }
		}

	}
}


main()
{
	ifstream instr("test.in");
	ofstream outstr("test.out");

	int numCases;
	instr >> numCases;

	forl(ccase,0,numCases)
	{
		int numMoves = 0;
		int nextoP, nextbP;
		char poop;
		oP = 1; bP = 1;
		instr >> numMoves;
		orange.clear();
		blue.clear();
		forl(i,0,numMoves) {
			int z;
			instr >> poop >> z;
			(poop == 'O')?orange.push_back(z):blue.push_back(z);
			next.push_back(poop == 'B');
		}
		outstr << "Case #" << ccase+1 << ": " << iterate() << endl;
	}


}

	
