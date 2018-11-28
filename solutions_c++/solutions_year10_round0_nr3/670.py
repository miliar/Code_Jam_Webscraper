#include<stdio.h>
#include<memory.h>

int T,r,k,n,pos,col,a[3111],sz,ss,was[3111],j;
long long sum,total,S[3111];

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		scanf("%d%d%d",&r,&k,&n);
		memset(was,0,sizeof(was));
		for(int i=1;i<=n;i++) scanf("%d",&a[i]);
		pos=1;
		col=0;
		total=0;
		while(col<r){
			if(!was[pos]){
				sum=a[pos];
				for(j=(pos==n)?1:(pos+1);j!=pos && sum+a[j]<=k;j=(j==n)?1:(j+1)) sum+=a[j];
				total+=sum;
				was[pos]=++col;
				S[col]=S[col-1]+sum;
				pos=j;
			}else{
				sz=col-was[pos]+1;
				ss=(r-col)/sz;
				total+=(long long)ss*(S[col]-S[was[pos]-1]);
				col+=sz*ss;
				while(col<r){
					sum=a[pos];
					for(j=(pos==n)?1:(pos+1);j!=pos && sum+a[j]<=k;j=(j==n)?1:(j+1)) sum+=a[j];
					total+=sum;
					pos=j;
					col++;
				}
			}
		}
		printf("Case #%d: %I64d\n",_,total);
	}
	return 0;
}
