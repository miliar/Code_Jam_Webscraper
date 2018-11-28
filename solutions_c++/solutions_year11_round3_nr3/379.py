#include<stdio.h>
#include<math.h>
#include<algorithm>
long long a[10001],b[10001];
long long mgcds[10001],mlcms[10001];
long long yuscvscv(long long a,long long b){
	while((a%=b)&&(b%=a));
	return a+b;
}
double fa[10001];
long long tp;
long long BMN,BMX,BMD;
long long ioi;
long long ggm[100001],mx;
main(){
	//by magrady
	//KSHS
	int T,TN;
	int N;
	long long L,H;
	int i,j,k;
	long long h,hh;
	long long MN,MX;
	double db;
	scanf("%d",&T);
	for(TN=1;TN<=T;TN++){
		scanf("%d%I64d%I64d",&N,&L,&H);
		for(i=0;i<N;i++){
			scanf("%I64d",&b[i]);
		}
		std::sort(b,b+N);
		k=0;
		for(i=0;i<N;i++){
			if(!i||b[i]!=b[i-1]){
				a[k++]=b[i];
			}
		}
		
		N=k;

		for(i=0;i<N;i++){
			fa[i]=log10(a[i]);
		}
		mgcds[N-1]=a[N-1];
		for(i=N-2;i>=0;i--){
			mgcds[i]=yuscvscv(mgcds[i+1],a[i]);
		}
		
		
		
		
		mlcms[0]=a[0];
		for(i=1;i<N;i++){
			tp=yuscvscv(mlcms[i-1],a[i]);
			db=log10(mlcms[i-1])+fa[i]-log10(tp);
			if(db>16.5||(mlcms[i-1]/tp)*(a[i]/tp)*tp>10000000000000000ll){
				for(;i<N;i++){
					mlcms[i]=-1;
				}
				break;
			}
			mlcms[i]=mlcms[i-1]/tp;
			mlcms[i]*=a[i]/tp;
			mlcms[i]*=tp;
		}
		

		ioi=-1;

		long long tH;
		for(i=-1;i<N;i++){
			MX=(i==(N-1))?-1:mgcds[i+1];
			MN=(i==-1)?1:mlcms[i];
			if(MN==-1)break;
			if(MN>MX&&MX!=-1)continue;
			if(MN>H)continue;
			if(MX<L&&MX!=-1)continue;
			
			if(MX%MN&&MX!=-1)continue;
			if(MN>=L){
				ioi=MN;
				break;
			}
			
			if(MX!=-1)tH=MX;
			else tH=H;
			tH<?=H;
			if(i!=N-1)tH<?=a[i+1]-1;

			mx=0;
			if(MX!=-1){
				h=MX/MN;
				for(hh=2;hh*hh<=h;hh++){
					if(h%hh==0){
						ggm[mx++]=hh;
						if(hh*hh<h)ggm[mx++]=h/hh;
					}
				}
				ggm[mx++]=h;
				
				std::sort(ggm,ggm+mx);

				BMN=0;
				BMX=mx-1;
				
				while(BMN<=BMX){
					BMD=(BMN+BMX)/2;
					if(log10(ggm[BMD])+log10(MN)<16.5&&ggm[BMD]*MN<L){
						BMN=BMD+1;
					} else {
						BMX=BMD-1;
					}
				}

				if(ggm[BMN]*MN>=L&&(ggm[BMN]*MN<=tH&&MX%(ggm[BMN]*MN)==0||MX==-1)){
					ioi=MN*ggm[BMN];
					break;
				}
			} else {
				BMN=2;
				BMX=10000000000000000ll;
				while(BMN<=BMX){
					BMD=(BMN+BMX)/2;
					if(log10(BMD)+log10(MN)<16.5&&BMD*MN<L){
						BMN=BMD+1;
					} else {
						BMX=BMD-1;
					}
				}
				if(BMN*MN>=L&&(BMN*MN<=tH&&BMN*MN<=MX||MX==-1)){
					ioi=MN*BMN;
					break;
				}
			}
		}

		if(ioi==-1){
			printf("Case #%d: NO\n",TN);
		} else {
			printf("Case #%d: %I64d\n",TN,ioi);
		}
					
	}
	
		
}
