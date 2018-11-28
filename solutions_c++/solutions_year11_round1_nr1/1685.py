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

int N,PG,PD,T,cas=1;
void reset(){}
int gcd(int a,int b){

	if(b==0) return a;
	return gcd(b,a%b);

}

bool chk_all(int nu,int de){

	if(de>N) return false;

	if(nu+(100-de)<PG || nu>PG  )
		return false;
	return true;

}
void process(){

	
	bool ok=false;
	int nu,de,g;

	g=gcd(PD,100);
	nu=PD/g;
	de=100/g;


	//if(de>N)		fail=true;
	int i;
	i=1;
	//for( i=1;i<100&& !ok;i++)
	//if(de*i<=100){
	
		ok=chk_all(nu*i,de*i);
	//}
	
	if(ok==true)
		printf("Case #%d: Possible\n",cas++);
	else printf("Case #%d: Broken\n",cas++);

}
int main()
{
	freopen("Source/A-small-attempt3.in","rt",stdin);	
	freopen("Source/out.txt","wt",stdout);	
	
	cin>>T;
	while(T--){
	
		cin>>N>>PD>>PG;
		process();

	
	}		
	return 0;
}
