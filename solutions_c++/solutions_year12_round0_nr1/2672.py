/*********************************HEADER FILES************************************/
#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <climits>
#include <cstring>
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define SZ(x) ((int)(x).size())
#define FORV(i,x) FOR(i,0,SZ(x))  
#define DBG(x) cout<<(#x)<<" : "<<(x)<<endl
#define PB push_back
#define ALL(x) x.begin(),x.end()

#define ACC(x) accumulate(ALL(x)) 
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define ROFE(i,a,b) for(int i=(b);i>=(a);i--)
#define MP make_pair
#define left(x) (x<<1)
#define right(x) (left(x)+1)
#define PI pair<int,int>
#define PD pair<double,double>
#define F first
#define S second 
#define LL long long
#define ULL unsigned long long
#define MAX 50010

string rep = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	int cases;
	scanf("%d", &cases); string str;
	char ch = getchar();
	FOR(i, 1, cases + 1)
	{
		getline(cin, str);
		printf("Case #%d: ", i);
		FORV(i, str)
			if(!isalpha(str[i])) printf("%c", str[i]);
			else printf("%c", rep[str[i] - 'a']);
		printf("\n");
	}
	return 0;
}