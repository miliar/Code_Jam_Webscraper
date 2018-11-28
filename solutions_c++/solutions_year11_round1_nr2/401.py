#include<stdio.h>
#include<string> 
char d[10010][20],L[30]; 
int a[10010],lo[10010]; 
int DO(int S,int n){
	int i,j,t=0,k,l,ans=0;
	char s[30]={};
	for(i=0;n>0&&L[i]!=0;i++){
		//if(s[L[i]]!=t)continue; 
		//t++;
		for(j=0,k=0;j<n;j++){
			for(l=0;d[a[j]][l]!=0;l++){ 
				if(d[a[j]][l]==L[i]&&d[S][l]==L[i])continue;
				if(d[a[j]][l]!=L[i]&&d[S][l]!=L[i])continue;
				break;  
			} 
			if(d[a[j]][l]!=0)continue;
			a[k++]=a[j]; 
		}
		if(n==k)continue; 
		n=k;
		for(l=0;d[S][l]!=0;l++)if(d[S][l]==L[i])break;
		if(d[S][l]!=0) continue;
		ans++; 
	}	
	return ans; 
} 
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B.out","w",stdout);
	int T,t,n,m,i,j,x,ans,g,k,l;
	scanf("%d",&T); 
	for(t=1;t<=T;t++){
		printf("Case #%d:",t); 
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			scanf("%s",d[i]);
			lo[i]=strlen(d[i]); 
			} 
		for(l=0;l<m;l++){ 
			scanf("%s",L);
			ans=-1; 
			for(i=0;i<n;i++){
				for(j=0,k=0;j<n;j++){
					if(i==j||lo[i]!=lo[j])continue; 
					a[k++]=j; 
					} 
				x=DO(i,k);
				if(x>ans){ans=x;g=i;} 
			}
			printf(" %s",d[g]); 
		} 
		puts(""); 
	} 
} 
