#define wru 0
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <cassert> 
#include <cmath> 
#include <vector> 
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std; 

typedef double LD;
typedef long long LL;
typedef  vector<int> VI;
typedef  vector<string> VS;
ifstream inf ;
ofstream outf ;

/*template  */

#define FOR(i,a,b) for( int i=(a),_b=(b); i<=(_b); i++) 
#define FORD(i,a,b) for( int i=(a),_b=(b); i>=(_b); i--) 
#define FORIT(i,a,type) for(type::iterator i=((a).begin()); i<((a).end()); i++) 
#define bend(x) x.begin(),x.end()
#define SORT(x) sort(bend(x))
#define pf(a) outf<< #a <<" = " <<a <<endl;
#define clr(t) memset((t),0,sizeof(t))
#define mnn 71234
#define imp 2000000102
#define pi 3.141592653589793
#define bad {printf("NO\n");return 0;}
map<string,int> ma;
map<int,string> ma2;
vector<int> next[100000];
int ek,pid;
int deg[10000];


int num[1100000];
int dd[1100000];
int k,n;
int nextt[60000];


int main()
{

	ifstream inf("input.txt");
	ofstream outf("output.txt");
	int test;
	
	inf >>test;



	
	FOR(ii,1,test){
		
		inf >>k>>n;
		 
		 FOR(i,1,n) inf>>dd[i];
		 FOR(i,1,k) num[i]=0;
		 FOR(i,1,k) nextt[i]=i+1;
		 nextt[k]=1;

		 int pos=1;int cnt=1;
		 FOR(cu,1,k){
			 while(1){
			 while(num[pos]!=0) pos=nextt[pos];
			 if(cnt==cu) {
				 num[pos]=cnt;
				 int pre=pos-1;if(pre==0)pre=k;
				 nextt[pre]=nextt[pos];
				 cnt=1;  break;}
			  cnt++;pos=nextt[pos];
			 }

		 }
		 //FOR(i,1,k) outf<< num[i]<<endl;
	    outf <<"Case #"<<ii <<":";
		FOR(i,1,n) outf <<" "<<num[dd[i]];
		outf <<endl;
		//printf("Case #%d: \n",ii);

	}


	outf.close();  
   return 0;
}