#include <stdio.h>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#define S(t,z) scanf("%"#t,&z)
#define P(t,z) printf("%"#t,z)
#define PLN(t,z) printf("%"#t"\n",z)
#define PS(t,z) printf("%"#t" ",z)

#define Z(t,n) memset(t,0,sizeof(t[0])*n)
#define MCP(d,s,n) memcpy(d,s,sizeof(s[0])*n)

#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)

#define LL long long

using namespace std;

int i,j,x,w,v,k,m,n;
int CS;
LL res;

int nf[2001];
int fv[2000][2001];
int fm[2000][2001];
int melt[2001];

int pe[2001];//jelsi 1 takiej osoby juz nie kontrolujemy

int main(){
   int T,N,M,C;
   int CT;
   S(d,C);
   CT=0;
   while (CT++,C--) {
     S(d,N);S(d,M);
     for (int i=0;i<M;i++) {
        S(d,nf[i]);
	for (int j=0;j<nf[i];j++) {
	    S(d,fv[i][j]);//jty smak i-tej osoby
	    S(d,fm[i][fv[i][j]]);//czy smak fv[i][j] jest melted
	}
	pe[i]=0;//kotrolujemy osobe i....
     }
     
     for (int i=1;i<=N;i++)
        melt[i] = 0;
	
    bool impossible(false);	
    bool success(false);
    while (!impossible && !success) {
        int i;
	bool exUns(false);
	for (i=0;i<M;i++) {
	    if (pe[i])
		continue;
	    bool sat(false);
	    int last1=-1;
	        
	    for (int j=0;j<nf[i];j++) {
	      if (melt[fv[i][j]] == fm[i][fv[i][j]]) {
	        sat = true;
	      }
	      if (fm[i][fv[i][j]]) 
	        last1=fv[i][j];
	    }
	    if (!sat) {
	        exUns = true;
		if (last1>0) {
		    melt[last1]=1;
		    pe[i]=1;//skoro dla niej robimy szejka mielonego, to juz nie ma sensu sprawdzac...
		} else
		    impossible = true;    
		break;    
	    }
	}
	success=!exUns;
    }
     cout <<"Case #"<<CT<<":";
     if (success) {
       for (int i=1;i<=N;i++)
         cout<<" "<<melt[i];
     } else {
        cout <<" IMPOSSIBLE";
     }
     cout << endl;	
   }
    return 0;
}

