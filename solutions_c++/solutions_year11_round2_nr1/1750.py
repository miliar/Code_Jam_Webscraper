#include<stdio.h>
#include<string.h>
#include <iostream>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout); 
	int i,j,n,k,l,p,q,T;
	char a[101][101],s[100];
	double WP[101],OWP[101],OOWP[101],RPI[101];
	int w[101],c[101];
	scanf("%d",&T);
	double sum;
	for(int z=1;z<=T;z++){
		printf("Case #%d:\n",z);
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",a[i]);
		for(i=0;i<n;i++){
			w[i]=c[i]=0;
			for(j=0;j<n;j++)
				if(a[i][j]!='.'){
					if(a[i][j]=='1')w[i]++;
					c[i]++;
				}
			WP[i] = w[i]*1.0/c[i];
		}
		for(i=0;i<n;i++){
			sum=0;
			for(j=0;j<n;j++)
				if(a[i][j]!='.')
				sum+=(w[j]-(a[i][j]=='0'))*1.0/(c[j]-1);
			OWP[i] = sum/c[i];
		}

		for(i=0;i<n;i++){
			sum = 0;
			for(j=0;j<n;j++)
				if(a[i][j]!='.')
					sum += OWP[j];
			OOWP[i]=sum/c[i];
		}
		for(i=0;i<n;i++){
			RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			sprintf(s,"%.12lf",RPI[i]);
			int  iii = strlen(s)-1;
			while(s[iii]=='0')iii--;
			s[iii+1] = 0;
			printf("%s\n",s);
		}
		
	} 
	return 0;
}
