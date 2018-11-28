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

#define LL long long 

#define F(i,a,b) for(long long i=(a);i<(b);++i)
#define Fe(it,v)for(__typeof__((v).begin()) it=(v).begin();it!=(v).end();++it)
#define all(x) (x).begin(),(x).end()
using namespace std;
using namespace __gnu_cxx;

int t[110][110];

bool rock[110][110];

int H,W,R;

int f(int x,int y){
	
	if(x==1&&y==1)return 1;
	
	int &ret=t[x][y];
	
	if(ret!=-1)return ret;
	
	ret=0;
	
	int dx[8]={-1,-1,1,1,-2,-2,2,2},dy[8]={-2,2,-2,2,-1,1,-1,1};
	
	F(i,0,8){
		int x2=x+dx[i],y2=y+dy[i];
		if(x2>=1&&x2<=H&&y2>=1&&y2<=W&&x2<x&&y2<y&&!rock[x2][y2]){
			ret+=f(x2,y2);
		}
	}
	ret%=10007;
	
	return ret;	
	
}


int main(){
	int N,test=1;
	cin>>N;
	while(N--){
		cin>>H>>W>>R;
		memset(t,-1,sizeof(t));
		memset(rock,0,sizeof(rock));
		F(i,0,R){
			int r,c;
			cin>>r>>c;
			rock[r][c]=1;
		}
		cout<<"Case #"<<test++<<": "<<f(H,W)<<endl;
	}
}
