#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend() 
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

vi tab;
int N; 

bool isok()
{
FOR(i,N)
if (tab[i] > i) return false;

return true;
}

void swap()
{
	int i=0;
	for(; i<N; ++i)
	{
		if (tab[i] > i)
			break;
	}

	int j=i+1;
	while(j<N)
	{
		if (tab[j] <= i) {
			swap(tab[j], tab[j-1]);
			return;
		}

		++j;
	}
}

int main(void) {
    int n; cin>>n;

    FOR(_i,n) {
		cin >> N;
		tab.clear();
		FOR(i,N) {
			string s;
			cin >> s;
			int idx = s.find_last_of('1');
			tab.push_back(idx);
		}

		int64 res=0;
		while (isok() == false) 
		{
			swap();
			++res;
		}

        printf("Case #%d: %lld\n", _i+1, res);
    }
    return 0;
}
