#include<stdio.h>
int main()
{
   freopen("C:\\C-small-attempt0.in","r",stdin);
    freopen("c:\\C-small-attempt0.out","w",stdout);
    int q[10],t,r,n,k,cns=0,ans,temp,p,l,j;
    scanf("%d",&t);
    while(t--){
		l=0;
		cns++;
		j=0;
		ans=0;
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0;i<n;i++)
		scanf("%d",&q[i]);
		for(int i=0;i<r;i++){
		//	printf("\nround %d:",i);
			temp=0;
		while(1){
			temp+=q[j];
		//	printf("%d ",q[j]);
			j++;
			if(j>=n) j=0;
			p=j;
		if(temp+q[j]>k||l==j) break;
		}
here:
//	printf("temp %d",temp);
		l=p;
		ans+=temp;
	}
	printf("Case #%d: %d\n",cns,ans);			
}
}
