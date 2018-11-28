#include <stdio.h>
#include <map>
#include <iostream>
using namespace std;
#define INF 1000000000

int d[105];
map<string,int> pos;
char w[200];

int main(){
	int N;
	scanf("%d\n",&N);
	for(int t=1;t<=N;t++){
		pos.clear();
		int S;
		scanf("%d\n",&S);
		for(int i=0;i<S;i++){
			string s;
			fgets(w,200,stdin);
			for(int j=0;j<strlen(w);j++) s+=w[j];
			pos[s]=i;
			d[i]=0;
		}
		int Q;
		scanf("%d\n",&Q);
		for(int i=0;i<Q;i++){
			int m = INF;
			string s;
			for(int j=0;j<S;j++) if(d[j]<m) m = d[j];
			fgets(w,200,stdin);
			for(int j=0;j<strlen(w);j++) s+=w[j];
			int p = pos[s];
			d[p] = INF;
			for(int j=0;j<S;j++){
				if(j==p) continue;
				if(m+1<d[j]) d[j] = m+1;	
			}
		}
		int m = INF;
		for(int j=0;j<S;j++) if(d[j]<m) m = d[j];
		printf("Case #%d: %d\n",t,m);
	}
}
