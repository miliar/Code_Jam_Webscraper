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
#include <sstream>
using namespace std;
#define PI 3.14159265358979323846264338327950288
#define ok(a, b) ((a) >= 0 && (a) < N && (b) >= 0 && (b) < M && mat[a][b] == '.')

ifstream fin("c:\\C-large.in");
ofstream fout("c:\\C-large.out");

string run()
{
	long long fakeSum = 0;
	long long sum = 0;
	long long minV = -1;
	int N;
	fin >> N;
	cout<<N<<endl;
	for ( int n = 0; n < N; n++)
	{
		long long tmp;
		fin >> tmp;
		fakeSum ^= tmp;
		sum += tmp;
		if ( minV < 0 || minV > tmp ) minV = tmp;
	}
	if ( fakeSum > 0 ) return string("NO");
	sum -= minV;
	//cout<<sum<<endl;
	ostringstream ss;
	ss<<sum;
	return ss.str();
}
int main() {

	int N;
	fin>> N;
	cout<<N<<endl;
	for( int n = 1; n <= N; n++)
	{
		string ret = run();
		//printf("Case #%d: %d\n", n, ret);
		fout<<"Case #"<<n<<": "<<ret<<endl;
   }
   return 0;
}