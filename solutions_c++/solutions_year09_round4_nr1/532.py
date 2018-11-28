#include<stdio.h>
#include<memory.h>
#include<algorithm>

int T,ans,d[111],max,mi,n;
char s[111];
            

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=0;_<T;_++){
		memset(d,0,sizeof(d));
		ans=0;

		scanf("%d\n",&n);
		for(int i=0;i<n;i++){
			gets(s);
			for(int j=0;j<n;j++)
				if(s[j]-48)
					d[i]=j;
		}
		for(int i=0;i<n;i++)if(d[i]>i){
			max=-1;
			mi=-1;
			for(int j=i+1;j<n;j++)if(d[j]<=i){
				max=d[j];
				mi=j;
				break;
			}
			memcpy(&d[i+1],&d[i],(mi-i)<<2);
			d[i]=max;
			ans+=mi-i;
		}

		printf("Case #%d: %d\n",_+1,ans);
	}
	return 0;
}
