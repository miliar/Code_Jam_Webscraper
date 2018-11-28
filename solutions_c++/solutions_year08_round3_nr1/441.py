//---------------------------------------------------------------------------

#pragma hdrstop
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
//---------------------------------------------------------------------------

#pragma argsused

using namespace std;

typedef long long LL;

struct Lett{
	int id;
	int freq;
	int pos;
	int hit;
};

bool operator<(const Lett& a, const Lett& b) {
    return a.freq > b.freq;
}

int main(int argc, char* argv[])
{
	ifstream in("input.txt");
	ofstream out("output.txt");



	int N;

	in >> N;
	for( int i = 0; i < N; i++ ){

		int P, K, L;


		vector<Lett> letters;

		in >> P >> K >> L;


		for (int j = 0; j < L; j++) {
			Lett l;
			l.id = j;
			in >> l.freq;
			letters.push_back(l);
		}

		sort(letters.begin(), letters.end() );

		map<LL,LL> keyb;
		
		LL p = 1;
		LL hit = 0;
		for( int j = 0; j < L; j++ ){
			letters[j].pos = p;
			hit += letters[j].freq * p;
            keyb[p]++;
			if( (j+1) >= K*p ) p++;         
        }
		
		out << "Case #" << i + 1<< ": " << hit << endl;
	}

	in.close();
	out.close();

	return 0;
}
//---------------------------------------------------------------------------
