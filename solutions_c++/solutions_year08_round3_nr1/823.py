#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>

#include <numeric>
#include <algorithm>

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>

#include <cmath>
#include <cstring>
#include <ctime>
#include <complex>

#include <cassert>


using namespace std;

typedef long long int64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef vector<double> VD;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

#define pi acos(-1.)
#define eps 1e-7

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

int main()
{
	freopen("C:\\input.in","r",stdin);
	freopen("C:\\output.out","w",stdout);

	int n;
	scanf("%d",&n);
	//printf("%d\n",n);

//	long junk;
//	scanf("%ld",&junk)

	///////////////////////////////////
	// DEFINE MAX CONSTANTS FOR PROBLEM
	///////////////////////////////////


	/////////////////
	// CASE VARIABLES
	/////////////////
	int p,k,l;
	vector<long> freq;
	vector<long>::iterator it_freq;
	long long keypresses;



	//////////////////
	// OTHER VARIABLES
	//////////////////
	long temp;
	int keypress_no;
	int keyno;
	

	FOR(input_case,0,n-1)
	{
		////////////////////////////////////////
		// INIT CASE VARIABLES FOR THIS NEW CASE
		////////////////////////////////////////
		keypresses = 0;
		freq.clear();


		///////////////////////
		// SCANF CASE VARIABLES
		///////////////////////
		scanf("%d %d %d",&p,&k,&l);
		//printf("%d %d %d\n",p,k,l);
		FOR(li,0,l-1)
		{
			scanf("%ld",&temp);
			//printf("%ld ",temp);
			freq.push_back(temp);
		}
		//printf("\n");


		/////////////////////////
		// PROBLEM SPECIFIC LOGIC
		/////////////////////////
		SORT(freq);
		REVERSE(freq);


		keypress_no = 1;
		keyno=1;
		for(it_freq = freq.begin(); it_freq != freq.end(); it_freq++)
		{
			keypresses = keypresses + (*it_freq) * keypress_no;
			keyno++;
			if(keyno>k)
			{
				keyno=1;
				keypress_no++;				
			}
		}
		


		/////////////////////
		// PRINTF CASE OUTPUT
		/////////////////////
		printf("Case #%d: %ld\n",input_case+1,keypresses);
		
	}
	
}
