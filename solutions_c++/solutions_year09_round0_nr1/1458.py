#include <cstdio>
#include <algorithm>
using namespace std;


int n,l,d,x,pos;
char words[5005][17];
char chain[1000];
int queue[5006],qs;
bool alfa[300];
void wypisz() {
printf("Q: ");
for(int i=0; i<qs; ++i) printf("%d ", queue[i]);
printf("\n");
}

int main() {
	scanf("%d%d%d", &l,&d, &n);
	for(int i=0; i<d; ++i) scanf("%s", words[i]);
	for(int k=1; k<=n; ++k) {
		scanf("%s", chain);
		qs=0;
		for(int i=0; i<d; ++i) queue[qs++]=i;
		x=strlen(chain);
		pos=0;
		for(int i=0; i<x && qs>0; ) {
			//pojedynczy znak ciagu
            for(int j='a'; j<='z'; ++j) alfa[j]=0;
			if(chain[i]=='(') {
					++i;
					while(chain[i]!=')' ) {
						alfa[chain[i]]=1; ++i;
					}
			}
			else alfa[chain[i]]=1;
			for(int j=0; j<qs; ) {
				if(!alfa[words[queue[j]][pos]]) {  if(qs==0) break; queue[j]=queue[qs-1]; qs--; }
				else ++j;
			}
			++pos;
			++i;
		}
		printf("Case #%d: %d\n", k, qs);
	}



}
