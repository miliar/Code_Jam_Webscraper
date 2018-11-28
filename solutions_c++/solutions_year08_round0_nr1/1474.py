#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

#define INF 1000000

char se[105][105];
char in[105];

int w[2][1005];
int akt;
int minimal[2];
int k;

int n;
int s,q;

int main(){
	scanf("%d\n",&n);
	for(int dd=1;dd<=n;dd++){
		scanf("%d\n",&s);
		for(int i=0;i<s;i++){
			fgets(se[i],105,stdin);
		}
		scanf("%d\n",&q);
		akt=0;
		for(int i=0;i<s;i++){
			w[0][i]=0;
		}
		minimal[akt]=0;
		for(int i=0;i<q;i++){
			akt^=1;
			minimal[akt]=INF;
			fgets(in,105,stdin);
			for(int j=0;j<s;j++){
				if(strcmp(in,se[j])==0) {k=j; w[akt][j]=INF; continue;}
				w[akt][j]=min(minimal[akt^1]+1,w[akt^1][j]);
				minimal[akt]=min(minimal[akt],w[akt][j]);
			}
		}
		printf("Case #%d: %d\n",dd,minimal[akt]);
	}
	return 0;
}

