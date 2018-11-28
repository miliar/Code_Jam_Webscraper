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
int len;
	int k;
	string s;
	string s1;
int perm[1000];
int used[100];
int anw;
void check(){
	//FOR(i,1,k) cout<< perm[i];
	//cout<<endl;
	s1=s;
	FOR(i,0,len){
		int nn=i/k;
		int mm=i%k+1;
		int nee=nn*k+perm[mm]-1;
		s1[i]=s[nee];
	}
	int t=1;
	FOR(i,0,len-1) if(s1[i]!=s1[i+1]) t++;
	if(t<anw) anw=t;



	return ;
}
void gen(int fr){
	if(fr==k+1) check();
	FOR(i,1,k)if (!used[i]){
		used[i]=1;
		perm[fr]=i;
		gen(fr+1);
		used[i]=0;
	}
	return;
}

int main()
{

	ifstream inf("input.txt");
	ofstream outf("output.txt");
	int test;
	
	inf >>test;



	
	FOR(ii,1,test){

		inf>>k;
		inf>>s;
		len=s.length()-1;
		//s=" "+s;
		anw=100000000;

		FOR(i,1,k) used[i]=0;
		gen(1);

		
			outf << "Case #"<<ii<<": "<<anw<<endl;



		//outf <<endl;
		//printf("Case #%d: \n",ii);

	}


	outf.close();  
   return 0;
}