#include<cstdio>
#include<cstring>
int L,D,N,z,T,i,j,cnt;
char a[5005][20],t[1000];
bool b[20][30],in=false;
int main(){
	scanf("%d%d%d",&L,&D,&N);
	for (i=0;i<D;++i){
		scanf("%s",a[i]);
	}
	
	for (z=1;z<=N;++z){
		cnt = 0;
		for (i=0;i<L;++i) for (j=0;j<26;++j) b[i][j] = false;
		scanf("%s",t);
		T = strlen(t);
		j = 0;
		for (i=0;i<T;++i){
			if (t[i]=='('){
				in = true;
			}else if (t[i]==')'){
				in = false;
				if (in==false) ++j;
			}else{
				b[j][t[i]-'a'] = true;
				if (in==false) ++j;
			}
		}
		
		for (i=0;i<D;++i){
			j = 0;
			while (j<L && b[j][a[i][j]-'a']) ++j;
			if (j==L) ++cnt;
//			printf("%d %d\n",i,j);
		}
		
		printf("Case #%d: %d\n",z,cnt);
	}
	
	
	

	return 0;
}
