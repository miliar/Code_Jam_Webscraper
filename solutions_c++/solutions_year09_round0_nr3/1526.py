#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list>
#include <cassert>
using namespace std; 

#define PB push_back 
#define MP make_pair 
#define SZ(v) ((int)(v).size()) 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) REP(i,SZ(v)) 
typedef long long ll; 

char pattern[20]="welcome to code jam";
char buff[502];

int nrcases;
int nrways[20];

int main() {
	gets(buff); sscanf(buff,"%d",&nrcases);
	FORE(casenr,1,nrcases) {
		gets(buff);
		memset(nrways,0,sizeof(nrways)); nrways[0]=1;
		for(int i=0;buff[i]!='\0';++i) {
			for(int j=18;j>=0;--j) {
				if(buff[i]==pattern[j]) nrways[j+1]=(nrways[j+1]+nrways[j])%10000;
			}
		}
		printf("Case #%d: %04d\n",casenr,nrways[19]);
	}
	return 0;
}
