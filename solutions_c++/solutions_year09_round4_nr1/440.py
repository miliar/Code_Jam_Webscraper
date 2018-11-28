#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iterator>
#include <utility>
#include <functional>
#include <algorithm>
#include <numeric>
#include <complex>
#include <bitset>
#include <valarray>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define SET(A,p) memset(A,p,sizeof(A))

//fix the file name here!
#define fname "A-large"

ifstream in;
ofstream out;

vector<string> A;
vector<int> V;

void do_case(int case_no)
{
	int N;
	in >> N;
	A.clear(); A.resize(N);
	V.clear(); V.resize(N);
	FOR(i,0,N) in >> A[i];
	FOR(i,0,N)
	{
		int er = 0;
		FOR(j,0,N) if(A[i][j] == '1') er = j;
		V[i] = er;
	}
	int res=0;
	FOR(i,0,N)
	{
		int mi;
		FOR(j,i,N) if(V[j] <= i) { mi=j; break;}
		res+=mi-i;
		for(int j=mi;j>i;j--)swap(V[j],V[j-1]);
	}
	cout << "Case #" << case_no << ": " << res << endl; // Change this in case the output requires it!
	out << "Case #" << case_no << ": " << res << endl;
}

int main()
{
	in.open(fname ".in");
	out.open(fname ".out");
	int T;
	in >> T; // Change this in case the input requires it!
	FOR(te,1,T+1) do_case(te);
	in.close();
	out.close();
	return 0;
}
