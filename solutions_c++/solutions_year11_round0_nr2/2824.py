#include <iostream>
#include <cstdio>
#include <stack>
#include <cstring>
using namespace std;
bool sssstat1[28][28];//combine
int ssssssstat2[28][28];//oppose
char s[105],com[6],opp[6];
int tar[55];
char ans[105];
int main()
{
	int txt,i,clen,olen,len,tarlen,top,j,tt=1;
//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);
	scanf("%d",&txt);
	while(txt--){
		memset(sssstat1,0,sizeof(sssstat1));
		memset(ssssssstat2,0,sizeof(ssssssstat2));
		top=0;
		scanf("%d",&clen);
		tarlen=1;
		for(i=0;i<clen;++i)
		{
			scanf("%s",com);
			ssssssstat2[com[0]-'A'][com[1]-'A']=ssssssstat2[com[1]-'A'][com[0]-'A']=tarlen;
			tar[tarlen++]=com[2]-'A';
		}
		scanf("%d",&olen);
		for(i=0;i<olen;++i)
		{
			scanf("%s",opp);
			sssstat1[opp[0]-'A'][opp[1]-'A']=sssstat1[opp[1]-'A'][opp[0]-'A']=1;
		}
		scanf("%d",&len);
		scanf("%s",s);
		ans[top++]=s[0];
		for(i=1;i<len;++i){
			if(ssssssstat2[s[i]-'A'][ans[top-1]-'A']!=0){
				ans[top-1]=tar[ssssssstat2[s[i]-'A'][ans[top-1]-'A']]+'A';
			}
			else if(sssstat1[s[i]-'A'][ans[top-1]-'A']!=0){//can't combine,can oppose
				top=0;
			}
			else{
				for(j=0;j<top;++j){
					if(sssstat1[s[i]-'A'][ans[j]-'A']!=0)
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
