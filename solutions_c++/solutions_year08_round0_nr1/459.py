//#include <math.h>
#include <map.h>
#include <list.h>
#include <iostream.h>
#include <iomanip.h>
//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused

int nSE = 0;
int nQL = 0;
int * Q = NULL;
int * brkAt = NULL;
int * curMin = NULL;

void Read()
{
	if( Q != NULL ) {
		delete[] Q;
		Q = NULL;
	}
	if( brkAt != NULL ) {
		delete[] brkAt;
		brkAt = NULL;
	}
	if( curMin != NULL ) {
		delete[] curMin;
		curMin = NULL;
	}

	cin >> nSE;
	cin.get();
	map<string, int> e2i;
	for( int i = 0; i < nSE; ++i ) {
		char buf[256];
		cin.getline(buf, 256);
		string s = buf;
		e2i[string(buf)] = i;
	}
/*
	for( map<string, int>::iterator i = e2i.begin(); i != e2i.end(); ++i ) {
		cout << i->first << ":" << i->second << endl;
	}
*/
	cin >> nQL;
	cin.get();
	Q = new int[nQL];
	for( int i = 0; i < nQL; ++i ) {
		char buf[256];
		cin.getline(buf, 256);
		Q[i] = e2i[string(buf)];
	}
/*
	cout << "q.read ok\n";
	for( int i = 0; i < nQL; ++i ) {
		cout << Q[i] << endl;
	}
*/
	brkAt = new int[nSE * nQL];
	for( int i = 0; i < nSE; ++i ) {
		int curpos = nQL;
		for( int j = nQL - 1; j >= 0; --j ) {
			if( Q[j] == i ) {
				brkAt[nSE * j + i] = -1;
				curpos = j;
			} else {
				brkAt[nSE * j + i] = curpos;
			}
		}
	}
/*
	cout << "tab ok\n";
	for( int i = 0; i < nQL; ++i ) {
		for( int j = 0; j < nSE; ++j ) {
			cout << brkAt[i * nSE + j] << ",";
		}
		cout << endl;
	}
*/
	curMin = new int[nSE * nQL];
	for( int i = 0; i < nSE * nQL; ++i ) {
		curMin[i] = -1;
	}
}

struct curSol {
	int curPos;
	int curSwt;
	int curSE;
};

int Solve()
{
	if( nQL == 0 ) {
		return 0;
	}
	list<curSol> q;
	curSol cs;
	cs.curPos = 0;
	cs.curSwt = 0;
	for( int i = 0; i < nSE; ++i ) {
		if( Q[0] == i ) {
			continue;
		}
		cs.curSE = i;
		cs.curPos = brkAt[i];
		if( brkAt[i] == nQL ) {
			return 0;
		}
		q.push_back(cs);
	}
//	int i = 0;
	do {
		cs = *q.begin();
/*
		cout << "step:" << i++ << endl;
		cout << "q.len:" << q.size() << endl;
		cout << "curPos:" << cs.curPos << ",";
		cout << "curSwt:" << cs.curSwt << ",";
		cout << "curSE:" << cs.curSE << endl;
*/
		q.pop_front();
		++cs.curSwt;
		int curPos = cs.curPos;
		for( int i = 0; i < nSE; ++i ) {
			cs.curPos = brkAt[curPos * nSE + i];
			if( cs.curPos == nQL) {
				return cs.curSwt;
			}
			if( cs.curPos < 0 ) {
				continue;
			}
			cs.curSE = i;
			if( curMin[cs.curPos * nSE + cs.curSE] >= 0 && curMin[cs.curPos * nSE + cs.curSE] <= cs.curSwt ) {
				continue;
			}
			curMin[cs.curPos * nSE + cs.curSE] = cs.curSwt;
			q.push_back(cs);
		}
	} while( !q.empty() );
	return 0;
}

int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	for( int i = 0; i < N; ++i ) {
		Read();
		cout << "Case #" << i + 1 << ": " << Solve() << endl;
	}
	return 0;
}
//---------------------------------------------------------------------------
