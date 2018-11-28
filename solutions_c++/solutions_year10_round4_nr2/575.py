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

int buy(int begin,int end,int round,vi& teams,vvi& match)
{
	if(round==0)
		return 0;
		//return teams[begin]*match[round-1][begin/2];
	
	int center=(begin+end)/2;
	if(*max_element(teams.begin()+begin,teams.begin()+end)==round){
		//printf("#res_havetobuy %d %d (%d)\n",begin,end,match[round-1][begin/(1<<round)]);
		int res=match[round-1][begin/(1<<round)];
		vi prev(end-begin);
		rep(i,end-begin)
			prev[i]=teams[begin+i];
		repi(i,begin,end)
			teams[i]=max(teams[i]-1,0);
		//res+=buy(begin,center,round-1,teams,match)+buy(center,end,round-1,teams,match);
		int res_left=buy(begin,center,round-1,teams,match);
		//dump(res_left);
		int res_right=buy(center,end,round-1,teams,match);
		//dump(res_right);
		res+=res_left+res_right;
		repi(i,begin,end)
			teams[i]=prev[i-begin];
		
		//printf("%d %d (round %d): %d\n",begin,end,round,res);
		return res;
	}
	else{
		//printf("#res_buy %d %d (%d)\n",begin,end,match[round-1][begin/(1<<round)]);
		int res_buy=match[round-1][begin/(1<<round)];
		vi prev(end-begin);
		rep(i,end-begin)
			prev[i]=teams[begin+i];
		repi(i,begin,end)
			teams[i]=max(teams[i]-1,0);
		res_buy+=buy(begin,center,round-1,teams,match)+buy(center,end,round-1,teams,match);
		repi(i,begin,end)
			teams[i]=prev[i-begin];
		
		//printf("#res_nobuy %d %d\n",begin,end);
		int res_nobuy=buy(begin,center,round-1,teams,match)+buy(center,end,round-1,teams,match);
		
		int res=min(res_buy,res_nobuy);
		//printf("%d %d (round %d): %d %d (min:%d)\n",begin,end,round,res_buy,res_nobuy,res);
		return res;
	}
	//if(end-begin==1)
	//	return teams[begin];
	//
	//int res=0;
	//if(*max_element(teams.begin()+begin,teams.begin()+end)){
	//	res++;
	//	repi(i,begin,end)
	//		teams[i]=max(teams[i]-1,0);
	//}
	////printf("%d %d: %d\n",begin,end,res);
	//int center=(begin+end)/2;
	//return res+buy(begin,center,teams)+buy(center,end,teams);
}

void solve()
{
	int p;
	cin>>p;
	vi teams(1<<p);
	rep(i,teams.size()){
		cin>>teams[i];
		teams[i]=p-teams[i];
	}
	vvi match(p);
	rep(i,match.size()){
		match[i].resize(1<<(p-1-i));
		rep(j,match[i].size())
			cin>>match[i][j];
	}
	int res=buy(0,teams.size(),p,teams,match);
	aprintf("%d\n",res);
	//rep(i,match.size()){
	//	rep(j,match[i].size())
	//		cout<<match[i][j]<<" ";
	//	cout<<endl;
	//}
}

int main()
{
	int case_num;
	scanf("%d ",&case_num);
	rep(i,case_num)
		solve();
	return 0;
}
