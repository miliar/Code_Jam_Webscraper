//Author  :   MAK(Kader)
//Problem no:  
//Title:  Cse DU

//#pragma warning(disable:4786)
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
#define min(a,b) ((a)<(b)?(a):(b))

void reset(){}
void process(){}
int main()
{
	freopen("contest/A-large.in","rt",stdin);
	freopen("contest/out.txt","wt",stdout);
	int mod,rem,N,K,T,cas=1;
	cin>>T;
	while(T--){
		cin>>N>>K;
		mod=(1<<N);
		rem=K%mod;
		printf("Case #%d: ",cas++);
		if(rem==mod-1)
			puts("ON");
		else puts("OFF");
	}		
	return 0;
}
