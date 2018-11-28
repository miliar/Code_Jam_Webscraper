#include <stdio.h>
#include <string.h>

const int size=50000;
const int maxk=16;
char s[size+1];
int a[maxk],h[maxk],k,p,r;

void cal(){
	int w=1;
	char c=s[a[0]],t;
	for(int i=1; i<p; i++){
		t=s[i-i%k+a[i%k]];
		if(t!=c)
			w++;
		c=t;
	}
	if(w<r)
		r=w;
}

void dfs(int v){
	if(v==k)
		cal();
	else{
		for(int i=0; i<k; i++){
			if(h[i]) continue;
			a[v]=i;
			h[i]=1;
			dfs(v+1);
			h[i]=0;
		}
	}
}

int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("d.txt","w",stdout);
	int n,t;
	scanf("%d",&n);
	for(t=1; t<=n; t++){
		scanf("%d%s",&k,s);
		r=p=strlen(s);
		memset(h,0,sizeof(h));
		dfs(0);
		printf("Case #%d: %d\n",t,r);
	}
	return 0;
}
