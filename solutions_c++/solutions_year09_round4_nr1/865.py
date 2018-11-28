#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[50];
int nf[50];
int cm[50],cn[50],oo[50];

int main(){
	int nn,ii,n,b,c,cnt;
	scanf("%d",&nn);
	for(ii =1;ii<=nn;ii++){
		scanf("%d",&n);
		memset(cn,0,sizeof(cn));
		memset(cm,0,sizeof(cm));
		memset(nf,0,sizeof(nf));
		for(int i=0;i<n;i++){
			a[i] = 0;
			for(int j=0;j<n;j++){
				scanf("%1d",&b);
				//printf(" %d\n",b);
				if(b)a[i]=j;
			}
			oo[i] = i;
		}
		/*
		nf[n] = n;
		for(int i=n-1;i>=0;i--){
			nf[i]=nf[i+1];
			for(int j=0;j<n;j++)if(a[j]==i)nf[i]--;
			printf(" %d: %d\n",i,nf[i]);
		}
		*/
		
		for(int i=0;i<n;i++){
			int tg = a[i];
			while(nf[tg])tg++;
			nf[tg]=1;
			cn[i]=tg;
			//if(tg<i)for(int j=tg;j<i;j++)cm[j]++;
			//if(tg>i)for(int j=i;j<tg;j++)cn[j]++;
		}
		
		cnt=0;
		
		
		/*
		int did = 1;
		while(did){
			did=0;
		for(int i=0;i<n;i++)for(int i2=0;i2<n;i2++){
			for(int j=n-2;j>=i;j--){
				if(j<cn[oo[j]] && j+1>cn[oo[j+1]]){
				//if(a[j]>a[j+1] && j+1>=nf[a[j+1]+1]){
					c=a[j];
					a[j]=a[j+1];
					a[j+1]=c;
					
					c=oo[j];
					oo[j]=oo[j+1];
					oo[j+1]=c;
					cnt++;
					did = 1;
				//	printf(" kk ");
				}
			}
		}
		
		for(int i=0;i<n && !did;i++){
			for(int i2=0;i2<n && !did;i2++){
				for(int j=n-2;j>=i && !did;j--){
					if(a[j]>a[j+1] && (j<cn[oo[j]] || j+1>cn[oo[j+1]])){
					//if(a[j]>a[j+1] && j+1>=nf[a[j+1]+1]){
						c=a[j];
						a[j]=a[j+1];
						a[j+1]=c;
						
						c=oo[j];
						oo[j]=oo[j+1];
						oo[j+1]=c;
						cnt++;
						did = 1;
					//printf(" pp ");
						break;
					}
				}
			}
		}
		//if(ii==15){
		//	for(int i=0;i<n;i++)printf("%d", a[i]);
		//	printf("\n");
		//}
		
	}*/
		//cnt = 0;
		//for(int i=0;i<n-1;i++)cnt += max(cm[i],cn[i]);
		
		
		for(int i=0;i<n;i++){
			for(int j=i;j<n;j++)if(cn[oo[j]]==i){
				for(int k=j-1;k>=i;k--){
						c=a[k];
						a[k]=a[k+1];
						a[k+1]=c;
						
						c=oo[k];
						oo[k]=oo[k+1];
						oo[k+1]=c;
						cnt++;
				}
				break;
			}
			
		}
					
		
		printf("Case #%d: %d\n",ii,cnt);
	}
	return 0;
}
