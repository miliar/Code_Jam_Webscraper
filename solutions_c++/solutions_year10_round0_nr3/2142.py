#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <fstream>
#include <iostream>
#include <utility>

using namespace std;

#define FOR(i, a, b) for (int i(a); i <= b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0); i < n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef _int64 i64;
typedef unsigned _int64 ui64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

int REMAIN=0;
int POS=0;

void findNext(int remain, int pos, int p[],int N){
		if(p[pos]<remain){
			if(pos==N-1){
				REMAIN-=p[pos];
				findNext(remain-p[pos], 0, p, N);
				return;
			}else{
				REMAIN-=p[pos];
				findNext(remain-p[pos], pos+1, p, N);
				return;
			}
		}else if(p[pos]==remain)
		{
			REMAIN=0;
			if(pos==N-1) POS=0;
			else POS=pos+1;
		}else{
			POS=pos;
		}
}

int main()
{
	ifstream infile("p2.in");
	if(! infile){
		cerr << "error: unable to open input file: "
			<< infile <<endl;
		return -1;
	}
	ofstream outfile("p2.out");
	if(! outfile){
		cerr << "error: unable to open output file: "
			<< outfile <<endl;
		return -2;
	}
	int testCase;
	infile >> testCase;
	REP(tc, testCase){
		outfile<<"Case #"<<tc+1<<": ";
		int R,k,N;
		infile >> R;infile >> k;infile >> N;
		int p[10000];
		REP(i,N){
			infile >> p[i];
		}		
		REMAIN=0;
		POS=0;
		int z=0;
		int res=0;
		REP(a, N){
			z+=p[a];
		}
		REP(j,R){
			if(z<=k) res+=z;
			else{
				REMAIN=k;
				findNext(k,POS,p,N);
				res+=(k-REMAIN);
			}
		}
		outfile<<res<<endl;
	}

	return 0;
}