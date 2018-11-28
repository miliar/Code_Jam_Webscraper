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


typedef long long ll;
ll vys,nat,poct,let,pom,N;

int main() 
{
	cin>>N;
	for(int i=1;i<=N;i++)
	{
		cin>>nat>>poct>>let;
		vys=0;
		vector<ll> f(let);
		REP(k,let)
		  cin>>f[k];
if(f.size()>poct*nat)
{
	cout<<"Case #"<<i<<": "<<"Impossible"<<endl;
	continue;
}
		sort(f.begin(),f.end());
		reverse(f.begin(),f.end());
		int k,o;
		for(k=0,o=1;k<(int)f.size();k+=poct,o++)
		{
			for(int u=k;u<k+poct && u<(int)f.size();u++)
			{
				vys+=f[u]*o;
			}
		}
		cout<<"Case #"<<i<<": "<<vys<<endl;
	}
	return 0;
}
