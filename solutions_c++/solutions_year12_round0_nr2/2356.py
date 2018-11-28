#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
using namespace std;

ifstream fin("in");
ofstream fout("out");

const int MAXN = 101;
int points[MAXN];
int N,S,p;

struct triplet {
	int a,b,c;
};

triplet getaverage(int score) {
	triplet t;
	t.a = score/3;
	t.b = (score-t.a)/2;
	t.c = score-t.a-t.b;
	return t;
}

/**
 *	0: all equal
 *	1: 1 off
 *	2: 2 off
 */
int getcase(triplet t) {
	if(t.a==t.c)
		return 0;
	else if(t.b==t.a)
		return 1;
	else
		return 2;
}

/**
 * 0: achieves, no surprise
 * 1: achieves, with surprise
 * 2: cannot achieve
 */
int canachieve(triplet t) {
	int thiscase = getcase(t);
	switch(thiscase) {
	case 0:
		if(t.a>=p)
			return 0;
		else if(t.a+1>=p && t.a>=1)
			return 1;
		else
			return 2;
		break;
	
	case 1:
		if(t.a+1>=p)
			return 0;
		else
			return 2;
		break;
	
	case 2:
		if(t.a+1>=p)
			return 0;
		else if(t.a+2>=p && t.a<=8)
			return 1;
		else
			return 2;
		break;
	default:
		return 2;
	}
}

int getmaxgoog() {
	int n0=0, ns=0;
	for(int i=0; i<N; i++) {
//		triplet t = getaverage(points[i]);
//		cout << points[i] << ": " << t.a << " " << t.b << " " << t.c << endl;
		int x = canachieve(getaverage(points[i]));
		if(x==0)
			n0++;
		else if(x==1)
			ns++;
	}
	return n0 + ( (ns<S)?ns:S );
}

int main() {
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		fin>>N>>S>>p;
		for(int i=0; i<N; i++)
			fin>>points[i];
		int maxgoog = getmaxgoog();
		fout << "Case #" << t << ": " << maxgoog << endl;
	}
	return 0;
}




