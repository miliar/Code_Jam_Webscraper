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
#include<sstream>
#include<algorithm>
using namespace std;
//-------------------------------------------------------
typedef pair<int,int> ii;
typedef vector<int> vi;
#define pb push_back
#define sz(c) (int)(c).size()
#define INF  (1<<30)
#define EPS  1e-8
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define LL long long
#define FOR(_name,_A,_B)  for(int _name=_A;_name<=(_B);_name++)

void reset(){}
void process(){	}
int main()
{
	freopen("source/C-large.in","rt",stdin);	
	freopen("source/C.out","wt",stdout);	

	int T,N,res,a,mn,cas=1,sum;
	cin>>T;
	while(T--){
	
		cin>>N;
		res=0;
		sum=0;
		mn=INF;
		while(N--){
		
			cin>>a;
			res=res^a;
			
			mn=min(a,mn);
			sum+=a;
		
		}

		if(res){
		
			printf("Case #%d: NO\n",cas++);
		}
		else printf("Case #%d: %d\n",cas++,sum-mn);
	
	}		
	return 0;
}
