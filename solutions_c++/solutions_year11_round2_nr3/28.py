#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

int N, M;
int U[2000], V[2000];

pair<int, int> edges[6000];
int next[6000], rev[6000];

void eval(){
	scanf("%d %d", &N, &M);
	for(int i=0; i<M; i++){
		scanf("%d", U+i);
	}
	for(int i=0; i<M; i++){
		scanf("%d", V+i);
	}
	int e=0;
	for(int i=0; i<N; i++)
		edges[e++]=make_pair(i, (i+1)%N);
	for(int i=0; i<M; i++){
		edges[e++]=make_pair(U[i]-1, V[i]-1);
		edges[e++]=make_pair(V[i]-1, U[i]-1);
	}
	sort(edges, edges+e);
	for(int i=0; i<e; i++)
		rev[i]=-1;
	for(int i=0; i<e; i++){
		next[i]=-1;
		for(int j=0; j<e; j++){
			if(edges[j].first!=edges[i].second)
				continue;
			if(edges[j].second==edges[i].first){
				rev[i]=j;
				continue;
			}
			if(j==i)
				continue;
			if(next[i]==-1)
				next[i]=j;
			else if(((edges[i].first-edges[j].second+N)%N)<((edges[i].first-edges[next[i]].second+N)%N))
				next[i]=j;
		}
	}
	int mark[6000]={0};
	int C=N;
	for(int i=0; i<e; i++)
		if(!mark[i]){
			int cnt=0;
			int j=i;
			do{
				mark[j]=1;
				cnt++;
				j=next[j];
			}while(j!=i);
			C=min(cnt, C);
		}
	printf("%d\n", C);
	queue<int> q;
	int color[2000]={0};
	color[edges[0].first]=0;
	color[edges[0].second]=1;
	q.push(0);
	for(; !q.empty(); q.pop()){
		int i=q.front();
		if(i==-1)
			continue;
		int used1=color[edges[i].first];
		int used2=color[edges[i].second];
		int cur=0;
		q.push(rev[next[i]]);
		int last;
		for(int j=next[next[i]]; j!=i; j=next[j]){
			q.push(rev[j]);
			while(cur==used1 || cur==used2)
				cur++;
			if(cur<C){
				last=color[edges[j].first]=cur;
				cur++;
			}else{
				int next=0;
				while(next==last || next==used1)
					next++;
				last=color[edges[j].first]=next;
			}
		}
	}
	for(int i=0; i<N; i++)
		printf("%d ", color[i]+1);
	putchar('\n');
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
