#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list>
#include <cassert>
#include <conio.h>
using namespace std; 

#define PB push_back 
#define MP make_pair 
#define SZ(v) ((int)(v).size()) 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) REP(i,SZ(v)) 
typedef long long ll; 

vector<int> freqs;

void findDiv(unsigned long long f)
{
	for(vector<int>::iterator it = freqs.begin(); it != freqs.end(); ) 
	//vector<int>::iterator it = freqs.begin()
	//REP(i, freqs.size())
	{
		if (((f >= *it) && (f % *it != 0)) ||
			((f < *it) && (*it % f != 0))) 
		{
			it = freqs.erase(it);
		}
		else ++it;
		if (freqs.empty()) return;

	}

}


int main() {
	freopen("..\\..\\IO Files\\C-small-attempt1.in", "r", stdin);
	freopen("..\\..\\IO Files\\C-small1.out", "w", stdout);

	//freopen("..\\..\\IO Files\\testC.in", "r", stdin);
	
	int T, N, L, H;	
	cin >> T;
	REP(i, T)
	{
		cin >> N >> L >> H;
		
		freqs.clear();
		
		FORE(i, L, H) freqs.push_back(i);


		FOR(i, 0, N)
		{
			unsigned long long F;
			cin >> F;
			findDiv(F);
			//if (freqs.empty()) break;
		}

		cout << "Case #" << i+1 << ": ";

		if (freqs.empty())
			cout << "NO" << endl;
		else
		{

			cout << freqs[0] << endl;
		}



	}

	getch();
	return 0;
}