#include<cstdio>
#include<cstring>

typedef __int64 LL;
const int maxn=6555;

LL R,ki,n,g[2210];
LL rin[1010];
LL pers[2210],gg[2210];


LL MIN(LL a,LL b) {return a<b?a:b;}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,ca,ct=1;
	scanf("%d",&ca);
	while(ca--) {
		scanf("%I64d%I64d%I64d",&R,&ki,&n);
		for(i=0;i<n;i++) scanf("%I64d",&g[i]);
		memset(pers,0,sizeof(pers));
		memset(rin,0,sizeof(rin));
		memset(gg,0,sizeof(gg));
		LL now=0,flag=0;
		LL ans=0,cnt;
		pers[0]=1;
		for(i=0;i<MIN(R,n+2);i++){
			j=now;
			flag=0,cnt=0;
			while(flag==0||j!=now){
				if(cnt+g[j]>ki) break;
				cnt+=g[j];
				j=(j+1)%n;
				flag=1;
			}
			if(flag==0) break;
			pers[j]++;
			ans+=cnt;
			if(pers[j]>1) break;
			rin[j]=rin[now]+cnt;
			gg[j]=gg[now]+1;
			now=j;
		}
		printf("Case #%d: ",ct++);
		if(g[now]>ki||i==R) {printf("%I64d\n",ans);continue;}
		ans=ans-cnt+(R-i)/(i-gg[j]+1)*(ans-rin[j]);
		LL has=(R-i)%(i-gg[j]+1);
		for(i=0;i<has;i++){	
			j=now;
			flag=0,cnt=0;
			while(flag==0||j!=now){
				if(cnt+g[j]>ki) break;
				cnt+=g[j];
				j=(j+1)%n;
				flag=1;
			}
			if(flag==0) break;
			ans+=cnt;
			now=j;
		}
		printf("%I64d\n",ans);
	}
	return 0;
}