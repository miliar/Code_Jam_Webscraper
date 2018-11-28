#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<cstring>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<sstream>
#include<utility>
#include<algorithm>
#include<bitset>
#include<stack>
#include<queue>

#define f(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define fiter(i,type,b) for((type)::iterator (i)=(b).begin();(i)!=(b).end();++(i))
#define pb push_back
#define mp make_pair
#define sz size()
#define x first
#define y second

using namespace std;

typedef pair<int,int> pii;
typedef long long lol;
typedef unsigned long long ull;
typedef pair<int,bool> pib;
typedef pair<long long, long long> pll;
typedef pair<double,double> pdd;

ifstream fin;
ofstream fout;
int d[10100],l[10100];

int abso(int q)
{
	return q<0?(-q):q;
}
int main()
{
	fin.open("A_small_attempt0.in");
	fout.open("A.out");
	int num_cases;
	fin>>num_cases;
	int n;
	int D;
	bool done;
	int dt,lt;
	map<int,int> vines,low;
	map<int,int>::iterator left,right;
	for(int caseno=1;caseno<=num_cases;++caseno)
	{
		vines.clear();
		fin>>n;
		f(i,0,n) 
		{	
			
			fin>>d[i]>>l[i];
			vines[d[i]]=(l[i]);
			low[d[i]]=0;
		}
		fin>>D;
		done=false;
		priority_queue<pii > dij;
		dij.push(mp(d[0],d[0]));
		cerr<<"C"<<caseno<<"\n";
		while(!dij.empty())
		{
			lt=dij.top().x;
			dt=dij.top().y;
			//cerr<<lt<<" "<<dt<<"\n";
			dij.pop();
			left=vines.lower_bound(dt-lt);
			right=vines.upper_bound(dt+lt);
			if(low[dt]>lt) continue;
			if(dt+lt>=D)
			{
				done=true;
				break;
			}
			for(map<int,int>::iterator it=left;it!=right;++it)
			{
				if(min((*it).y,abso(dt-(*it).x))>low[(*it).x])				{
					low[(*it).x]=min((*it).y,abso(dt-(*it).x));
					dij.push(mp(low[(*it).x],(*it).x));
				}
			}
		}
		if(done) fout<<"Case #"<<caseno<<": YES\n";
		else	fout<<"Case #"<<caseno<<": NO\n";	
	}
		

	fin.close();
	fout.close();
	return 0;
}
