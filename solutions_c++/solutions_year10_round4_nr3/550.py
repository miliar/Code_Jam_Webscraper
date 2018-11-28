#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <functional>
#include <utility>
#include <algorithm>
#include <numeric>
#include <typeinfo>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cstdarg>

using namespace std;

#define dump(n) cout<<"# "<<#n<<"="<<(n)<<endl
#define debug(n) cout<<__FILE__<<","<<__LINE__<<": #"<<#n<<"="<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define rep(i,n) repi(i,0,n)
#define iter(c) __typeof((c).begin())
#define foreach(i,c) for(iter(c) i=(c).begin();i!=(c).end();i++)
#define allof(c) (c).begin(),(c).end()
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

void aprintf(const char* format,...)
{
	static int counter;
	va_list args;
	va_start(args,format);
	printf("Case #%d: ",++counter);
	vprintf(format,args);
	va_end(args);
}

struct _aout:public ostream{
	template<typename T>
	ostream& operator<<(T a){
		static int counter;
		return cout<<"Case #"<<++counter<<": "<<a;
	}
	ostream& operator<<(ostream& (*pf)(ostream&)){
		return pf(*this);
	}
}aout;

int count_bacteria(const vvi& grid)
{
	int h=grid.size(),w=grid[0].size();
	int res=0;
	rep(i,h)
		rep(j,w)
			res+=grid[i][j];
	return res;
}

void update(vvi& grid)
{
	int h=grid.size(),w=grid[0].size();
	vvi newgrid(h,vi(w));
	repi(i,1,h)
		repi(j,1,w)
			if(grid[i][j]){
				if(grid[i-1][j] || grid[i][j-1])
					newgrid[i][j]=1;
			}
			else{
				if(grid[i-1][j] && grid[i][j-1])
					newgrid[i][j]=1;
			}
	grid=newgrid;
}

void show(const vvi& grid)
{
	puts("show");
	int h=grid.size(),w=grid[0].size();
	rep(i,h){
		rep(j,w)
			cout<<grid[i][j];
		cout<<endl;
	}
}

void solve()
{
	int n;
	cin>>n;
	vector<int> x1(n),y1(n),x2(n),y2(n);
	int w=0,h=0;
	rep(i,n){
		cin>>x1[i]>>y1[i]>>x2[i]>>y2[i];
		w=max(w,x2[i]);
		h=max(h,y2[i]);
	}
	//puts("input1");
	vvi grid(h,vi(w));
	rep(k,n)
		repi(i,y1[k]-1,y2[k])
			repi(j,x1[k]-1,x2[k])
				grid[i][j]=1;
	//puts("input2");
	for(int i=0;;i++){
		//show(grid);
		if(count_bacteria(grid)==0){
			aprintf("%d\n",i);
			break;
		}
		else
			update(grid);
	}
}

int main()
{
	int case_num;
	scanf("%d ",&case_num);
	rep(i,case_num)
		solve();
	return 0;
}
