#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ext/hash_map>
#include <ext/hash_set>
#define F(i,a,b) for(int i=(a);i<(b);++i)
#define Fe(it,v)for(__typeof__((v).begin()) it=(v).begin();it!=(v).end();++it)
#define all(x) (x).begin(),(x).end()
using namespace std;
using namespace __gnu_cxx;

int t[11000][3];
int n;
int g[11000];
int c[11000];
int v[11000];
#define oo 100000
int f(int x,int y){
	
	if(x>(n-1)/2){
		return v[x]==y?0:oo;
	}
	
	int &ret=t[x][y];
	if(ret!=-1)return ret;
	
	ret=oo;
	int temp;
	int andcost,orcost;
	if(y==1){
		andcost=f(2*x,1)+f(2*x+1,1);
		orcost=f(2*x,1)+f(2*x+1,1);
		int temporcost=min(f(2*x,0)+f(2*x+1,1),f(2*x,1)+f(2*x+1,0));
		orcost=min(orcost,temporcost);
	}
	else{
		andcost=f(2*x,0)+f(2*x+1,0);
		int tempandcost=min(f(2*x,0)+f(2*x+1,1),f(2*x,1)+f(2*x+1,0));
		andcost=min(andcost,tempandcost);
		orcost=f(2*x,0)+f(2*x+1,0);
	}
	if(g[x]==1&&c[x]==1){
		temp=min(andcost,orcost+1);
	}
	if(g[x]==1&&c[x]==0){
		temp=andcost;
	}
	if(g[x]==0&&c[x]==1){
		temp=min(andcost+1,orcost);
	}
	if(g[x]==0&&c[x]==0){
		temp=orcost;
	}
	ret=min(ret,temp);
	return ret;
	
	
}

int main(){
	int N;
	int test=1;
	cin>>N;
	while(N--){
		int V;
		cin>>n>>V;
		F(i,1,(n-1)/2+1){
			cin>>g[i]>>c[i];
			//cout<<"g"<<endl;
		}
		F(i,(n-1)/2+1,n+1){
			cin>>v[i];
			//cout<<"i"<<endl;
		}
		memset(t,-1,sizeof(t));
		int ret=f(1,V);
		//if(test==1)cout<<f(3,1)<<endl;
		cout<<"Case #"<<test++<<": ";
		if(ret>=oo)cout<<"IMPOSSIBLE";
		else cout<<ret;
		cout<<endl;
	}
}
