#include<stdio.h>
int in[1010];
int main(){
    int t,i,j,cas=1;
    scanf("%d",&t);
    while(t--){
	int n;
	scanf("%d",&n);
	int allx=0;
	for(i=0;i<n;i++){
	    scanf("%d",&in[i]);
	    allx^=in[i];
	}
	printf("Case #%d: ",cas++);
	if(allx)puts("NO");
	else{
	    int mi=1000000000,s=0;
	    for(i=0;i<n;i++){
		s+=in[i];
		if(mi>in[i])mi=in[i];
	    }
	    printf("%d\n",s-mi);
	}
    }
}
