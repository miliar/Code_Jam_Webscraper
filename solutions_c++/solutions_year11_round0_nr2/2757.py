#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <algorithm>
using namespace std;

enum RELATION{NOTHING, CANDIDATED, INVOKED};
struct Combination{
	char m_a, m_b, m_c;

	Combination(char a = '\0', char b = '\0', char c = '\0') { m_a = a; m_b = b; m_c = c; }
	RELATION check(char a, char b)
	{
		if( (a == m_a && b == m_b) || (b == m_a && a == m_b) ) return INVOKED;
		if( a == m_a || a == m_b || b == m_a || b == m_b ) return CANDIDATED;

		return NOTHING;
	}
};

struct Opposition{
	char m_a, m_b;

	Opposition(char a = '\0', char b = '\0') { m_a = a; m_b = b; }
	RELATION check(char a, char b)
	{
		if( (a == m_a && b == m_b) || (b == m_a && a == m_b) ) return INVOKED;
		if( a == m_a || a == m_b || b == m_a || b == m_b ) return CANDIDATED;

		return NOTHING;
	}
};

void foo( char spell, list<char> & spells, vector<Combination> & combinations, vector<Opposition> & oppositions) 
{
	if( spells.empty() )
	{
		spells.push_back(spell);
		return;
	}

	for(unsigned int i = 0; i < combinations.size(); i++){
		if( combinations[i].check(spell, spells.back()) == INVOKED ){
			// COMBINE SPELL
			spells.pop_back();
			spells.push_back(combinations[i].m_c);
			return;
		}
	}

	for(list<char>::iterator it = spells.begin(); it != spells.end(); it++){
		for(unsigned int j = 0; j < oppositions.size(); j++){
			if( oppositions[j].check(spell, *it) == INVOKED ){
				spells.clear();
				return;
			}
		}
	}

	spells.push_back(spell);
}

int main(int _argc, char* _argv)
{
	ifstream infile;
	ofstream outfile;
	string line;

	infile.open("B.in");
	outfile.open("B.out");

	int cases = 0;
	infile >> cases;

	for( int i = 1; i <= cases; i++ ){
		int C, D, N;
		vector<Combination> combinations;
		vector<Opposition> oppositions;
		list<char> spells;

		infile >> C;
		combinations.resize(C);
		for( int j = 0; j < C; j++ ){
			string comb_buf;
			infile >> comb_buf; 
			combinations[j] = Combination(comb_buf[0], comb_buf[1], comb_buf[2]);
		}

		infile >> D;
		oppositions.resize(D);
		for( int k = 0; k < D; k++ ){
			string oppo_buf;
			infile >> oppo_buf;
			oppositions[k] = Opposition(oppo_buf[0], oppo_buf[1]);
		}

		infile >> N;
		string notes;
		
		getline(infile, notes);
		remove(notes.begin(), notes.end(), ' ');

		spells.push_back(notes[0]);
		for( int m = 1; m < N; m++ ){
			foo(notes[m], spells, combinations, oppositions);
		}

		outfile << "Case #" << i << ": [";
		for(list<char>::iterator it = spells.begin(); it != spells.end(); it++) 
		{
			if ( it != spells.begin() ) outfile << ", ";
			outfile << *it;
		}

		outfile << "]" << endl;
	}

	infile.close();
	outfile.close();

	return 0;
}