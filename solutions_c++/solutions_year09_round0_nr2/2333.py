#include<iostream>
using namespace std;
int update(int &j,int &k,int a[100][100],int H,int W);
int main()
{
	int a[100][100],i,j,k,T,H,W,min_j,min_k;
	int x,p,q,cnt,*points[100][100],b[10001],l,m,n;	
	scanf("%d",&T);
	for(i=0;i<T;++i){
		l=x=0;cnt=97;
		scanf("%d %d",&H,&W);
		for(j=0;j<H;++j)
			for(k=0;k<W;++k){
				points[j][k]=&x;
				scanf("%d",&a[j][k]);
			}

		b[0]=cnt;
		for(j=0;j<H;++j){
			for(k=0;k<W;++k){
				p=j,q=k;
				if((*points[j][k])==0){	
					while(1){
						if((*points[p][q])==0){
							points[p][q]=&b[l];	
							m=p,n=q;		
							update(p,q,a,H,W);		
							if(p==m && q==n){
								++l;b[l]=++cnt;
								break;
							}
						}else{
							b[l]=*points[p][q]; 
							++l,b[l]=cnt;		
							break;
						}
					}
				}	
	
			}
		}
		printf("Case #%d:\n",i+1);
		for(j=0;j<H;++j){
			for(k=0;k<W;++k){
				printf("%c ",*points[j][k]);
			}
			printf("\n");
		}
	}
}
int update(int &j,int &k,int a[100][100],int H,int W)
{
	int min_j=j,min_k=k;
	if(j-1>-1)
		if(a[min_j][min_k]>a[j-1][k]){
			min_k=k;
			min_j=j-1;
		}
	if(k-1>-1)
		if(a[min_j][min_k]>a[j][k-1]){
			min_k=k-1;
			min_j=j;
		}

	if(k+1<W)		
		if(a[min_j][min_k]>a[j][k+1]){
			min_k=k+1;
			min_j=j;
		}
	if(j+1<H)
		if(a[min_j][min_k]>a[j+1][k]){
			min_k=k;
			min_j=j+1;
		}
		
	j=min_j;
	k=min_k;
}
