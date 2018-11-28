#include<stdio.h>
#include<algorithm>
int a[101];
bool cmp(int x,int y){
	return x>y;
}
main(){
	int i,j,cnt;
	int T,TN=0;
	int n,s,p;
	scanf("%d",&T);
	while(T--){
		TN++;
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		std::sort(a,a+n,cmp);
		cnt=0;
		for(i=0;i<n;i++){
			if((a[i]+2)/3>=p){
				cnt++;
			} else if(a[i]!=0&&(a[i]%3==0||a[i]%3==2)&&(a[i]+1)/3==p-1&&s>0){
				cnt++;
				s--;
			}
		}
		printf("Case #%d: %d\n",TN,cnt);
	}
}
