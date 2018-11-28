#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int X,S,R,N;
double T;
int b[1009],e[1009],w[1009];

int main() {
	int tests;
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    scanf("%d",&tests);
    for (int test=1;test<=tests;test++) {
		scanf("%d %d %d %lf %d",&X,&S,&R,&T,&N);
		vector<pair<double,int> > ways;
		for (int i=0;i<N;i++) {
			scanf("%d %d %d",&b[i],&e[i],&w[i]);
			ways.push_back(make_pair(w[i],i));
			X-=e[i]-b[i];
		}
		b[N]=0; e[N]=X; w[N]=0;
		ways.push_back(make_pair(w[N],N));
		sort(ways.begin(),ways.end());
		double total=0;
		for (int i=0;i<ways.size();i++) {
			int id=ways[i].second;
			double len=e[id]-b[id];
			double t=len/(w[id]+R);
			t=min(1.0*T,t);
			total+=t;
			T-=t;
			double d=(w[id]+R)*t;
			total+=(len-d)/(w[id]+S);
		}
    	printf("Case #%d: %.9lf\n",test,total);
    }
    return 0;
}
