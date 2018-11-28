#include<stdio.h>
#include<string.h>


const int N=31;

int f[N],s[N];



int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,t;
	memset(f,-1,sizeof(f));
	memset(s,0,sizeof(s));
	f[0]=0; f[1]=1;
	s[0]=0; s[1]=1;
	for(i=2;i<N;i++){
		f[i]=1+s[i-1];
		s[i]=s[i-1]+f[i];
	}
	scanf("%d",&t);
	k=0;
	while(t--){
		scanf("%d%d",&i,&j);
		j%=s[i]+1;
		printf("Case #%d: ",++k);
		if(j==s[i]) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}