#include <iostream>
#include <fstream>
#include <string>
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
#include <ctime>
#define REP(i,u) for(int i=0;i<u;i++)
#define FOR(i,z,u) for(int i=(z);i<=(u);i++)
#define FORO(i,z,u,p) for(int i=(z);i<=(u);i=i+(p))
#define PI 3.14159265358979323846
#define SQ(aa) ((aa)*(aa))
#define EPS 10e-20
#define eps EPS
using namespace std;

#define LLL 1000000
typedef long long ll;
ll vys,nat,poct,let,pom,N,poc,num,A[LLL],X,Y,Z,m,n;
vector<ll> lim;
int mem[LLL];

ll go(int k)
{
	ll poc=1;
	if(mem[k]!=-1) return mem[k];
	for(int i=k+1;i<(int)lim.size();i++)
		if(lim[i]>lim[k])
			poc+=(go(i)%1000000007LL);
	mem[k]=poc%1000000007LL;
	return poc%1000000007LL;
}

int main() 
{
	cin>>N;
	for(int j=1;j<=N;j++)
	{
		vys=0;
		cin>>n>>m>>X>>Y>>Z;
		REP(i,LLL)mem[i]=-1;
		REP(i,m)cin>>A[i];
		lim.clear();
		for(int i=0;i<n;i++)
		{
			lim.push_back(A[i%m]);
			A[i%m] = (X * A[i%m] + Y * (i + 1)) % Z;
		}
		for(int i=0;i<(int)lim.size();i++)
			vys+=go(i)%1000000007LL;
		cout<<"Case #"<<j<<": "<<vys%1000000007LL<<endl;
	}
	return 0;
}
