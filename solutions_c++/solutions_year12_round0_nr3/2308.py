#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<map>
using namespace std;

int a,b,t,cc[2000005];
char s[100],bs[100];

int main(){
	memset(cc,0,sizeof(cc));
	for (int x=1;x<=2000000;++x){
		map<int,bool> visit;
		sprintf(s,"%d",x);
		int len=strlen(s),y=x,pp=1;
		for (int i=1;i<len;++i) pp*=10;
		for (int n=1;n<len;++n){
			int tmp=y%10; y/=10; y+=tmp*pp;
			if (x<y && visit.find(y)==visit.end()) ++cc[x],visit[y]=1;
		}
	}	
	scanf("%d",&t);
	for (int tt=1;tt<=t;++tt){
		scanf("%d%d",&a,&b);
		sprintf(bs,"%d",b);
		int blen=strlen(bs);
		int ans=0;
		for (int x=a;x<=b;++x){
			map<int,bool> visit;
			sprintf(s,"%d",x);
			int len=strlen(s),y=x,pp=1;
			if (len<blen){
	  		   ans+=cc[x];
	  		   continue;
	  		}
			for (int i=1;i<len;++i) pp*=10;
			for (int n=1;n<len;++n){
				int tmp=y%10; y/=10; y+=tmp*pp;
				if (x<y && a<=y && y<=b && visit.find(y)==visit.end()) ++ans,visit[y]=1;
			}
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
