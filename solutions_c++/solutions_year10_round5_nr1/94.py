#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long LL;

LL egcd(LL a, LL b, LL &x, LL &y){
	LL d;
	if(b==0){x=1;y=0;return a;}
	d=egcd(b, a%b, y, x);
	y-=a/b*x;return d;
}

LL gm(LL a, LL m){
	return ((a%m)+m)%m;
}

LL inv(LL a, LL p){
	LL x, y;
	LL g = egcd(a, p, x, y);
	if(g!=1)return -1;
	//printf(" inv %d mod %d = %d\n", a, p, gm(x, p));
	return gm(x, p);
}


LL d, n, p, an, kok, rp,ans, ma;
LL a[110];
char isp[2000100];

LL reg(LL k){
	if(k<0)return 0;
	if(an<0){
		an = k;
	}else{
		if(an != k){
			kok=1;
		}
	}
}		

int main(){
	int nnt, ntt;
	memset(isp, 0, sizeof(isp));
	for(int i=2; i<2000100; i++)if(!isp[i])
	for(int j=i*2; j<2000100; j+=i)isp[j]=1;
	
	scanf("%d", &nnt);
	for(ntt = 1; ntt<=nnt; ntt++){
		scanf("%lld%lld", &d, &n);
		printf("Case #%d: ", ntt);
		ma=0;
		for(int i=0; i<n; i++){
			scanf("%lld", &a[i]);
			if(a[i]>ma)ma=a[i];
		}
		LL p10=1; for(int i=0; i<d;i++)p10*=10;
		ans=-1;
		int dunno=0;
		for(p=ma+1; p<=p10; p++)if(!isp[p]){
			an = -1;
			kok=0;
			for(int i=0;i<n-2; i++){
				LL s = gm(a[i+1]-a[i], p);
				LL t = gm(a[i+2]-a[i+1], p);
				if(s!=0 && t==0){
					reg(0);
					if(kok)break;
				}else if(s!=0 && t!=0){
					reg(gm(inv(s, p)*t, p));
					if(kok)break;
				}
			}
			if(!kok){
				//printf(" p=%d, an=%d\n", p, an);
				if(an<0){
					if(n>=2 && a[n-2]==a[n-1])
						an=0;
					else{
						printf("I don't know.\n");
						dunno=1;
						break;
					}
				}
				LL bb = gm( a[1]-a[0]*an, p);
				LL tans = gm( an*a[n-1] + bb, p);
				if(ans!=-1 && tans!=ans){
					printf("I don't know.\n");
					dunno=1;
					break;
				}
				ans = tans;
				
			}
		}
		if(!dunno)printf("%lld\n", ans);
	}
	return 0;
}

