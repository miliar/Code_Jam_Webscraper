#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int t,n;
int w[110][2];
int v[110];

int ab(int q){
	return q>0?q:-q;
}

int main(){
	int h,i,j,k,l,m,ans;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d",&n);
		for(i=1;i<=n;i++){
			getchar();
			if(getchar()=='B')w[i][0]=0;
			else w[i][0]=1;
			scanf("%d",&w[i][1]);
		}
		j=k=0;w[0][1]=1;
		l=m=0;
		for(i=1;i<=n;i++){
			if(w[i][0]==0){
				v[j]=i;j=i;v[j]=0;
				if(l==0)l=i;
			}else{
				v[k]=i;k=i;v[k]=0;
				if(m==0)m=i;
			}
		}
		j=k=1;ans=0;v[0]=0;
		for(i=1;i<=n;i++){
			if(w[i][0]==0){
				ans+=ab(j-w[i][1])+1;
				if(m!=0){
					if(ab(k-w[m][1])>ab(j-w[i][1])){
						if(k<w[m][1])k+=ab(j-w[i][1])+1;
						else k-=ab(j-w[i][1])+1;
					}else{
						k=w[m][1];
					}
				}
				j=w[i][1];
				l=v[l];
			}else{
				ans+=ab(k-w[i][1])+1;
				if(l!=0){
					if(ab(j-w[l][1])>ab(k-w[i][1])){
						if(j<w[l][1])j+=ab(k-w[i][1])+1;
						else j-=ab(k-w[i][1])+1;
					}else{
						j=w[l][1];
					}
				}
				k=w[i][1];
				m=v[m];
			}
		}
		printf("Case #%d: %d\n",h,ans);
	}
	return 0;
}
