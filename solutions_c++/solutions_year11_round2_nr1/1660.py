#include<iostream>
#include<cstdio>

using namespace std;

int main(){
	int i,j,k,l,m,n,t;
	int A[100][100];
	double WP[100],OWP[100],OOWP[100];
	scanf("%d",&t);
	char c;
	int p=1;
	while(p<=t){
		printf("Case #%d:\n",p++);
		scanf("%d",&n);
		for(i=0;i<n;i++){
			c=getchar();
			for(j=0;j<n;j++){
				c=getchar();
				if(c=='.') A[i][j]=-1;
				else A[i][j]=c-'0';
			}
		}
		double total,pos,sum;
		for(i=0;i<n;i++){
			total=pos=0;
			for(j=0;j<n;j++){
				if(A[i][j] !=-1) total++;
				if(A[i][j] !=-1 && A[i][j] != 0) pos++;
			}
			WP[i]=pos/total;
		}
		float count;
		for(i=0;i<n;i++){
			sum=0;
			count=0;
			for(j=0;j<n;j++){
				if(A[i][j] != -1){
					count++;
					total=0;
					pos=0;
					for(k=0;k<n;k++){
						if(k!=i){
							if(A[j][k] !=-1) total++;
							if(A[j][k] !=-1 && A[j][k]!=0 ) pos++;
						}
					}
					//cout<<i<<" "<<j<<" " <<pos<<" "<<total<<"\n";
					sum+=pos/total;
				}
			}
			//cout<<"count "<<count<<"\n";
			OWP[i]=sum/count;
		}
		for(i=0;i<n;i++){
			count=0;
			sum=0;
			for(j=0;j<n;j++){
				if(A[i][j] != -1){
					count++;
					sum+=OWP[j];
				}
			}
			if(count>0){
				OOWP[i]=sum/count;
			}else{
				OOWP[i]=0;
			}
		}
		for(i=0;i<n;i++){
			printf("%0.10lf\n",0.25*WP[i]+0.50*OWP[i]+0.25*OOWP[i]);
		}
	}
	return 0;
}
