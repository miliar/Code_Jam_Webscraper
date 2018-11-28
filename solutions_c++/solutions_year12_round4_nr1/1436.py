#include<cstdio>
#include<vector>
#include<list>
#include<map>
#include<cmath>

using namespace std;

typedef long num;
#define SC "%ld"

typedef vector<num> vi;

typedef pair<num,num> Vertex;
typedef map<Vertex,list<Vertex> > Graph;
typedef map<Vertex,bool> vt;

#define FOR(T,it,L) for(T::iterator it = (L).begin(); it!=(L).end(); ++it)

void load(Graph & g,num & N,vt volt) {
	scanf(SC,&N);

	vi d(N+2);
	vi l(N+2);
	
	d[0] = 0;
	l[0] = 0;

	for(num i=1;i<=N;i++) {
		scanf(SC SC, &d[i], &l[i]);
	}

	scanf(SC,&d[N+1]);
	l[N+1]=0;

	for(num i=0;i<N+2;i++) {
		for(num j=0;j<N+2;j++) {
			Vertex v(i,j);
			//printf("Processing %ld,%ld\n",i,j);
			if(i<j) {
				//elore lendulok
				num hossz = std::min(d[j]-d[i],l[j]);
				//printf("Hossz=%ld\n",hossz);
				for(num k = i+1; k<N+2 && d[j]+hossz >= d[k] ; k++) {
					if(j!=k && d[j]-hossz <= d[k]) g[v].push_back(make_pair(j,k));
				}
			} else {
				//vissza lendulok
				num hossz = std::min(d[i]-d[j],l[j]);
				for(num k = i-1; k>=0 && d[j]-hossz <= d[k] ; k--) {
					if(j!=k && d[j]+hossz >= d[k]) g[v].push_back(make_pair(j,k));
				}
			}
			volt[v]=false;
		}
	}
}

/*
bool MK(Graph & g, VID s, VID t, Path & P, vector<bool> & volt) {
	if(s==t) return true;
	if(volt[s]) return false;
	volt[s] = true;
	FOR(it,g[s]) {
		Path::value_type p = make_pair(*it,s);
		if(marad(p)==0) continue;
		
		P.push_back(p);
		if(MK(g, other(p), t, P, volt)) return true;
		P.pop_back();
	}
	return false;
}
*/

bool MK(Graph & g, Vertex v, num N, vt & volt) {
	if(v.second==N+1) return true;
	if(volt[v]) return false;
	volt[v]=true;
	FOR(list<Vertex>,it,g[v]) {
		if(MK(g,*it,N,volt)) return true;
	}
	return false;
}

bool calc(Graph & g, vt & volt,num N) {
	return MK(g,make_pair(0,1),N,volt);
}

void print(num ti, bool ans) {
	printf("Case #%ld: %s\n",ti,ans ? "YES" : "NO");
}

void dump(Graph & g,vt & volt) {
	printf("DUMP\n");
	FOR(Graph,it,g) {
		printf("%ld %ld:\n",it->first.first,it->first.second);
		FOR(list<Vertex>,jt,it->second) {
			printf("\t%ld,%ld\n",jt->first,jt->second);
		}
	}
}


int main() {
	num T;
	scanf(SC,&T);
	for(num i=1;i<=T;i++) {
		Graph g;
		vt volt;
		num N;
		load(g,N,volt);
		//dump(g,volt);
		print(i,calc(g,volt,N));
	}
}
