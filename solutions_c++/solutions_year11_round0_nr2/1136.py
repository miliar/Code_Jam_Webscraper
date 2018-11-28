/*
ID: ebappa11
PROG: solder
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>



#define MAXN 105
using namespace std;

int main() {
	ofstream out ("B.out");
	ifstream in ("B.in");


	int ts, C, D, N;
	char a, b, c;
	int base[8] = {(int)'Q'-(int)'A', (int)'W'-(int)'A', (int)'E'-(int)'A', (int)'R'-(int)'A', (int)'A'-(int)'A', (int)'S'-(int)'A', (int)'D'-(int)'A', (int)'F'-(int)'A'};
	int pair[26][26];
	int foe[26];
	vector <int> v;
	int fp[26];

	for (unsigned int i = 0; i < 26; i += 1)
	{
		for (unsigned int j = 0; j < 26; j += 1)
		{
			pair[i][j]=-1;
		}
	}
	for (unsigned int i = 0; i < 26; i += 1)
	{
		foe[i] = -1;
	}

	for (unsigned int i = 0; i < 26; i += 1)
	{
		fp[i] = 0;
	}

	in >> ts;

	for (unsigned int t = 0; t < ts; t += 1)
	{
		for (unsigned int i = 0; i < 8; i += 1)
		{
			for (unsigned int j = 0; j < 8; j += 1)
			{
				pair[base[i]][base[j]] = -1;
			}
		}

		for (unsigned int i = 0; i < 8; i += 1)
		{
			foe[base[i]] = -1;
		}
		for (unsigned int i = 0; i < 8; i += 1)
		{
			fp[base[i]] = 0;
		}
		in >> C;
		for (unsigned int i = 0; i < C; i += 1)
		{
			in >> a >> b >> c;
			pair[(int)a-(int)'A'][(int)b - (int)'A']=(int)c - (int)'A';
			pair[(int)b-(int)'A'][(int)a - (int)'A']=(int)c - (int)'A';
		}
		in >> D;
		for (unsigned int i = 0; i < D; i += 1)
		{
			in >> a >> b;
			foe[(int)a - (int)'A'] = (int)b - (int)'A';
			foe[(int)b - (int)'A'] = (int)a - (int)'A';
		}
		in >> N;
		for (unsigned int i = 0; i < N; i += 1)
		{
			in >> a;
			//cout << "inputted " << a << "\n";

			if (v.size() >=1 && pair[v[v.size()-1]][(int)a -(int)'A'] != -1)
			{
				if (foe[v[v.size()-1]] != -1 && fp[foe[v[v.size()-1]]] >= 1)
				{
					fp[foe[v[v.size()-1]]] -- ;
				}
				v[v.size()-1] = pair[v[v.size()-1]][(int)a -(int)'A'];
				
			}
			else if (fp[(int)a -(int)'A'] >= 1)
			{
				v.clear();
				//cout << "i'm here!\n";
				//cout << "foe[" << a << "=" << (char)(foe[(int)a -(int)'A']+(int)'A') << "\n";
				for (unsigned int i = 0; i < 8; i += 1)
				{
					fp[base[i]] = 0;
				}
			}
			else
			{
				v.push_back((int)a -(int)'A');
				//cout << "foe[" << a << "=" << (char)(foe[(int)a -(int)'A']+(int)'A') << "and fp=";
				//cout << fp[(int)a - (int)'A'] << "\n";
				if (foe[(int)a -(int)'A'] != -1)
				{
					fp[foe[(int)a -(int)'A']] ++;
				}
			}
		}
		out << "Case #" << t+1 << ": [";
		if (v.size()==0)
		{
			out << "]\n";
		}
		else if(v.size() == 1)
		{
			out << (char)( v[0] + (int)'A' ) << "]\n";
		}
		else
		{
			for (unsigned int i = 0; i < v.size()-1; i += 1)
			{
				out << (char)(v[i]+(int)'A') << ", ";
			}
			out << (char)( v[v.size()-1] + (int)'A' ) << "]\n";
		}
		v.clear();
	}
	
	return 0;
}








