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

long long int velo[100],loc[100];

long long int N,K,B,T;
void reset(){}
void process(){

	
	long long int i;
	long long int s,v,res=0,inv=0;
	for(i=N-1;i>=0;i--){
	
		s=B-loc[i];
		v=velo[i];
		
		if(s<=v*T)		
		{
			
			K--;
			res+=inv;
			if(K==0) break;
		}
		else inv++;
	}
	if(K)
		cout<<"IMPOSSIBLE"<<endl;
	else
	cout<<res<<endl;

}
int main()
{
	freopen("code_jam/B-large.in","rt",stdin);
	freopen("code_jam/out.txt","wt",stdout);
	int test,i,cas=1;
	cin>>test;
	while(test--){
		cin>>N>>K>>B>>T;
		for(i=0;i<N;i++)
			cin>>loc[i];

		for(i=0;i<N;i++)
			cin>>velo[i];

		printf("Case #%d: ",cas++);
		process();
	
	}
		
	return 0;
}
