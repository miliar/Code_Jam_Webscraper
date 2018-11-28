#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <fstream>

using namespace std;

#define all(x) (x).begin(),(x).end()
#define forn(i,s,e) for(int i=(s),_e=(e);i<_e;i++)
#define rep(i,n) forn(i,0,n)
#define pb push_back 
#define db(i) cout<<#i<<"= "<<i<<endl; 

ifstream fin("A-large.in.txt");
ofstream fout("output.out");

int main()
{
	int nCases;
	fin >> nCases;
	long long n, k;
	for (int ij = 1; ij <= nCases; ij++)
	{
		fin >> n >> k;
		int rem = ( k - ( (1LL << n) - 1 ) ) % (1LL << n);
		fout << "Case #" << ij << ": ";
		if ( rem == 0 )
			fout << "ON" << "\n";
		else 
			fout << "OFF" << "\n";
	}		
    printf("done\n");
    int z;
    scanf("%d",&z);
    return 0;
}
