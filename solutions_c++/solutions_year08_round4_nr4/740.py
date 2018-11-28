#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <queue>
#define MP make_pair
#define PB push_back
#define FS first
#define SD second
#define VI vector<int>
#define PI pair<int,int>
using namespace std;

int n,k,m,t;
char tek[1010];
char tempa[1010];
vector<int> perma;

int main() {
	scanf("%d",&t);
	int id=1;
	while(t--) {
		scanf("%d %s",&k,tek);
		perma.clear();
		for(int i=0;i<k;i++) perma.PB(i+1);
		int best=1000000000;
		int dl=strlen(tek);
		do {
			int ile=dl/k;
			int dla=0;
			for(int ak=0;ak<ile;ak++) {
				int pol=ak*k;
				for(int i=0;i<k;i++) {
					tempa[pol+i]=tek[pol+perma[i]-1];
				}
			}
			
			//for(int i=0;i<k;i++) printf("%d,",perma[i]);printf("\n");
			//for(int i=0;i<dl;i++) printf("%c,",tempa[i]);printf("\n");
			
				
				char akt=tempa[0];
				dla++;
				for(int i=1;i<dl;i++) {
					while(akt==tempa[i]&&i<dl) {
						i++;
					}
					if(i<dl) {akt=tempa[i];dla++;}
				}
				//dla++;
			//printf("%d\n",dla); 
			best<?=dla;
		} while(next_permutation(perma.begin(),perma.end()));
		printf("Case #%d: %d\n",id++,best);
	}
	return 0;
}
