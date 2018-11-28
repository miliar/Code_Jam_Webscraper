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

ifstream fin("c:\\A-large.in");
ofstream fout("c:\\A-large.out");

int run()
{
	int tm[2];
	int pos[2];
	tm[0]=tm[1] = 0;
	pos[0]=pos[1] = 1;
	
	int N;
	fin >> N;
	for ( int i = 0; i < N; i++)
	{
		char c;
		int nxtP;
		fin >> c >> nxtP;
		int id;
		if ( c=='O') id = 0; else id = 1;
		
		int t1 = tm[1 - id];
		int t2 = tm[id] + abs(nxtP - pos[id]);
		if ( t2 > t1 ) t1 = t2;
		tm[id] = t1 + 1;
		pos[id] = nxtP;
		//cout<<tm[0]<<' '<<pos[0]<<" || "<<tm[1]<<' '<<pos[1]<<endl;
	}
	if (tm[0] > tm[1]) return tm[0];
	return tm[1];
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