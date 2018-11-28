#include<stdio.h>
#include<string.h>

typedef __int64 LL;
const int N=26;
const int M=10009;

int ft[110][N];
int temp[N];
int fuc[100][6],len[100],fn;
int n;
int cho[100];
int ans;
int ha[110],inv[110];

void dfs(int d,int deep,int w){
	int i,j,k,t,go;
	if(d==deep){
		memset(temp,0,sizeof(temp));
		for(i=0;i<d;i++){
			for(j=0;j<N;j++) temp[j]+=ft[cho[i]][j];
		}
		go=ha[deep];
		i=0;
		while(i<d){
			j=i;
			while(j<d&&cho[j]==cho[i]) j++;
			go=go*inv[j-i]%M;
			i=j;
		}
		t=0;
		for(i=0;i<fn;i++){
			k=1;
			for(j=0;j<len[i];j++){
				k*=temp[fuc[i][j]];
				k%=M;
			}
			t+=k;
			t%=M;
		}
		ans=ans+go*t;
		ans%=M;
		return ;
	}
	for(i=w;i<n;i++){
		cho[d]=i;
		dfs(d+1,deep,i);
	}
}
int ext_gcd(int a,int b,int& x,int& y){
	int t,ret;
	if (!b){
		x=1,y=0;
		return a;
	}
	ret=ext_gcd(b,a%b,x,y);
	t=x,x=y,y=t-a/b*y;
	return ret;
}


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	char s[10000];
	int i,j,k,t,T,ca,kk;
	int last;
	ca=0;
	ha[0]=1; inv[0]=1;
	for(i=1;i<110;i++){
		ha[i]=(i*ha[i-1])%M;
		ext_gcd(ha[i],M,inv[i],j);
		inv[i]%=M;
		if(inv[i]<0) inv[i]+=M; 
	}
	scanf("%d",&T);
	while(T--){
		scanf("%s%d",s,&kk);
		t=strlen(s);
		fn=0;
		i=0;
		while(i<t){
			
			while(i<t&&s[i]=='+') i++;
			if(i>=t) break;
			len[fn]=0;
			while(i<t&&s[i]!='+'){
				fuc[fn][len[fn]++]=s[i]-'a';
				i++;
			}
			fn++;
		}
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",s);
			memset(ft[i],0,sizeof(ft[i]));
			t=strlen(s);
			for(j=0;j<t;j++){
				ft[i][s[j]-'a']++;
			}
		}

		printf("Case #%d:",++ca);
		
		for(k=1;k<=kk;k++){
			ans=0;
			dfs(0,k,0);
			printf(" %d",(ans)%M);
			
		}
		printf("\n");
	}
	return 0;
}
