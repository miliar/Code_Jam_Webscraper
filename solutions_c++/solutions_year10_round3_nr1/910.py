/*
Coder : Kushagra Gour
chinchang457@gmail.com
23 may 2010

complexity : --
*/
#include<iostream>
#include<fstream>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<string>
#include<stdio.h>
#include<math.h>
#include<time.h>
using namespace std;

#define DEBUG 1
#define FOR(i,a,b) for(int i=(int)(a) ; i < (int)(b);++i)
#define REP(i,n) FOR(i,0,n)

int arr[1002][2];

int main(){
	FILE *f; 
	FILE *pf;
	f=fopen("A-large.in","r+");
	pf=fopen("A-large.out","w+");
	
	int t; fscanf(f,"%d",&t);	
	int n;	
	
	REP(i,t){		
		fscanf(f,"%d",&n);
		REP(j,n){
			fscanf(f,"%d %d",&arr[j][0],&arr[j][1]);
		}

		int ans=0;

		REP(u,n)
			FOR(v,u+1,n){
				if(u!=v){
					int res = (arr[u][0]-arr[v][0])*(arr[u][1]-arr[v][1]);
					if(res<0) ans++;
				}
		}
		cout<<ans<<endl;

		fprintf(pf,"Case #%d: %d\n",i+1,ans);
	}
}