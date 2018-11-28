#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <map>
#include <set>
#include <cassert>
#include <list>
#include <deque>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <queue>
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b)) 
#define SETF(x) memset(x,0xff,sizeof(x))
#define SET0(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB(x) push_back(x)
#define VI vector <int> 
#define VVI vector < vector <int> > 
#define VS vector <string>
 
using namespace std;

int x[100];
int y[100];
double r[100];
int N;
double dist(int n, int m)
{
	return sqrt((x[n]-x[m])*(x[n]-x[m])+(y[n]-y[m])*(y[n]-y[m]));
}
double solve(int N)
{
	if(N==1)
		return r[0];
	if(N==2)
		return max(r[1],r[0]);
	if(N==3)
	{
		double ret=1e13;
		double retr=1e13;;
		double d;
		d=dist(0,1);
		ret=max(r[2],(d+r[0]+r[1])/2.0);
		retr=min(ret,retr);
		d=dist(1,2);
		ret=max(r[0],(d+r[1]+r[2])/2.0);
		retr=min(ret,retr);
		d=dist(2,0);
		ret=max(r[1],(d+r[2]+r[0])/2.0);
		retr=min(ret,retr);
		return retr;
	}
}
int main()
{
	int _ncases;
	cin>>_ncases;
	for(int ncases=1;ncases<=_ncases;ncases++)
	{
		cin>>N;
		int i;
		for(i=0;i<N;i++)
			cin>>x[i]>>y[i]>>r[i];
		double ans=solve(N);
		cout<<"Case #"<<ncases<<": "<<ans<<endl;
	}
	return 0;
}
