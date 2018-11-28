#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <sstream>
#include <string>
#include <cstdlib>
#define ABS( A ) (A) < 0 ? -(A) : (A);
using namespace std;
struct bot
{
	char id;
	int btn;
};

int main()
{
	string line;
	int T;
	getline(cin, line);
	T = atoi(line.c_str());
	for(int tcase=1; tcase<=T; ++tcase)
	{
		vector<bot> seq;

		string line;
		getline(cin, line);
		//cout << line << endl;
		istringstream is(line);

		int nSeq;
		is >> nSeq;

		for(int i=0; i < nSeq; ++i)
		{
			bot b;
			char id; int btn;
			is >> id; is >> btn;
			b.id=id, b.btn=btn;
			seq.push_back(b);
		}
		
		int _t=1;
		int oPos = 1, oTime = 0;
		int bPos = 1, bTime = 0;
		for(int i=0; i < nSeq; ++i)
		{
			bot& _b = seq[i];
			int *pos = _b.id == 'O' ? &oPos : &bPos;
			int *t = _b.id == 'O' ? &oTime : &bTime;
			int *t2 = _b.id == 'O' ? &bTime : &oTime;
			int to = _b.btn;
			if( to == *pos )
			{
				*t = *t+1 <= *t2 ? *t2+1 : *t+1;
				*pos = _b.btn;
			}
			else
			{
				int far = ABS( (to)-(*pos) );
				*t = *t+far+1 <= *t2 ? *t2+1 : *t+far+1;
			}
			//printf("?%c %d %d\n", _b.id, _b.btn, *t);
			*pos = _b.btn;
		}
		_t = max(oTime, bTime);

		//printf("Case #%d: %d\n", tcase, _t);
		cout << "Case #" << tcase << ": " << _t << endl;
	}
	return 0;
}
