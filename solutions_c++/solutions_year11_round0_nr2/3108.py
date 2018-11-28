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
	infile.open ("G:\\Users\\Pio\\Desktop\\B-small-attempt0.in", ifstream::in);
	outfile.open("G:\\Users\\Pio\\Desktop\\out.txt", ifstream::out);
	int T;
	infile>>T;
	F(t,T) {
		map<pair<char,char>, char> com;
		map<char, char> ops;
		string out = "";
		int C;
		infile>>C;
		F(c,C) {
			char c1,c2,c3;
			infile>>c1>>c2>>c3;
			com.insert(make_pair(make_pair(c1,c2),c3));
			com.insert(make_pair(make_pair(c2,c1),c3));
		}
		int D;
		infile>>D;
		F(d,D) {
			char c1,c2;
			infile>>c1>>c2;
			ops.insert(make_pair(c1,c2));
			ops.insert(make_pair(c2,c1));
		}
		int N;
		infile>>N;
		F(n,N) {
			char cn;
			infile>>cn;
			while (out.size() > 0 && com.find(make_pair(LAST(out),cn)) != com.end()) {
				cn = com[make_pair(LAST(out),cn)];
				out = out.substr(0,out.size()-1);
			}
			bool clean = false;
			F(i,out.size()) {
				if(ops[out[i]] == cn) {
					clean = true;
					break;
				}
			}
			if (!clean)
				out += cn;
			else 
				out = "";
		}
		string res = "[";
		if (out.size() > 0) {
			F(o,out.size()-1) {
				res += out[o];
				res += ", ";
			}
			res += LAST(out);
		}
		res += "]";
		outfile<<"Case #"<<t+1<<": "<<res<<endl;
	}
	infile.close();
	outfile.close();
}