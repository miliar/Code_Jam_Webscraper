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
#define pi 3.141592653589793
#define bad {printf("NO\n");return 0;}
map<string,int> ma;
map<int,string> ma2;


int isand[50000];
int isch[50000];
int x[50000];
int dp0[50000];
int dp1[50000];
int m;
int imp;

int find(int i,int va){
	if(x[i]!=-1) {
		if(x[i]==va) return 0;
		else return imp;
	}
	if(va==1) if(dp1[i]!=-1) return dp1[i];
	if(va==0) if(dp0[i]!=-1) return dp0[i];
	//make and
	int pp;
	if (isand[i]) pp=0 ;
	else {
		if (isch[i]) pp=1;
		else pp=imp;
	}
	int x1,x2;
	if (va==1){
		x1=find(i*2,1);
		x2=find(i*2+1,1);
		dp1[i]=x1+x2+pp;
		if(dp1[i]>imp) dp1[i]=imp;

	}
	else{
		//va=0;
		x1=find(i*2,0);
		x2=find(i*2+1,0);
		dp0[i]=min(x1,x2)+pp;
		if(dp0[i]>imp) dp0[i]=imp;

	}
	//now make or
	if (!isand[i]) pp=0 ;
	else {
		if (isch[i]) pp=1;
		else pp=imp;
	}
	if (va==1){
		x1=find(i*2,1);
		x2=find(i*2+1,1);
		int nee=min(x1,x2)+pp;
		if(dp1[i]>nee) dp1[i]=nee		;
		if(dp1[i]>imp) dp1[i]=imp;

	}
	else{
		//va=0;
		x1=find(i*2,0);
		x2=find(i*2+1,0);
		int nee=x1+x2+pp;
		if(dp0[i]>nee) dp0[i]=nee;
		if(dp0[i]>imp) dp0[i]=imp;
	}
	if(va==1) return dp1[i];
	else return dp0[i];





	
	
	

}
int main()
{

	ifstream inf("input.txt");
	ofstream outf("output.txt");
	int test;
	
	inf >>test;



	
	FOR(ii,1,test){
		int v;
		imp=2000000;
		inf >>m>>v;
		clr(x);

		FOR(i,1,(m-1)/2) inf >> isand[i]>>isch[i];
		FOR(i,1,(m-1)/2) x[i]=-1;
		FOR(i,(m-1)/2+1 ,m)inf >> x[i];
		FOR(i,1,m) dp1[i]=-1;
		FOR(i,1,m) dp0[i]=-1;
		int anw=find(1,v);
		if(anw<imp)
			outf << "Case #"<<ii<<": "<<anw<<endl;
		else
			outf << "Case #"<<ii<<": "<<"IMPOSSIBLE"<<endl;



		//outf <<endl;
		//printf("Case #%d: \n",ii);

	}


	outf.close();  
   return 0;
}