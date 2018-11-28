#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
using namespace std;

long t;
long D,I,m,n;
long a[1000];
long v[1000][256];
long list1[1000][2],s1,e1;
long list2[1000][2],s2,e2;
long list3[1000][2],s3,e3;

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	long h,i,j,k,l;
	scanf("%ld",&t);
	for(h=1;h<=t;h++){
		scanf("%ld%ld%ld%ld",&D,&I,&m,&n);
		
		for(i=0;i<256;i++)
			v[0][i]=0;
		for(i=1;i<1000;i++)
			for(j=0;j<256;j++)
				v[i][j]=100000000;
		for(i=1;i<=n;i++)
			scanf("%ld",&a[i]);
		for(j=1;j<=n;j++){
			s1=e1=0;k=0;
			for(i=0;i<256;i++){
				if(v[j][i]>v[j-1][i]+D)v[j][i]=v[j-1][i]+D;
				if(v[j][a[j]]>v[j-1][i] && labs(a[j]-i)<=m)v[j][a[j]]=v[j-1][i];
				while(e1>s1 && list1[s1][0]<i-m)s1++;
				while(k<=i+m && k<256){
					while(e1>s1 && list1[e1-1][1]>v[j-1][k])e1--;
					list1[e1][0]=k;
					list1[e1][1]=v[j-1][k];
					e1++;
					k++;
				}
				if(v[j][i]>list1[s1][1]+labs(i-a[j]))v[j][i]=list1[s1][1]+labs(i-a[j]);
				/*for(k=0;k<256;k++){
					if(labs(k-i)<=m && v[j][i]>v[j-1][k]+labs(i-a[j]))
						v[j][i]=v[j-1][k]+labs(i-a[j]);
				}*/
			}
			s2=e2=0;
			for(i=0;i<256;i++){
				while(e2>s2 && list2[s2][0]<i-m)s2++;
				if(e2>s2 && v[j][i]>list2[s2][1]+I)v[j][i]=list2[s2][1]+I;
				while(e2>s2 && list2[e2-1][1]>v[j][i])e2--;
				list2[e2][0]=i;
				list2[e2][1]=v[j][i];
				e2++;
			}
				/*for(k=0;k<256;k++)
					if(labs(i-k)<=m && v[j][k]>v[j][i]+I)v[j][k]=v[j][i]+I;*/
			s3=e3=0;
			for(i=255;i>=0;i--){
				while(e3>s3 && list3[s3][0]>i+m)s3++;
				if(e3>s3 && v[j][i]>list3[s3][1]+I)v[j][i]=list3[s3][1]+I;
				while(e3>s3 && list3[e3-1][1]>v[j][i])e3--;
				list3[e3][0]=i;
				list3[e3][1]=v[j][i];
				e3++;
			}
				/*for(k=0;k<256;k++)
					if(labs(i-k)<=m && v[j][k]>v[j][i]+I)v[j][k]=v[j][i]+I;*/
		}
		k=1000000000;
		for(j=0;j<256;j++)
			if(v[n][j]<k)k=v[n][j];
		printf("Case #%ld: %ld\n",h,k);
	}
	return 0;
}
