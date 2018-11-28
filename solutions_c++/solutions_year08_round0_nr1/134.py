#include<stdio.h>
#include <string.h>

#define MAX_S 101
#define MAX_Q 1001
#define MAX 101

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int n,s,q,i,j,k,ptr,count;
	char str_s[MAX_S][MAX];
	bool  num_s[MAX_S];
	int num;
	char str_q[MAX_Q][MAX];
	scanf("%d",&n);
	for(int t=1;t<=n;t++){
		scanf("%d",&s);
		gets(str_s[0]);
		for(i=0;i<s;i++) gets(str_s[i]);
		scanf("%d",&q);
		gets(str_q[0]);
		for(i=0;i<q;i++) gets(str_q[i]);
		count=0;
		k =0;
		while(k<=q-1){
			for(i=0;i<s;i++) num_s[i]=false;
			num = s;
			for(i=k;i<q;i++){
				for(j=0;j<s;j++){
					if(num_s[j]==false && strcmp(str_q[i],str_s[j])==0){
						num_s[j]=true;
						num--;
					}
					if(num<=0)	break;
				}
				if(num<=0)	break;
			}
		
			if(num<=0)	ptr =j;
			else	break;

			for(k;k<q;k++){
				if(strcmp(str_q[k],str_s[ptr])==0){	count++;	break;	}
			}
		}
		printf("Case #%d: %d\n",t,count);

	}
	return 0;
}
