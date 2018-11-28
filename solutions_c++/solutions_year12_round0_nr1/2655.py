

#include<cstdio>
#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<stack>
#include<list>
#include<queue>
#include<deque>
#include<cctype>
#include<string>
#include<vector>
#include<sstream>
#include<iterator>
#include<numeric>
#include<cmath>
#include<cstring>
#include<complex>
#include<cstdlib>
#include<climits>
#include<bitset>
using namespace std;
#define RFOR(i,a,b) for(int i=a; i > b; i--)
#define FOR(i,a,b) for(int i=a; i < b;i++)
#define PB push_back
#define BN begin()
#define ED end()
#define RN rbegin()
#define RD rend()
#define PF push_front
#define BP pop_back
#define FP pop_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN) 
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it) 
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it)
#define VV(X) vector< vector< X > > 
#define PIB(X) pair<IT(X),bool>
#define SQ ((x)*(x))
#define El() cout<<endl;

typedef long long LL;
typedef unsigned long long ULL;
typedef istringstream ISS;
typedef stringstream SS;
typedef vector<int> VI;
typedef pair <int,int> PII;
typedef vector< PII > VPII;

using namespace std;
int main()
{
        int cas,n=1,k;
	cin >> cas;
	while(n<=cas)
	{char ch[100];
	//cin >> ch;
	cin >> k;
	gets(ch);
	int l=strlen(ch);
//	cout <<l;
	cout<<"Case #"<<n<<": ";
	//while(ch!="\n")
	FOR(i,0,l)
	{
	switch(ch[i])
	{
	case 'a':cout<<"y";
		break;
	case 'b':cout<<"h";
                break;
	case 'c':cout<<"e";
                break;
	case 'd':cout<<"s";
                break;
	case 'e':cout<<"o";
                break;
	case 'f':cout<<"c";
                break;
	case 'g':cout<<"v";
                break;
	case 'h':cout<<"x";
                break;
	case 'i':cout<<"d";
                break;
	case 'j':cout<<"u";
                break;
	case 'k':cout<<"i";
                break;
	case 'l':cout<<"g";
                break;
	case 'm':cout<<"l";
                break;
	case 'n':cout<<"b";
                break;
	case 'o':cout<<"k";
                break;
	case 'p':cout<<"r";
                break;
	case 'q':cout<<"z";
                break;
	case 'r':cout<<"t";
                break;
	case 's':cout<<"n";
                break;
	case 't':cout<<"w";
                break;
	case 'u':cout<<"j";
                break;
	case 'v':cout<<"p";
                break;
	case 'w':cout<<"f";
                break;
	case 'x':cout<<"m";
                break;
	case 'y':cout<<"a";
                break;
	case 'z':cout<<"q";
                break;
	default:cout<<" ";
	}}

	n++;		
	cout<<endl;
	}

	return 0;
}
