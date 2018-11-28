#include <stdio.h>
#include <string.h>

int a[7],b[7],tmp[7],pre[7];
int anum,bnum;

int smaller(int* a, int* b){
	int i;
	for(i=6; i>=0; i--){
		if(a[i]<b[i]){
			return 1;
		}
		else if(a[i]>b[i]){
			return -1;
		}
	}
	return 0;
}

void increase(int* a){
	int i=0;
	if(a[i]<9) a[i]++;
	else if(a[++i]<9){
		a[0]=0;
		a[i]++;
	}
	else if(a[++i]<9){
		a[0]=a[1]=0;
		a[i]++;
	}
	else if(a[++i]<9){
		a[0]=a[1]=a[2]=0;
		a[i]++;
	}
	else if(a[++i]<9){
		a[0]=a[1]=a[2]=a[3]=0;
		a[i]++;
	}
	else if(a[++i]<9){
		a[0]=a[1]=a[2]=a[3]=a[4]=0;
		a[i]++;
	}
	else if(a[++i]<9){
		a[0]=a[1]=a[2]=a[3]=a[4]=a[5]=0;
		a[i]++;
	}
	if(i>anum)
		anum++;
}


int main(int argc, char** argv){
	int i,j,k,p,T,ans,A,B;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&T);
	for(i=1; i<=T; i++){
		for(j=0; j<7; j++){
			a[j]=0;
			b[j]=0;
		}
		scanf("%d%d",&A,&B);
		anum=0;
		while(A>0){
			a[anum++]=A%10;
			A /= 10;
		}
		bnum=0;
		while(B>0){
			b[bnum++]=B%10;
			B /= 10;
		}
		ans = 0;
		while(smaller(a,b)==1){
			for(p=0; p<anum-1; p++){
				for(j=0; j<7; j++)
					tmp[j]=0;
				for(j=p+1, k=0; j<anum; j++){
					tmp[k++]=a[j];
				}
				for(j=0; j<=p; j++){
					tmp[k++]=a[j];
				}
				if(smaller(a, tmp)==1 && smaller(tmp, b)!=-1 && smaller(tmp, pre)!=0){
				/*	for(k=anum-1; k>=0; k--){
						printf("%d",a[k]);
					}
					printf(" ");
					for(k=anum-1; k>=0; k--){
						printf("%d",tmp[k]);
					}
					printf("\n");*/
					for(k=0; k<7; k++){
						pre[k]=tmp[k];
					}
					ans++;
				}
			}
			increase(a);
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}