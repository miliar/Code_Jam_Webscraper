#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
//#include <cstdio>  
//#include <cstdlib>  
//#include <cctype> 
#include <cmath>  
#include <list>  
using namespace std;  

//a to b-1
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n)  
//a to b
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)
typedef long long ll;

#define IPSET 100

void algo(int testNum) 
{
	// read each test inputs..
	int nplay; 
	unsigned long int jefLn, jefHn;
	cin >> nplay >> jefLn >> jefHn;

	unsigned long int othN[IPSET+5]={0};	
	for( int i = 0; i < nplay; i++) cin >> othN[i];

	unsigned long int jefNLows = 0;
	bool possible = false;
	for(unsigned long int jefN = jefLn; jefN <= jefHn; jefN++ )
	{
		possible = true;
		for( int i = 0; i < nplay && possible; i++)
		{
			possible &= (jefN!=0 && (othN[i] % jefN == 0) ) ||
				(othN[i] !=0 && (jefN % othN[i] == 0 ));
		}
		if(possible)
		{
			jefNLows = jefN; break;
		}
	}


	cout << "Case #" << testNum << ": ";
	if(possible) cout << jefNLows ;
	else cout << "NO";
	cout << endl;
}

int main() {
	int test_num=0;
	cin >> test_num;
	
	FORE(i,1,test_num) algo(i);

	return 0;
}