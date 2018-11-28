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



int main()
{ 
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test,t,na,nb,n;
	scanf("%d",&test);
	char cc[211];
	int t1[211],t2[211],used[211],froma[211];
	map <string , int> mm;
	FOR(ii,1,test){
		scanf("%d%d%d",&t,&na,&nb);;
		gets(cc);
		n=na+nb;
		FOR(i,1,na+nb){
		gets(cc);
		t1[i]=((cc[0]-'0')*10+(cc[1]-'0'))*60+((cc[3]-'0')*10+(cc[4]-'0'));
		t2[i]=((cc[0+6]-'0')*10+(cc[1+6]-'0'))*60+((cc[3+6]-'0')*10+(cc[4+6]-'0'));
		used[i]=0;
		froma[i]=i<=na;
		}
		int anwa=0;
		int anwb=0;
		while(1){
			int time1=100000000;
			int time2=100000000;
			int ii=-1;
			FOR(i,1,n) if (!used[i] && (t1[i]<time1 ||(t1[i]==time1)&&t2[i]<time2  )   ) {
				time1=t1[i];time2=t2[i];ii=i;
			}
			if(ii==-1) break;
			if(froma[ii]) anwa++;else anwb++;
			int dir=froma[ii];
			used[ii]=1;
			while (1){
				int time1=100000000;
				int time2=100000000;
				int jj=-1;
				FOR(i,1,n) if(froma[i]!=dir && t1[i]>=t2[ii]+t  ) if (!used[i] && (t1[i]<time1 ||(t1[i]==time1)&&t2[i]<time2  )   ){
					time1=t1[i];time2=t2[i];jj=i;
				}
				if(jj==-1) break;
				used[jj]=1;
				ii=jj;
				dir=froma[ii];

				
			}



		
		}




		printf("Case #%d: %d %d\n",ii,anwa,anwb);

	}


   
   return 0;
}