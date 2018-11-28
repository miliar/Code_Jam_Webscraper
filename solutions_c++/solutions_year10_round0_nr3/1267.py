#include<cstdio>
#include<cstdlib>
#include<cstring>
typedef long long LL;

int a[9999];
int ne[9999];
LL ts[9999];

int main(){
	int nnn;
	scanf("%d", &nnn);
	for(int nn=1;nn<=nnn;nn++){
		int r, n, k;
		long long x=1;
		scanf("%d%d%d", &r, &k, &n);
		for(int i=0;i<n;i++)scanf("%d", &a[i]);
		memset(ne,-1,sizeof(ne));
		memset(ts,0,sizeof(ts));
		int cp=0;
		LL sum=0;
		LL csum=0;
		int cy=-1;
		while(r>0){
			LL s=0;
			int icp = cp;
			if(ne[cp]>=0){
				if(cy<0){
					cy=1;
					int ii=ne[cp];
					csum = ts[cp];
					while(ii!=cp){
						csum += ts[ii];
						ii = ne[ii];
						cy++;
					}
				}else{
				}
				if(r%cy==0){
					sum += csum * (r/cy);
					break;
				}
			}
			int ni=0;
			while(s+a[cp] <=k && ni < n){
				s+=a[cp];
				cp=(cp+1)% n;
				ni++;
			}
			ne[icp]=cp;
			ts[icp]=s;
			sum += s;
			r--;
		}
		
		printf("Case #%d: %I64d\n", nn, sum);
	}
	return 0;
}

