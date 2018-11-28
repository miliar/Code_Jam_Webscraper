#include <iostream>
#include <cstdio>
#include <stack>
#include <cstring>
using namespace std;
bool stat1[28][28];//combine
int stat2[28][28];//oppose
char s[105],com[6],opp[6];
int tar[55];
char ans[105];
int main()
{
	int txt,i,clen,olen,len,tarlen,top,j,tt=1;
//	freopen("B-small-attempt1.in","r",stdin);
//	freopen("B-small-attempt1.out","w",stdout);
	scanf("%d",&txt);
	while(txt--){
		memset(stat1,0,sizeof(stat1));
		memset(stat2,0,sizeof(stat2));
		top=0;
		scanf("%d",&clen);
		tarlen=1;
		for(i=0;i<clen;++i)
		{
			scanf("%s",com);
			stat2[com[0]-'A'][com[1]-'A']=stat2[com[1]-'A'][com[0]-'A']=tarlen;
			tar[tarlen++]=com[2]-'A';
		}
		scanf("%d",&olen);
		for(i=0;i<olen;++i)
		{
			scanf("%s",opp);
			stat1[opp[0]-'A'][opp[1]-'A']=stat1[opp[1]-'A'][opp[0]-'A']=1;
		}
		scanf("%d",&len);
		scanf("%s",s);
		ans[top++]=s[0];
		for(i=1;i<len;++i){
			if(stat2[s[i]-'A'][ans[top-1]-'A']!=0){
				ans[top-1]=tar[stat2[s[i]-'A'][ans[top-1]-'A']]+'A';
			}
			else if(stat1[s[i]-'A'][ans[top-1]-'A']!=0){//can't combine,can oppose
				top=0;
			}
			else{
				for(j=0;j<top;++j){
					if(stat1[s[i]-'A'][ans[j]-'A']!=0)
						break;
				}
				if(j<top)top=0;
				else{
					ans[top++]=s[i];
				}
			}
		}
		printf("Case #%d: [",tt++);
		for(i=0;i<top-1;++i){
			printf("%c, ",ans[i]);
		}
		if(top>0)
		printf("%c]\n",ans[i]);
		else printf("]\n");
	}
	return 0;
}
