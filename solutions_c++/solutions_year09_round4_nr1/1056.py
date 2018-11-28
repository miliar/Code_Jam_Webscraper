#include<cstdio>
#include<cstdlib>
#include<algorithm>


#define N 45
int tc,ans,n;
int data[N];

void swap(int &a,int &b){
	int t=a;
	a=b;
	b=t;
}
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int i,j,k;
	char str[N];

	scanf("%d",&tc);
	for(int tcc=1;tcc<=tc;tcc++){
		scanf("%d ",&n);
		memset(data,0,sizeof(data));
		for(i=0;i<n;i++){
			gets(str);
			for(j=n-1;j>=0;j--){
				if (str[j]=='1'){
					data[i]=j;
					break;
				}
			}
		}
		ans=0;
		for(i=0;i<n;i++){
			if (data[i]<=i) continue;
			for(j=i+1;j<n;j++){
				if (data[j]<=i) {
					for(k=j;k>i;k--){
						swap(data[k],data[k-1]);
						ans++;
					}
					break;
				}
			}
		}
		printf("Case #%d: %d\n",tcc,ans);
	}
	return 0;
}