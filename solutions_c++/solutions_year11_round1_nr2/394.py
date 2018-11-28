#include<cstdio>
#include<cstring>
int n,len;
bool    p[128];
char L[32],d[128][12];
bool ok(char c){
	for(int i=0;i<n;++i)
	  if(p[i]){
		for(char *x=d[i];*x;++x)
		  if(*x==c)return true;
	}
	return false;
}
bool chk(char c,int k){
	bool oo=false;
	for(char* x=d[k];*x;++x)
		if (*x==c){
			oo= true;
			break;
		}
	
	if(oo){
		for(int i=0;i<n;++i)if(i!=k && p[i])
		  for(int j=0;j<len;++j)if((d[k][j]==c)!=(d[i][j]==c)){
				p[i]=false;break;
		}
	}else{
		for(int i=0;i<n;++i)if(i!=k && p[i])
			for(int j=0;j<len;++j)if(d[i][j]==c){
				p[i]=false;break;
			}
	}
	return oo;
}
int main(){
	freopen("bin.txt","r",stdin);
	freopen("bou.txt","w",stdout);
	int C,m,i,j,k,aa,max,t;
	scanf("%d",&C);
	for(int cc=1;cc<=C;++cc){
		scanf("%d%d",&n,&m);
		for(i=0;i<n;++i){
			scanf("%s",d[i]);
		}
		printf("Case #%d:",cc);
		while(m--){
			scanf("%s",L);
			max=-1;
			for(i=0;i<n;++i){
				memset(p,true,n);
				len=strlen(d[i]);
				t=0;
				for(j=0;j<n;++j)
				  if(j!=i && strlen(d[j])!=len)p[j]=false;
				for(j=0;j<26;++j)if(ok(L[j])){
					if(!chk(L[j],i))++t;
				}
				if(t>max){
					max=t;aa=i;
				}
			}
			printf(" %s",d[aa],max);
		}
		puts("");
	}
	return 0;
}
