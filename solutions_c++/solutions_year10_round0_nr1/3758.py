

/* Author : Sanidhya Kashyap */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define F(i,a) for(int i=0;i<a;i++)
#define FD(i,b) for(int i=b;i>=0;i--)
#define F1(i,a,b) for(int i=a;i<b;i++)
#define FD1(i,a,b) for(int i=b;i>=a;i--)
#define REP(i,a,b,c) for(int i=a;i<=b;i+=c)
#define PB(X) push_back(X)
#define MP(X,Y) make_pair(X,Y)
#define SIZE(X) ((int)(X.size()))
#define Length(X) ((int)(X.length()))
#define ALL(X) (X.begin(),X.end())
#define INF 100000000
#define S scanf
#define P printf
#define LB lower_bound 

typedef long long LL;
typedef long double LD;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef pair<int,string> pis;
typedef pair<string,int> psi;
typedef pair<int, pii > piii;


int main()
{
	LL k,n;
	int t;
	S("%d",&t);
	F(i,t)
	{
		S("%Ld%Ld",&n,&k);
		k%=(1<<n);
		P("Case #%d: ",i+1);
		k==((1<<n)-1)?puts("ON"):puts("OFF");
	}
	return 0;
}
