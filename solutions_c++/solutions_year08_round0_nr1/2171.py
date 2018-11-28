#include<iostream>
#include<string>
#include<map>
using namespace std;

const int maxn=110;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int count[maxn],i,j,n,q,t;

	int ca=0;
	map<string,int>mq;
	string str;
	char s[110];
	scanf("%d",&t);

	while(t--){
		mq.clear();
		scanf("%d",&n);
		getchar();
		for(i=1;i<=n;i++){
			gets(s);
			str=string(s);
			mq[str]=i;
		}
		memset(count,0,sizeof(count));
		scanf("%d",&q);
		printf("Case #%d: ",++ca);
		

		
         getchar();
		int id;
		int nn=0;
		for(nn=0;nn<q;nn++){
			gets(s);
			str=string(s);
		    id=mq[str];
			if(nn==0){
				count[ id ]=100000;
				continue;
			}
			int s=count[ id ]+1;
			for(i=1;i<=n;i++)
				if( id!=i )if(s<count[i])count[i]=s;
			count[id]=100000;
		}
		
		if( q==0 ){
			printf("0\n");
		}
		else {
		int ans=1000000;
		for(i=1;i<=n;i++)
			if( id!=i && ans>count[i])ans=count[i];
		printf("%d\n",ans);
    }
	
	}
	return 0;
}
	
