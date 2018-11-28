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


long long prime[1100000];
long long p[1100000];
long long r[1100000];
long long  findset(long long i){
	if (p[i]!=i){
		i=findset(p[i]);
	}
	return p[i];
}
void   un (long long a, long long b)
{
	a=findset(a);b=findset(b);
  if (r[a] < r[b])  p[a]=b;
  else{
	  p[b]=a;
	  if(r[a]==r[b]) r[a]++;
  }
}
    


int main()
{

	ifstream inf("input.txt");
	ofstream outf("output.txt");
	int test,t,na,nb,n;
	inf >>test;
	
	prime[1]=2;prime[2]=3;
	long long i=5;int pk=2;
	long long mx=1010100;
	while (i<= mx) {
     int j;
   for(j=1;j<=pk;j++)
   if ((i % prime[j]==0)||(prime[j]*prime[j]>i)) break;
   if  (prime[j]*prime[j]>i) {pk++;prime[pk]=i;
   //outf<<i<<endl;
   }
   i++;
	}



	
	FOR(ii,1,test){
		long long n,a, b, p1;
		inf >>a>>b>>p1;
		n=b-a+1;
		FOR(i,1,n) p[i]=i;
		FOR(i,1,n) r[i]=0;
		long long pri;
		FOR(i,1,pk){
			long long pr=prime[i];
			if(pr<p1) continue;
			if(pr>n+1) break;
			long long le=a-a%pr -pr;
			long long ri;
			while(le<a)le+=pr;
			//l-est
			ri=le+pr;
			while (ri<=b){
				long long x=le-a+1;
				long long y=ri-a+1;
				un(x,y);

				ri+=pr;
			}

		}
		

         int anw=0;
		 FOR(i,1,n) if(p[i]==i) anw++;
	outf <<"Case #"<<ii <<": "<< anw<<endl;
		//printf("Case #%d: \n",ii);

	}


	outf.close();  
   return 0;
}