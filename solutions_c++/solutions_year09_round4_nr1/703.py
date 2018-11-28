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
	int T,N;
	int mt[41][41];
	int rows[41];
//	ifstream fin("A-small-attempt0.in");
	ifstream fin("A-large.in");
//	ofstream fout("A-small.out");
	ofstream fout("A-large.out");
	string ss;
	getline(fin,ss);
	T = strToInt(ss);
	for(int tc=1;tc<=T;tc++){
		int count = 0;
		getline(fin,ss);
		N = strToInt(ss);
		for(i=1;i<=N;i++){
			rows[i] = 0;
			for (j=1;j<=N;j++)
				mt[i][j] = 0;
		}
		for(i=1;i<=N;i++){
			getline(fin,ss);
			//cout<<ss<<endl;
			for (j=1;j<=N;j++){
				mt[i][j] = ss.at(j-1)-'0';
				if(mt[i][j]==1)
					rows[i] = j;
			}
		}
		for(i=1;i<=N;i++){
			if(rows[i]>i){
				for(j=i+1;j<=N;j++){
					if(rows[j]<=i)
						break;
				}
				for(k=j;k>i;k--){
					rows[k] = rows[k-1];
				}
				count += (j-i);
			}
		}
		fout<<"Case #"<<tc<<": "<<count<<endl;

	}
	system("PAUSE");
	return EXIT_SUCCESS;
}
