#include <stdio.h>
#include <algorithm>
#include <vector>
#include <assert.h>
using namespace std;
#define MAX 1000000
#define IDN "I don't know.\n"
typedef long long ll;

int era[MAX+10];

ll powmod(ll a, ll b, ll m){
	if(b==0)return 1;
	if(b%2==1)return (powmod(a,b-1,m)*a)%m;
	ll c=powmod(a,b/2,m);
	return (c*c)%m;
}

main(){
	vector<ll> prm;
	for(int i=2;i<=MAX;i++)for(int j=2;i*j<=MAX;j++)era[i*j]=1;
	for(int i=2;i<=MAX;i++)if(era[i]==0)prm.push_back(i);
	//printf("done.\n");
	
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		int dd,k;
		scanf("%d%d",&dd,&k);
		ll d=1;
		for(int i=0;i<dd;i++)d*=10;
		ll a[20];
		for(int i=0;i<k;i++){
			scanf("%lld",&a[i]);
		}
		printf("Case #%d: ",t);
		if(k==1){
			printf(IDN);
		}else{/*
			int si=-1;
			for(int i=0;i<k-1;i++){
				if(a[i]==a[k-1])si=i;
			}
			if(si!=-1){printf("%lld\n",a[si+1]);continue;}
			*/
			if(a[0]==a[1]){printf("%lld\n",a[1]);continue;}
			if(k==2){printf(IDN);continue;}
			vector<ll> ans;
			ans.clear();
			for(int pn=0;pn<prm.size();pn++){
				ll P=prm[pn];
				if(P>d)break;
				if(a[0]>=P)continue;
				//printf("p=%lld\n",P);
				ll A=(((a[2]-a[1])%P+P)%P)*powmod(((a[1]-a[0])%P+P)%P,P-2,P)%P;
				ll B=((a[1]-a[0]*A)%P+P)%P;
				if(!(A>=0 && B>=0)){printf("P=%lld A,B=%lld %lld\n",t,P,A,B);return 0;}
				bool ok=true;
				for(int i=0;i<k-1;i++){
					if(a[i+1]!=(a[i]*A+B)%P)ok=false;
				}
				if(ok){
					//puts("ok");
					ans.push_back((a[k-1]*A+B)%P);
					//printf("%lld? ",(a[k-1]*A+B)%P);
				}
			}
			sort(ans.begin(),ans.end());
			ans.erase(unique(ans.begin(),ans.end()),ans.end());
			if(ans.size()==0){fprintf(stderr,"hogehoge\n");return 0;}
			if(ans.size()==1){printf("%lld\n",ans[0]);}
			else {printf(IDN);}
			
		}
		
	}
}