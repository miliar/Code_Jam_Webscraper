//GCJ 1C C s
#include <cstdio>

int d[103];
int main(){
	int t,tt,n,l,h,i,j,gotit;
	bool no;
	scanf("%d",&tt);

	for(t=1;t<=tt;t++){
		scanf("%d%d%d",&n,&l,&h);
		printf("Case #%d: ",t);
		for(i=0;i<n;i++){
			scanf("%d",&d[i]);
		}
		if(l==1){
			printf("1\n");
			continue;
		}
		//c[]=0;
		for(i=l,gotit=0;i<=h;i++){
			no=0;
			//for(j=0;j<n;j++) c[j]=0;
			for(j=0;j<n;j++){
				//printf("%d %d  %d\n",i,d[j],gotit);
				//if(gotit!=i) gotit=0;
				if(i%d[j]!=0 && d[j]%i!=0){
					no=1;
					break;
				}
				//c[j]=1;
			}
			if(no) continue;
			printf("%d\n",i);
			break;
		}
		if(no) printf("NO\n");
		//if(gotit) printf("%d\n",gotit);
		//else printf("NO\n");
	}
	return 0;
}
