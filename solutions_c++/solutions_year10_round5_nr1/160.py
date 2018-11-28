#include <cstdio>
#include <cstring>
using namespace std;

const int lim=10000;

bool pr[1000010];
int p[200000];
int s[100],n;
int base;

int muti(int a,int t) {
	if (t==0) return 1;
	if (t==1) return a;
	int tmp=muti(a,t/2);
	tmp=tmp*tmp%base;
	if (t%2==0) return tmp; else return tmp*a%base;
}

bool check(int a,int &b) {
	b=(s[2]-a*s[1])%base;
	if (b<0) b+=base;
	for (int i=2;i<=n-1;i++) {
		if (((s[i]*a+b)%base)!=s[i+1]) return false;
	}
	return true;
}

int main() {
	memset(pr,true,sizeof(pr));
	int lp=0;
	memset(p,0,sizeof(p));
	for (int i=2;i<=lim;i++) {
		if (pr[i]) {
			p[++lp]=i;
			for (int j=i*i;j<=lim;j+=i) pr[j]=false;
		}
	}
	int cc,cases,d;
	scanf("%d",&cases);
	for (cc=1;cc<=cases;cc++) {
		scanf("%d%d",&d,&n);
		int ansx=-1,ans=0;
		int md=1;
		for (int i=1;i<=d;i++) md=md*10;
		int ms=-1;
		for (int i=1;i<=n;i++) {
			scanf("%d",&s[i]);
			if (s[i]>ms) ms=s[i];
		}
		if (n<=2) {
			if (s[1]==0 && s[2]==0) {
				printf("Case #%d: 0\n",cc);
				continue;
			}
			printf("Case #%d: I don't know.\n",cc);
			continue;
		}
		for (int i=1;i<=lp;i++) {
			base=p[i];
			if (base<=ms) continue;
			if (base>md) break;
			int k1=(s[2]-s[1])%base;
			if (k1<0) k1+=base;
			int k2=(s[3]-s[2])%base;
			if (k2<0) k2+=base;
//			printf("%d\n",base);
			int inv=muti(k1,base-2);
			int a=(inv*k2)%base,b=0;
//			printf("%d %d %d\n",k1,k2,a);
			if (check(a,b)) {
				int tmp=(s[n]*a+b)%base;
				if (tmp!=ansx) {
//					printf("%d %d %d\n",a,b,base);
					ans++;
					if (ansx==-1) ansx=tmp;
				}
			}
			if (ans>1) break;
		}
//		printf("%d\n",ans);
		if (ans==1) {
			printf("Case #%d: %d\n",cc,ansx);
		} else {
			printf("Case #%d: I don't know.\n",cc);
		}
	}
}
