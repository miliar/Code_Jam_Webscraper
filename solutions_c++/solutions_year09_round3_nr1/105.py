#include <cstdio>
#include <cstring>

char s[100];
int w[256];
int z[100];

int main(){
	unsigned long long ans,tb;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int q;
	scanf("%d",&q);
	gets(s);
	for(int k=1;k<=q;k++){
		gets(s);
		int i,l=strlen(s),b=2,c=1;
		if(l==1){
			printf("Case #%d: 1\n",k);
			continue;
		}
		for(i=0;i<256;i++)w[i]=-1;
		for(i=0;i<l;i++){
			if(w[s[i]]==-1){
				w[s[i]]=c;
				if(c==1)c=0;
				else if(c==0)c=2;
				else c++;
				if(c>b)b=c;
			}
		}
		ans=0;
		tb=1;
		for(i=l-1;i>=0;i--){
			ans=ans+tb*w[s[i]];
			tb*=b;
		}
		printf("Case #%d: %lld\n",k,ans);
	}

	return 0;
}
