#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXT (24*60+10)

int nTC, nA, nB, T, aa[MAXT], ab[MAXT];
vector<int> sa[MAXT], sb[MAXT];
char s[100000];

int t(){
	int hh, mm;
	scanf("%d:%d",&hh,&mm);
	return hh*60 + mm;
}

bool can(int startA, int startB){
	memset(aa,0,sizeof(aa));
	memset(ab,0,sizeof(ab));
	aa[0] = startA; ab[0] = startB;
	for (int i=0; i<MAXT; i++){
		if (i>0) aa[i] += aa[i-1], ab[i] += ab[i-1];
		for (int j=0; j<sa[i].size(); j++){
			if (aa[i]>0) aa[i]--; else return false;
			if (sa[i][j]+T < MAXT) ab[ sa[i][j]+T ]++;
		}
		for (int j=0; j<sb[i].size(); j++){
			if (ab[i]>0) ab[i]--; else return false;
			if (sb[i][j]+T < MAXT) aa[ sb[i][j]+T ]++;
		}
	}
	return true;
}

int main(){
	scanf("%d",&nTC);
	for (int TC=1; TC<=nTC; TC++){
		scanf("%d %d %d",&T,&nA,&nB);
		for (int i=0; i<MAXT; i++)
			sa[i].clear(), sb[i].clear();
		for (int i=0; i<nA; i++){
			int dep = t(), arr = t();
			sa[dep].push_back(arr);
		}
		for (int i=0; i<nB; i++){
			int dep = t(), arr = t();
			sb[dep].push_back(arr);
		}
		
		int needA = nA, needB = nB;
		for (int i=0; i<=nA; i++)
			for (int j=0; j<=nB; j++)
				if (i+j<needA+needB && can(i,j))
					needA = i, needB = j;

		printf("Case #%d: %d %d\n",TC,needA,needB);
	}
}
