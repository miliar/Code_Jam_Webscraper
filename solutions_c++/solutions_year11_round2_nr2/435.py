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
#include <cassert>
#include <cstring>
#include <queue>
#define vvi vector<vector<int> > 
#define pii pair<int,int>
#define vpii vector<vector<pair<int,int> > > 
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;

double ven[300];
int P[300];
int V[300];
int C,D;
int Vnew[300];

int setis(double d){
	double left=P[0]-d;
	for(int i=0;i<C;i++)	Vnew[i]=V[i];
	Vnew[0]--;
	for(int i=0;i<C;i++){
		while(Vnew[i]--){
			double t=P[i]-d;
			if(fabs(left-t)<D || t<left){
				t=left+D;
				if(fabs(t-P[i])>d)	return 0;
			}
			left=t;
		}
	}
	return 100;
}

int main()
{
	int tc;
	scanf("%d",&tc);
	int caseno=1;
	while(tc--){
		scanf("%d%d",&C,&D);
		for(int i=0;i<C;i++){
			scanf("%d%d",&P[i],&V[i]);
		}
		double _min=0,_max=1e16;
		int cyc=100;
		while(cyc--){
			double _mid=(_max+_min)/2.0;
			if(setis(_mid))	_max=_mid;
			else					_min=_mid;
		}
		printf("Case #%d: %.9lf\n",caseno++,_max);
	}
	return 0;
}