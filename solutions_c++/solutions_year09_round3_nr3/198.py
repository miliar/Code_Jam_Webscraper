
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cctype>
#include<iostream>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
//-------------------------------------------------------
typedef pair<int,int> ii;
typedef vector<int> vi;
#define pb push_back
#define sz(c) (c).size()
#define all(c) (c).begin(),(c).end()
#define vtr(c,i) for(vi::iterator i=c.begin();i!=c.end();i++)
#define INF  (1<<30)
#define EPS  1e-8
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))
#define max(a,b) ((a)>(b)?(a):(b))

//--------------------------------------------------------

int real[1000],P,Q;
map<int,int> memo[100003];
void reset(){

	for(int i=0;i<=10000+1;i++)
		memo[i].clear();

}

int fun(int i,int j){

	if(memo[i].find(j)!=memo[i].end())
			return memo[i][j];

	int k,m=INF;
	for(k=0;k<Q;k++)
		if(real[k]<=j&& real[k]>=i)
			m=min(m,  fun(i,real[k]-1)+fun(real[k]+1,j)  );
	
	if(m==INF)		return memo[i][j]=0;
	return memo[i][j]=m+j-i;
}
void process(){

	reset();
	int i,g;
	for(int i=P-100;i>=1;i-=100)
		g=fun(i,P);
	cout<<fun(1,P)<<endl;
}
int main()
{
	freopen("contest/C-large.in","rt",stdin);
	freopen("contest/out.txt","w",stdout);
		int t,i,cas=1;
		cin>>t;
		while(t--){
		
			cin>>P>>Q;
			for( i=0;i<Q;i++)
				cin>>real[i];
			printf("Case #%d: ",cas++);
			process();
		}
	return 0;
}
