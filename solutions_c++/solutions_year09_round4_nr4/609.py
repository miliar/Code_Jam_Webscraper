#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;
string intToStr(int k){
	ostringstream os;
	os << k;
	return os.str();
}

int strToInt(string s){
	istringstream is(s);
	int ri;
	is >> ri;
	return ri;
}

int main(int argc, char *argv[])
{
	int i,j,k;
	int C,N;
	int X[3],Y[3],R[3];
	ifstream fin("D-small-attempt2.in");
	//	ifstream fin("D-large-practice.in");
	ofstream fout("D-small.out");
	//	ofstream fout("D-large.out");
	string ss;
	getline(fin,ss);
	C = strToInt(ss);
	for(int tc=1;tc<=C;tc++){
		getline(fin,ss);
		N = strToInt(ss);
		for(i=0;i<N;i++){
			getline(fin,ss);
			istringstream is(ss);
			is >> X[i] >> Y[i] >> R[i];
		}
		double maxD = 100000.0;
		for(i=0;i<N;i++){
			for(j=i+1;j<N;j++){
				double d = (Y[j]-Y[i])*(Y[j]-Y[i])+(X[j]-X[i])*(X[j]-X[i]);
				double tmp = (sqrt(d) + R[i] + R[j])/2;
				if(tmp<R[N-i-j])
					tmp = R[N-i-j];
				if(tmp<maxD)
					maxD = tmp;
			}
		}
		if(N==1){
			maxD = R[0];
		}else if(N==2){
			maxD = R[0]>R[1]?R[0]:R[1];
		}
		printf("Case #%d: %.6f\n",tc,maxD);
	}
	system("PAUSE");
	return EXIT_SUCCESS;
}
