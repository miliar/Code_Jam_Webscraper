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

int anw2;
#define bad {printf("NO\n");return 0;}
//int dp[200][200];
int imp=-100000;
int dp[22][2000];
int bb[22][2000];
int pp[33];


int main()
{

	ifstream inf("input.txt");
	ofstream outf("output.txt");
	int test;
	
	inf >>test;




	
	FOR(ii,1,test){
			int m,n;
			int anw;
			inf>>m>>n;
			string ss[100];
			FOR(i,1,m) inf>>ss[i];
			//FOR(i,1,m) outf<<ss[i]<<endl;
			ss[0]="--------------------------------";
			FOR(i,0,m)FOR(j,1,n) bb[i][j]=ss[i][j-1]=='x';
			int po=1;
			int is1[20];
			int is2[20];

			pp[1]=1;
			FOR(i,2,13)pp[i]=pp[i-1]*2;
			FOR(i,1,n) po=po*2;
			
			FOR(i,0,m) FOR(j,0,po) dp[i][j]=imp;
			int i;
			i=0;FOR(j,0,po) dp[i][j]=0;
			FOR(le,1,m)FOR(j,0,po-1){
				dp[le][j]=imp;
				FOR(i,1,n) is1[i]=j&pp[i];
				FOR(i,1,n) if(is1[i]) is1[i]=1;
				int fl=0;
				FOR(i,1,n-1) if(is1[i] && is1[i+1]) fl=1;
				FOR(i,1,n) if(is1[i] && bb[le][i]) fl=1;
				if(fl){ dp[le][j]=imp;continue;}
				//pos возможеен
				int pl=0;
				FOR(i,1,n) if(is1[i]!=0) pl++;
				//выбор предка
				FOR(k,0,po-1){
						FOR(i,1,n) is2[i]=k&pp[i];
						FOR(i,1,n) if(is2[i]) is2[i]=1;

				
				int dd=dp[le-1][k];
				//checkvis
				int fla=0;
				FOR(i,1,n) if (is1[i]){
					if((i-1>=1)  && (is2[i-1])) fla=1;
					if((i+1<=n)  && (is2[i+1])) fla=1;
					
				}
				if (fla==0){
					int nee=dd+pl;
						if(dp[le][j]<nee)dp[le][j]=nee;
				}
				}
				

				//outf<<le<<endl;
				//FOR(i,1,n) outf<<is1[i];outf<<endl;
				//outf<<j<<" "<<dp[le][j] <<endl;
				
			}

			

			anw=imp;
			FOR(j,0,po-1) if(dp[m][j]>anw) anw=dp[m][j];
			if(anw==imp) anw=0;
			outf << "Case #"<<ii<<": "<<abs(anw)<<endl;
			//outf << "Case #"<<ii<<": "<<anw<<endl;
	
		//outf <<endl;
		//printf("Case #%d: \n",ii);

	}


	outf.close();  
   return 0;
}