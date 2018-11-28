#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <iostream>
#include <fstream>
using namespace std;
#define PI 3.14159265358979323846264338327950288
#define ok(a, b) ((a) >= 0 && (a) < N && (b) >= 0 && (b) < M && mat[a][b] == '.')

ifstream fin("c:\\D-large.in");
ofstream fout("c:\\D-large.out");

int run()
{
	int N;
	fin >> N;
	int ret = 0;
	vector<int> t,q;
	for ( int n = 0; n < N; n++)
	{
		int tmp;
		fin >> tmp;
		t.push_back(tmp);
	}
	q = t;
	sort(q.begin(),q.end());
	for ( int n = 0; n < N; n++)
		if ( q[n] != t[n] ) ret++;
	return ret;
	
}
int main() {
  
	int N;
	fin>> N;
	for( int n = 1; n <= N; n++)
	{
		int ret = run();
		//printf("Case #%d: %d\n", n, ret);
		fout<<"Case #"<<n<<": "<<ret<<endl;
   }
   return 0;
}