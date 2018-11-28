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

ifstream in;
ofstream out;

void open() {
	in.open ("G:\\Users\\Pio\\Desktop\\gógl d¿em\\C-large.in", ifstream::in);
	out.open("G:\\Users\\Pio\\Desktop\\gógl d¿em\\out.txt", ifstream::out);
}
template <typename T>
void print(T t) {
	static int testCaseNo = 0;
	if (t == 0) {
		out<<"Case #"<<++testCaseNo<<": NO"<<endl;
		cout<<"Case #"<<testCaseNo<<": NO"<<endl;
	}
	else {
		out<<"Case #"<<++testCaseNo<<": "<<t<<endl;
		cout<<"Case #"<<testCaseNo<<": "<<t<<endl;
	}
}
void close() {
	in.close();
	out.close();
}

int candy() {
	int N;
	in>>N;

	int all = 0;
	int sum = 0;
	int mn = 2100000000;


	F(n,N) {
		int c;
		in>>c;
		all = all ^ c;
		sum += c;
		mn = min(mn, c);
	}
	if (!all)
		return sum-mn;
	return 0;
}


void main() {
	open();
	int T;
	in>>T;
	F(t,T) {
		int res = candy();
		print<int>(res);
	}
	close();
	system("pause");
}