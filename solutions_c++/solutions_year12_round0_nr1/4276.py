#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>
using namespace std;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<=(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 
#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front
#define BN begin()
#define RN rbegin()
#define RD rend()
#define ED end()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it)
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it) 
#define VV(X) vector < vector< X > >
#define PIB(X)  pair<IT(X),bool >  

typedef long long LL;
typedef unsigned long long ULL;
typedef istringstream ISS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;

int main()
{
    int cases,caseNum;
	map <char, char> googlerese;
	googlerese['a']='y';
	googlerese['b']='h';
	googlerese['c']='e';
	googlerese['d']='s';
	googlerese['e']='o';
	googlerese['f']='c';
	googlerese['g']='v';
	googlerese['h']='x';
	googlerese['i']='d';
	googlerese['j']='u';
	googlerese['k']='i';
	googlerese['l']='g';
	googlerese['m']='l';
	googlerese['n']='b';
	googlerese['o']='k';
	googlerese['p']='r';
	googlerese['q']='z';
	googlerese['r']='t';
	googlerese['s']='n';
	googlerese['t']='w';
	googlerese['u']='j';
	googlerese['v']='p';
	googlerese['w']='f';
	googlerese['x']='m';
	googlerese['y']='a';
	googlerese['z']='q';
	googlerese[' ']=' ';
    cin >> cases;
	caseNum = 1;
	cin.ignore();
    while(cases>0)
    {
		string input;
		int i=0;
		getline(cin,input);
		printf("Case #%d: ",caseNum);
		while(1)
		{
			if(input[i]=='\0')
				break;
			printf("%c",googlerese[input[i]]);
			i++;
		}
		printf("\n");
        cases--;
		caseNum++;
    }
    return 0;
}
