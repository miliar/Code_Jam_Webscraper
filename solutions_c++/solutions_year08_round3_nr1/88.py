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

int freq[20000];
int poz;
int t,p,k,l;

int main() {
	scanf("%d",&t);
	int id=1;
	while(t--) {
		scanf("%d%d%d",&p,&k,&l);
		for(int i=0;i<l;i++) scanf("%d",&freq[i]);
		sort(freq,&freq[l]);
		poz=k;
		int akt=1;
		long long wyn=0;
		for(int i=l-1;i>=0;i--) {
			if(poz) {
				wyn+=(long long)freq[i]*akt;
				poz--;
			}
			else {
				poz=k;
				akt++;
				wyn+=(long long)freq[i]*akt;
				poz--;
			}
		}
		printf("Case #%d: %I64d\n",id++,wyn);
	}



	return 0;
}
