#include<iostream>
using namespace  std;

long t;
long v[30],d[30],x[30];

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	long h,i,j,k,l;
	scanf("%ld",&t);
	while(getchar()!='\n');
	for(h=1;h<=t;h++){
		memset(v,0,sizeof(v));
		memset(d,0,sizeof(d));
		memset(x,0,sizeof(x));
		i=0;
		while(1){
			scanf("%c",&v[i]);
			if(v[i]=='\n')break;
			i++;
		}
		v[i]=0;
		for(j=i-1;j>=0;j--){
			v[j]-='0';
		}
		for(j=i-1;j>=0;j--)d[j]=v[i-j-1];
		for(j=0;j<i-1;j++)
			if(d[j]>d[j+1])break;
		for(k=0;k<=j+1;k++)
			x[d[k]]++;
		for(k=0;k<10;k++)
			if(x[k]!=0 && k>d[j+1]){
				d[j+1]=k;x[k]--;
				break;
			}
		l=j;
		for(k=0;k<10;k++)
			while(x[k]!=0){
				d[l]=k;
				x[k]--;
				l--;
			}
		printf("Case #%ld: ",h);
		if(d[i]!=0)printf("%ld",d[i]);
		for(k=i-1;k>=0;k--)printf("%ld",d[k]);
		putchar('\n');
	}
	return 0;
}