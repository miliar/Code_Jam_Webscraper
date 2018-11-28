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
ll vys,nat,poct,let,pom,N,poc,num;
char c;
ll co[43],pc;

vector<ll> cis,bol;
vector<ll> cccc,zn;

void go(int h)
{
	if(h==poc-1)
	{
		ll num=cis[0],a=0;
		zn.clear();
		cccc.clear();
		zn.push_back(1);

		REP(i,pc)
		{
			if(co[i]==0)
			{
				a++;
				num*=10;
				num+=cis[a];
			}else if(co[i]==1)
			{
				cccc.push_back(num);
				a++;
				num=cis[a];
				zn.push_back(1);
			}else if(co[i]==2)
			{
				cccc.push_back(num);
				a++;
				num=cis[a];
				zn.push_back(-1);
			}
		}
		a++;
		for(;a<(int)cis.size();a++)
		{
			num*=10;
			num+=cis[a];
		}
			cccc.push_back(num);
			ll v=0;
			REP(i,(int)zn.size())
				v+=(zn[i]*cccc[i]);
			v=abs(v);
			if(v%2==0 || v%3==0 || v%5==0 || v%7==0 || v==0)
				vys++;
		return;
	}
	REP(i,3)
	{
		co[pc++]=i;
		go(h+1);
		pc--;
	}	
}

int main() 
{
	cin>>N;
	getchar();
	for(int i=1;i<=N;i++)
	{
		cis.clear();
		vys=0;
		pc=0;
		while((c=getchar())!='\n')
		{
			cis.push_back(c-'0');
		}
		poc=cis.size();
		go(0);
		cout<<"Case #"<<i<<": "<<vys<<endl;
	}
	return 0;
}
