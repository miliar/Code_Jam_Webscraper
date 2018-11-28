#include <stdio.h>

int main(){
	int ncas;
	scanf("%d",&ncas);
	for(int t=1;t<=ncas;t++){
		long long euro = 0LL;
		long long r,k;
		int n;
		long long g[1000];
		int startidx = 0;
		int startidxs[1000];
		int nstartidxs = 0;
		long long cg[1000] = {0};
		int ssidx[1000];
		long long sumg = 0;

		for(int i=0;i<1000;i++){
			ssidx[i] = -1;
		}

		scanf("%lld %lld %d",&r,&k,&n);
		for(int i=0;i<n;i++){
			scanf("%lld",&g[i]);
		}

		//preprocess
		while(1){
			long long sum = 0;
			int j;
			for(int i=startidx;i<startidx+n;i++){
				j = i % n;
				if(sum + g[j] > k) break;
				sum += g[j];
			}
			ssidx[startidx] = nstartidxs;
			cg[nstartidxs] = sum;
			startidxs[nstartidxs++] = startidx;
			//next start person
			startidx = j;
			if(ssidx[startidx] != -1) break;
		}

		for(int i=0;i<ssidx[startidx]&&r>=0;i++){
			euro += cg[i];
			r--;
		}

		if(r>0){
			int len = 0;
			for(int i=ssidx[startidx];i<nstartidxs;i++){
				sumg += cg[i];
				len++;
			}
			euro += sumg*(r/len);
			for(int i=ssidx[startidx];i<r%len+ssidx[startidx];i++){
				euro += cg[i];
			}
		}

		printf("Case #%d: %lld\n",t,euro);
	}
	return 0;
}
