#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <cstdio>
#include <cmath>
#include <ctime>

#include <fstream>

using namespace std;
#define F(I,N) for(int I=0; I<N; ++I)
#define FR(I,N) for(int I=N-1; I>=0; --I)
#define FE(IT,CONTAINER) for(IT = CONTAINER.begin(); IT != CONTAINER.end(); ++IT)
#define FER(IT,CONTAINER) for(IT = CONTAINER.rbegin(); IT != CONTAINER.rend(); ++IT)
#define INT(DBL) (int)(DBL + 0.000001)
#define LAST(C) C[C.size()-1]


void main() {
	ifstream infile;
	ofstream outfile;
	infile.open ("G:\\Users\\Pio\\Desktop\\A-large.in", ifstream::in);
	outfile.open("G:\\Users\\Pio\\Desktop\\out.txt", ifstream::out);
	int T;
	infile>>T;
	F(i,T) {
		int N;
		infile>>N;
		int res=0;
		int opos=1;
		int bpos=1;
		int otime=0;
		int btime=0;
		F(j,N) {
			int pos;
			char robo;
			infile>>robo>>pos;
			if (robo == 'B') {
				int t = abs(bpos-pos);
				t = max(0,t-btime);
				t++;
				res += t;
				btime = 0;
				otime += t;
				bpos = pos;
			} else {
				int t = abs(opos-pos);
				t = max(0,t-otime);
				t++;
				res += t;
				otime = 0;
				btime += t;
				opos = pos;
			}
		}
		outfile<<"Case #"<<i+1<<": "<<res<<endl;
	}
	infile.close();
	outfile.close();
}