#include<stdio.h>
#include<malloc.h>
int main(){
	int T,N;
	float **schedule;
	scanf("%d",&T);
	int i,j,k,l,m,n,yash,count;
	float *wp,*owp,*oowp,*wp1,*rpi;
	char ch;
	for(i=1;i<=T;i++){
		scanf("%d",&N);
		wp=(float*)malloc(sizeof(float)*N);
		wp1=(float*)malloc(sizeof(float)*N);
		owp=(float*)malloc(sizeof(float)*N);
		oowp=(float*)malloc(sizeof(float)*N);
		schedule=(float**)malloc(sizeof(float*)*N);
		rpi=(float*)malloc(sizeof(float)*N);
		for(j=0;j<N;j++)
			schedule[j]=(float*)malloc(sizeof(float)*N);
		for(k=0;k<N;k++){
			for(l=0;l<N;l++){
				ch='\n';
				while(ch=='\n'||ch==' ')
					scanf("%c",&ch);
				if(ch=='.')
					schedule[k][l]=-1;
				else if(ch=='1')
					schedule[k][l]=1;
				else schedule[k][l]=0;
			}
		}
		for(k=0;k<N;k++){
			wp[k]=0;
			count=0;
			for(l=0;l<N;l++){
				if(schedule[k][l]!=-1)
					count++;
				if(schedule[k][l]==1)
					wp[k]++;
			}
			wp[k]/=(float)count;
		}
		for(k=0;k<N;k++){
			owp[k]=0;
			for(l=0;l<N;l++){
				if(schedule[k][l]==-1)
				{
					wp1[l]=-1;
					continue;
				}
				wp1[l]=0;
				if(l==k)
				{wp1[l]=-1;	
				continue;
				}
				count=0;
				for(m=0;m<N;m++){
					if(m==k)
					{	
						continue;
					
					}
				//	if(schedule[k][m]==-1)
				//		continue;
					if(schedule[l][m]!=-1)
						count++;
					if(schedule[l][m]==1)
						wp1[l]++;
				}
				if(count!=0)
					wp1[l]/=(float)count;
				else wp1[l]=-1;
			}
			count=0;
			for(yash=0;yash<N;yash++){
				if(yash==k||schedule[k][yash]==-1)
					continue;
				if(wp1[yash]!=-1){
					count++;
					if(k==3)
					{ 
	//				printf(";yash=%d ;;;%f;;;;;;",yash,wp1[yash]);
					}
					owp[k]+=wp1[yash];
				
				}
			}
		//	if(count!=0)
				owp[k]/=(float)count;
	//		else owp[k]=-1;
		}
		for(yash=0;yash<N;yash++){
			count=0;
			oowp[yash]=0;
			for(l=0;l<N;l++){
				if(l==yash||schedule[yash][l]==-1)
					continue;
				oowp[yash]+=owp[l];
				count++;
			}
			oowp[yash]/=(float)count;
		}
		printf("Case #%d:\n",i);
		for(yash=0;yash<N;yash++){
	        rpi[yash]=0.25*wp[yash]+0.50*owp[yash]+0.25*oowp[yash];
	//	printf("---wp = %f ----owp = %f ----oowp = %f \n",wp[yash],owp[yash],oowp[yash]);
		printf("%f\n",rpi[yash]);	
		}
	}
		return 0;
}
