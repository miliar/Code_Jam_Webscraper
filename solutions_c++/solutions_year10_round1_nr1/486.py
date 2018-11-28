#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <complex>
#include <functional>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

#define dump(n) cout<<"# "<<#n<<"="<<(n)<<endl
#define debug(n) cout<<__FILE__<<","<<__LINE__<<": #"<<#n<<"="<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define rep(i,n) repi(i,0,n)
#define iter(c) __typeof((c).begin())
#define tr(c,i) for(iter(c) i=(c).begin();i!=(c).end();i++)
#define allof(c) (c).begin(),(c).end()
#define mp make_pair

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

void turn(vs& slots)
{
	int size=slots.size();
	vs temp(size);
	rep(i,size){
		for(int j=size-1;j>=0;j--)
			if(slots[i][j]!='.')
				temp[i]+=slots[i][j];
		while(temp[i].size()<size)
			temp[i]+='.';
		reverse(allof(temp[i]));
	}
	
	rep(i,size)
		rep(j,size)
			slots[i][j]=temp[size-1-j][i];
}

bool win(vs& slots,char color,int counts)
{
	int size=slots.size();
	rep(i,size)
		rep(j,size-counts+1){
			bool ok=true;
			rep(k,counts)
				if(slots[i][j+k]!=color){
					ok=false;
					break;
				}
			if(ok)
				return true;
		}
	rep(i,size)
		rep(j,size-counts+1){
			bool ok=true;
			rep(k,counts)
				if(slots[j+k][i]!=color){
					ok=false;
					break;
				}
			if(ok)
				return true;
		}
	rep(i,size-counts+1)
		rep(j,size-counts+1){
			bool ok=true;
			rep(k,counts)
				if(slots[i+k][j+k]!=color){
					ok=false;
					break;
				}
			if(ok)
				return true;
		}
	rep(i,size-counts+1)
		rep(j,size-counts+1){
			bool ok=true;
			rep(k,counts)
				if(slots[i+k][size-1-(j+k)]!=color){
					ok=false;
					break;
				}
			if(ok)
				return true;
		}
	return false;
}

const char* solve(int n,int k,vs& slots)
{
	turn(slots);
	bool red=win(slots,'R',k);
	bool blue=win(slots,'B',k);
	if(red&&blue)
		return "Both";
	if(!red && !blue)
		return "Neither";
	if(red)
		return "Red";
	if(blue)
		return "Blue";
	return ""; // dummy
}

int main()
{
	int t;
	cin>>t;
	rep(ti,t){
		int n,k;
		cin>>n>>k;
		vs slots(n);
		rep(i,n)
			cin>>slots[i];
		
		printf("Case #%d: %s\n",ti+1,solve(n,k,slots));
	}
	
	return 0;
}
