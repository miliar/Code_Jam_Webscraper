/* Author :: Kaushik */

//STL includes
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <deque>
#include <queue>
#include <set>
#include <stack>
#include <string>

//C includes
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <ctime>

//Other includes
#include <iomanip>
#include <iostream>
#include <sstream>
#include <fstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <tr1/random>
#include <tr1/unordered_map>

using namespace std;
using namespace std::tr1;

#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i) 
#define REP(i,n) 	FOR(i,0,n)
#define V(x) 		vector< x >
#define PB 			push_back
#define ALL(x) 		x.begin(),x.end()
#define SORT(x) 	sort(ALL(x))
#define fill(a,v) 	memset(a, v, sizeof(a))
#define PRINT(x)    cout << #x << " " << x << endl
#define S(N)		scanf("%d",&N)
#define gc 			getchar_unlocked
#define sqr(x)  	((x)*(x))
#define gcd  __gcd
#define mp make_pair

//Constants
const long double MPI = 3.14159265358979323846264338;
const long double E   = 2.71828182845904523536028747;
const int 		  INF = (int) 1e9;

typedef pair<int,int>   PI;
typedef pair<int,PI>    TRI;
typedef V( int )        VI;
typedef V( PI  )        VII;
typedef V( string )     VS;
typedef long long       ll;
typedef long double     ld;

ll nll(){ll a;cin>>a;return a;}
int ni(){int a;cin>>a;return a;}

int main()
{
	int kases;
	S(kases);
	for(int kase = 1;kase <= kases;kase++)
	{
		printf("Case #%d: ",kase);
		int n,l,h;
		n=ni(),l=ni(),h=ni();
		int A[n];
		REP(i,n)A[i]=ni();
		int tmp=0;
		for(int i=l;i<=h;i++)
		{
				int flag=0;
				for(int j=0;j<n;j++)
						if(A[j]%i!=0 && i%A[j]!=0){
								flag=1;
								break;
						}
				if(flag==0)
				{
						printf("%d\n",i);
						tmp=1;
						break;
				}
		}
		if(tmp==0)
				puts("NO");
	}
	return EXIT_SUCCESS;
}
