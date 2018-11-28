/*
Coder : Kushagra Gour
chinchang457@gmail.com
8 may 2010

complexity : --
*/
#include<iostream>
#include<fstream>
#include<stack>
#include<queue>
#include<vector>
#include<string>
#include<stdio.h>
#include<math.h>
#include<time.h>
using namespace std;

#define DEBUG 1
#define FOR(i,a,b) for(int i=(int)(a) ; i < (int)(b);++i)
#define REP(i,n) FOR(i,0,n)

#define MAX 1002

int arr[MAX];

int main(){
	FILE *f; 
	FILE *pf;
	f=fopen("C-small-attempt0.in","r+");
	pf=fopen("C-small.out","w+");
	
	int t; fscanf(f,"%d",&t);

	int r,k,n;
	REP(i,t){
		fscanf(f,"%d %d %d",&r,&k,&n); 
		REP(j,n) fscanf(f,"%d",&arr[j]);

		//REP(j,n) cout<<arr[j];

		int ans=0;
		int ind=0,ride;

		while(r){
			ride=0; int start=ind;
			while((ride+arr[ind])<=k){ 
				ride+=arr[ind]; ind++; ind%=n;
				if(ind==start) break;
			}
			ans+=ride; //cout<<ride<<" ";
			r--;
		}

		fprintf(pf,"Case #%d: %d\n",i+1,ans);		
		//cout<<ans<<endl;
	}
}