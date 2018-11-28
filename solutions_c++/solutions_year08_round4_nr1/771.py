#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#define MP make_pair
#define PB push_back
#define FS first
#define SD second
#define VI vector<int>
#define PI pair<int,int>
#define INF 10000000

using namespace std;

int bramki[20100];
int dane[20100];
int change[20100];
int n,v,m;
int minimum[2][20100];
int ilewew;

void czysc() {
	for(int i=0;i<20100;i++) {
		dane[i]=bramki[i]=minimum[0][i]=minimum[1][i]=-1;
		change[i]=-1;
	}
}

int minim(int v, int war) {
	int anda, ora,wynik;
	if(minimum[war][v]==-1) {
		//printf("wchodze v%d war%d \n",v,war);
		if(v<=ilewew) {
			if(war==0) {
				//printf("wew\n");
				anda=min(minim(v*2,0),minim(v*2+1,0));
				ora=minim(v*2,0)+minim(v*2+1,0);
			}
			else {
				//printf("wew2\n");
				ora=min(minim(v*2,1),minim(v*2+1,1));
				anda=minim(v*2,1)+minim(v*2+1,1);
			
			}
			if(bramki[v]==1) ora++;
			else anda++;
			//printf("{%d %d}",v,change[v]);
			if(change[v]==0) {
				if(bramki[v]==1) ora=INF;
				else anda=INF;
			}
			wynik=min(anda,ora);
			if(wynik>=INF) wynik=INF;
		}
		else {
			//printf("dane%d=   ",dane[v]);
			if(dane[v]==war) wynik=0;
			else wynik=INF;
		}
		//printf("wyn=%d}\n",wynik);
		minimum[war][v]=wynik;
	}
	return minimum[war][v];
	
}

int main() {
	scanf("%d",&n);
	int id=1;
	while(n--) {
		czysc();
		scanf("%d %d",&m,&v);
		for(int i=1;i<=(m-1)/2;i++) {scanf("%d",&bramki[i]);scanf("%d",&change[i]);}
		ilewew=(m-1)/2;
		//printf("%d m",m);
		for(int i=1;i<=(m+1)/2;i++) {scanf("%d",&dane[i+(m-1)/2]);}
		int wyn;
		wyn=minim(1,v);
		printf("Case #%d: ",id++);
		if(wyn>=INF) printf("IMPOSSIBLE");
		else printf("%d",wyn);
		printf("\n");
	}
	return 0;
}
