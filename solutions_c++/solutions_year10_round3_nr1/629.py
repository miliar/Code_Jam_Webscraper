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

int A[1002],B[1002];
int N;
void reset(){}
bool isInsec(int i,int j){

	int d1=A[i]-A[j],d2=B[i]-B[j];
	if(d1<0 && d2>0)
		return true;
	if(d1>0 && d2<0) return true;
	return false;

}
void process(){

	int i,j,res=0;
	for(i=0;i<N-1;i++)
		for(j=i+1;j<N;j++)
			if(isInsec(i,j))
				res++;
	cout<<res<<endl;

}
int main()
{
	freopen("code_jam/A-large.in","rt",stdin);
	freopen("code_jam/out.txt","wt",stdout);
	int T,i,cas=1;

	cin>>T;
	while(T--){
		cin>>N;

		for(i=0;i<N;i++)
			cin>>A[i]>>B[i];

		printf("Case #%d: ",cas++);
		process();
	
	}
		
	return 0;
}
