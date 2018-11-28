#include <iostream>
#include <map>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define INF 1000000

map<string,int> mapa;
char str[3000];
int tab[3000];
int pom[3000],next[3000];
int n,m;

int main(){
	int d;
	fgets(str,sizeof(str),stdin);
	sscanf(str,"%d",&d);
	REP(test,d){
		mapa.clear();
		fgets(str,sizeof(str),stdin);
		sscanf(str,"%d",&n);
		REP(i,n){
			fgets(str,sizeof(str),stdin);
			mapa[string(str)]=i;
		}
		fgets(str,sizeof(str),stdin);
		sscanf(str,"%d",&m);
		REP(i,m){
			fgets(str,sizeof(str),stdin);
			tab[i] = mapa[string(str)];
		}
		REP(i,n)pom[i]=INF;
		for(int i=m-1;i>=0;i--){
			next[i] = pom[ tab[i] ];
			pom[ tab[i] ] = i;
		}
		int curr = 0;
		REP(i,n)if( pom[i] > pom[curr] )curr = i;

		int res = 0;
		REP(i,m){
			if( tab[i] == curr ){
				res++;
				REP(j,n)if( pom[j] > pom[curr] )curr = j;
				pom[ tab[i] ] = next[i];
			}else{
				pom[ tab[i] ] = next[i];
			}
		}
		printf("Case #%d: %d\n",test+1,res);
	}
	return 0;
}
