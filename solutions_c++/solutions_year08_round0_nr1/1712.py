#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int minChange(vector<string> g, vector<string> q){
	map<string,int> num;
	for(int i=0; i<g.size(); i++)
		num[g[i]] = i;
	
	vector<int> w;
	for(int i=0; i<q.size(); i++)
		w.push_back(num[q[i]]);
	
	int S = g.size();
	int N = w.size();
	int F[100][1001];
	int next[100];	
	int inf = N+10000;
	
	for(int s=0; s<S; s++) next[s]=inf;
	for(int s=0; s<S; s++) F[s][N] = 0;
	for(int k=N-1; k>=0; k--){
		next[w[k]] = k;
		for(int s=0; s<S; s++){
			if (next[s]==inf) {
				F[s][k] = 0;
				continue;
			}
			F[s][k] = inf;
			for(int z=0; z<S; z++) if(z!=s)
				F[s][k] = min(F[s][k],F[z][next[s]+1]);
			F[s][k] = F[s][k]+1;				
		}
	}
	
	int best = inf;
	for (int s=0; s<S; s++)
		best = min(best,F[s][0]);
		
	return best;
}



int main(){
	FILE *fin, *fout;
	fin = fopen("A-large.in","r");
	fout = fopen("A-large.out","w");
	
	int N,G,Q;
	int cnt = 0;
		
	fscanf(fin,"%d\n",&N);
	while(N-->0){
		vector<string> g, q;
		char s[1000];
		
		fscanf(fin,"%d\n",&G);
		cout<<G<<endl;
		while(G-->0){
			//fscanf(fin,"%s",s);
			fgets(s,105,fin);
			g.push_back(string(s));	
			cout << string(s) << endl;
		}
		fscanf(fin,"%d\n",&Q);
		while(Q-->0){
			//fscanf(fin,"%s",s);
			fgets(s,105,fin);
			q.push_back(string(s));	
		}
		
		cnt++;
		int res = minChange(g,q);
		fprintf(fout,"Case #%d: %d\n",cnt,res);
		
	}
	
	fclose(fin);
	fclose(fout);
	getchar();
}


