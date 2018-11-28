#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
#include <deque>

using namespace std;
#define forl(i,a,b) for(int i = a; i < b; ++i)

struct combination {
char a;
char b;
char out;
};

struct opposition {
char a;
char b;
};

deque<char> elems;
deque<combination> combs;
deque<opposition> opps;
int elemc[26];

void clearcounts()
{
	forl(i,0,26) elemc[i] = 0;
}

int countindex(char c)
{
	return (c - 'A');
}

void pushelem(char elem)
{
	if (!elems.size()) { elems.push_back(elem); elemc[countindex(elem)]++; return;}
	char c = elems.back();
	for (deque<combination>::iterator it = combs.begin(); it != combs.end(); ++it)
	{
		combination cm = *it;
		if (cm.a == c && cm.b == elem || cm.b == c && cm.a == elem)
		{
			elems.pop_back();
			elemc[countindex(c)]--;
			pushelem(cm.out);
//			elems.push_back
			return;
		}
	}
	for (deque<opposition>::iterator it = opps.begin(); it != opps.end(); ++it)
	{
		opposition cm = *it;
		if (cm.a == elem && elemc[countindex(cm.b)] || cm.b == elem && elemc[countindex(cm.a)])
		{
			clearcounts();
			elems.clear();
			return;
		}
	}

	elems.push_back(elem);
	elemc[countindex(elem)]++;
}


main()
{
	ifstream instr("testb.in");
	ofstream outstr("testb.out");

	int numCases;
	instr >> numCases;

	forl(ccase,0,numCases)
	{
		int numMoves = 0;
		int numComb, numOpp;
		instr >> numComb;
		combs.clear();
		forl(i,0,numComb) {
			string blah;
			instr >> blah;
			combination c;
			c.a = blah[0];
			c.b = blah[1];
			c.out = blah[2];
			combs.push_back(c);
		}
		instr >> numOpp;
		opps.clear();
		forl(i,0,numOpp) {
			string boo;
			instr >> boo;
			opposition o;
			o.a = boo[0];
			o.b = boo[1];
			opps.push_back(o);
		}
		instr >> numMoves;
		string moves;
		instr >> moves;
		elems.clear();
		clearcounts();
		forl(i,0,numMoves) {
			pushelem(moves[i]);
		}

		outstr << "Case #" << ccase+1 << ": [";
		for (deque<char>::iterator it = elems.begin(); it != elems.end(); ++it)
			outstr << *it << (((it+1) != elems.end())?", ":"");
		outstr << "]" << endl;
	}


}

	
