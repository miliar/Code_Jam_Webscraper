#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

typedef pair<int,int> pii;
#define pb(x)    push_back(x)
#define sz(x)    (x).size()
#define mp(x,y)  make_pair(x,y) 
#define all(x)   (x).begin(),(x).end()
#define inf 100000

pii timeTable(vector<pii> A, vector<pii> B){
	vector<int> freeA, freeB;
	int nA = 0, nB = 0;
	int i = 0, j = 0;
	
	if (sz(A)==0) return mp((int)0,(int)sz(B));
	if (sz(B)==0) return mp((int)sz(A),(int)0);
	
	sort(all(A));
	sort(all(B));
	freeA.pb(inf);
	freeB.pb(inf);	
	
	while (i<sz(A) && j<sz(B)){
		int t = min(A[i].first,B[j].first);
		if (t==A[i].first){
			if (freeA[0]<=t) {freeA[0] = inf; sort(all(freeA));} else nA++;
			freeB.pb(A[i].second); sort(all(freeB));
			i++;
		} else {
			if (freeB[0]<=t) {freeB[0] = inf; sort(all(freeB));} else nB++;
			freeA.pb(B[j].second); sort(all(freeA));
			j++;
		}
	}
	
	if (i==sz(A)){
		while(j<sz(B)){
			if (freeB[0]<=B[j].first) {freeB[0]=inf; sort(all(freeB));} else nB++;
			j++;
		}
	}
	
	if (j==sz(B)){
		while(i<sz(A)) {
			if (freeA[0]<=A[i].first) {freeA[0]=inf; sort(all(freeA));} else nA++;
			i++;
		}
	}
	
	return mp(nA,nB);
}

int main(){
	FILE *dat, *sol;
	dat = fopen("B-large.in","r");
	sol = fopen("B-large.out","w");
	
	int N,cnt=0;
	int NA, NB, T;
	
	fscanf(dat,"%d\n",&N);
	while(N-->0){
		vector<pii> A,B;
		fscanf(dat,"%d%d%d\n",&T,&NA,&NB);

		while(NA-->0){
			char s[100];
			fgets(s,40,dat);
			int xh,xm,yh,ym;
			sscanf(s,"%2d:%2d %2d:%2d",&xh,&xm,&yh,&ym);
			A.pb(mp(xh*60+xm, yh*60+ym+T));			
		}
		
		while(NB-->0){
			char s[100];
			fgets(s,40,dat);
			int xh,xm,yh,ym;
			sscanf(s,"%2d:%2d %2d:%2d",&xh,&xm,&yh,&ym);
			B.pb(mp(xh*60+xm, yh*60+ym+T));			
		}
		
		cnt++;
		pii res = timeTable(A,B);
		cout<<cnt<<endl;
		fprintf(sol, "Case #%d: %d %d\n", cnt, res.first, res.second);		
	}
	
	fclose(dat);
	fclose(sol);
}
