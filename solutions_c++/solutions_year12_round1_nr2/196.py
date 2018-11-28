#include<cstdio>

int main() {
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		int N;
		int tab[2][1001];
		int completed[1001];
		int stars=0;
		scanf("%d",&N);
		for(int i=0;i<N;i++) {
			scanf("%d %d",&(tab[0][i]),&(tab[1][i]));
			completed[i]=0;
		}
		bool ok = true;
		int completes=0;
		while(ok) {
			ok = false;
			for(int i=0;i<N;i++)
				if(completed[i]<2 && tab[1][i]<=stars) {
					if(completed[i]==0)
						stars+=2;
					else
						stars+=1;
					completed[i]=2;
					ok = true;
					completes++;
				}
			
			if(!ok) {
				int goodLevel=-1;
				for(int i=0;i<N;i++)
					if(completed[i]==0 && tab[0][i]<=stars)
						if(goodLevel==-1 || tab[1][goodLevel]<tab[1][i])
							goodLevel=i;
				if(goodLevel!=-1) {
					ok = true;
					stars++;
					completed[goodLevel]=1;
					completes++;
				}
			}
		}
		if(stars!=2*N)
			printf("Case #%d: Too Bad\n",t,stars);
		else
			printf("Case #%d: %d\n",t,completes);
	}
	return 0;
}
