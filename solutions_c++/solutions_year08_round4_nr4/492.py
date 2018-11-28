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
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

#define MAXN 60000
int n,m,N,M,P,T,K;
char s[MAXN],ns[MAXN];
int pos[18];

int bruteforce()
{
			Repi(K) pos[i]=i;
			int ans=INF;
			do
			{
				int tmp=0;
				int let='-';
				Repi(M)
				 Repj(K)
				  ns[i*K+j]=s[i*K+pos[j]];
				Repi(N) if (ns[i]!=let) let=ns[i],tmp++;
				ans=MIN(ans,tmp);
			//	Repi(K)cout<<pos[i]; cout<<" -> "<<ns<<" ("<<tmp<<")"<<endl; 
			}while(next_permutation(pos,pos+K));
			return ans;
}

int main()
{
 scanf("%d",&T);   
 for (int id=1;id<=T;id++)
  {
		scanf("%d\n%s\n",&K,s);
	///	cout<<K<<" "<<s<<endl;
		N=strlen(s); M=N/K;
		printf("Case #%d: %d\n",id,bruteforce());
  }
    return 0;
}
