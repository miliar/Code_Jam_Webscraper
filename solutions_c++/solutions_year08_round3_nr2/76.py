#include <stdio.h>
#include <vector>
#include <deque>
#include <algorithm>
#include <map>
#include <string>
//#include "bnum.h"
using namespace std;
#define MP make_pair
#define FS first
#define SD second
#define PI pair<int,int>
#define VI vector<int>
#define INF 1000000000

char strin[100];
char tworz[100];
int n;

int tworza() {
	if(n<2) return 0;
	tworz[n-2]++;
	int ns=n-2;
	while(tworz[ns]>2&&ns>0) {
		tworz[ns]=0;
		tworz[--ns]++;
	}
	//for(int i=0;i<n;i++) {printf("%d ",tworz[i]);}
	//printf("\n");
	return tworz[0]!=3;
}

long long liczby[100];
int licza;

void wart() {
	licza=0;
	int od=0;
	while(od<n) {
		long long t=strin[od];
		while(tworz[od]==0&&od<n-1) {
			t=t*10+strin[++od];
		}
		liczby[licza++]=t;
		od++;
	}
}

long long zlicz() {
	long long ile=0;
	for(int i=0;i<n;i++) tworz[i]=0;
	while(1) {
		wart();
		long long wyn=0;
		int znak=0;
		for(int i=0;i<licza;i++) {
			while(tworz[znak]==0) {znak++;}
			if(tworz[znak]==1) wyn+=liczby[i];
			else wyn-=liczby[i];
			znak++;
		}
		for(int i=0;i<licza;i++) {
			//printf("%d ",liczby[i]);
		} //printf("\n");
		if(wyn<0) wyn*=-1;
		//printf("[%I64d]\n",wyn);
		if(wyn%2==0||wyn%3==0||wyn%5==0||wyn%7==0) {
			ile++;
		}
		if(!tworza())break;
	}
	return ile;
}

int t;
int main() {
	scanf("%d",&t);
	int id=1;
	while(t--) {
		scanf("%s",strin);
		n=strlen(strin);
		for(int i=0;i<n;i++) strin[i]-='0';
		long long wyn=zlicz();
		printf("Case #%d: %I64d\n",id++,wyn);
	}
	return 0;
}