#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("Boutput.in","w",stdout);
	
	int T,t,C,D,N,i,j,k,len;
	char com[40][4],opt[3],str[110],ans[110];
	int opp[30][30];
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		memset(opp,0,sizeof(opp));
		memset(ans,0,sizeof(ans));
		scanf("%d ",&C);
		for(i=1;i<=C;i++){
			scanf("%s",&com[i]);
		}
		scanf("%d ",&D);
		for(i=1;i<=D;i++){
			scanf("%s",&opt);
			opp[opt[0]-'A'][++(opp[opt[0]-'A'][0])]=opt[1]-'A';
			opp[opt[1]-'A'][++(opp[opt[1]-'A'][0])]=opt[0]-'A';
		}
		scanf("%d %s",&N,&str);
		for(len=0,i=0;i<N;i++){
			if(len==0){
				ans[len++]=str[i];continue;
			}
			for(j=1;j<=C;j++){
				if((com[j][0]==ans[len-1] && com[j][1]==str[i]) || (com[j][0]==str[i] && com[j][1]==ans[len-1]))break;
			}
			if(j<=C)ans[len-1]=com[j][2];
			else{
				for(j=0;j<len;j++){
					for(k=1;k<=opp[str[i]-'A'][0];k++){
						if(ans[j]==(opp[str[i]-'A'][k]+'A'))break;
					}
					if(k<=opp[str[i]-'A'][0])break;
				}
				if(j<len)len=0;
				else ans[len++]=str[i];
			}
		}
		ans[len]='\0';
		printf("Case #%d: [",t);
		for(i=0;i<len;i++){
			if(i!=len-1)printf("%c, ",ans[i]);
			else printf("%c",ans[i]);
		}
		printf("]\n");
	}
	
	return 0;
}
