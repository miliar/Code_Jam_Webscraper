#include<cstdio>
#include<cstring>

char a[40000][100];
char b[10000];
bool c[100][500];
int n,m,k;

bool check(char *a){
	for(int i=0;i<n;i++)
		if(c[i][a[i]]==0)return 0;
	return 1;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d%d%d",&n,&m,&k);
	int kase=0;
	for(int i=0;i<m;i++) scanf("%s",a+i);
	for(int i=0;i<k;i++){
		scanf("%s",b);
		memset(c,0,sizeof(c));
		for(int i=0,j=0;i<n;i++,j++)
			if(b[j]=='('){
				for(j++;b[j]!=')';j++)
					c[i][b[j]]=1;
			}else c[i][b[j]]=1;
		int ans=0;
		for(int i=0;i<m;i++)
			if(check(a[i]))ans++;
		printf("Case #%d: %d\n",++kase,ans);
	}
}
