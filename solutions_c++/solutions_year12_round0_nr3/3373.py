#include<cstdio>
#include<cstring>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

bool check(int x,int y){
	char s[16]; sprintf(s,"%d",x); int m=strlen(s);
	char t[16]; sprintf(t,"%d",y); int n=strlen(t);
	if(m!=n) return false;
	rep(i,m) if(strncmp(s,t+i,m-i)==0 && strncmp(s+m-i,t,i)==0) return true;
	return false;
}

void solve(){
	int a,b; scanf("%d%d",&a,&b);
	int ans=0;
	for(int n=a;n<=b;n++) for(int m=n+1;m<=b;m++) if(check(n,m)) ans++;
	printf("%d\n",ans);
}

int main(){
	int T; scanf("%d",&T);
	for(int t=1;t<=T;t++) printf("Case #%d: ",t), solve();
	return 0;
}
