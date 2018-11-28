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
#define fname "D-small-attempt2"

ifstream in;
ofstream out;

double X[3],Y[3],R[3];

double dist(int a, int b)
{
	return sqrt((X[a]-X[b])*(X[a]-X[b]) + (Y[a]-Y[b])*(Y[a]-Y[b]));
}

void do_case(int case_no)
{
	int N;
	in >> N;
	FOR(i,0,N) in >> X[i] >> Y[i] >> R[i];
	double res = 1e100;
	if(N == 1) res = R[0];
	else if(N == 2) res = max(R[0],R[1]);
	else
	{
		res <?= max(dist(0,1)+R[0]+R[1],R[2])/2;
		res <?= max(dist(0,2)+R[0]+R[2],R[1])/2;
		res <?= max(dist(2,1)+R[2]+R[1],R[0])/2;
	}
	cout << "Case #" << case_no << ": " << res << endl; // Change this in case the output requires it!
	out << "Case #" << case_no << ": " << res << endl; // Change this in case the output requires it!
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
