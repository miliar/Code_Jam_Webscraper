//Magicka
#include <cstdio>
#include <cstring>

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int TST;
	scanf("%d",&TST);
	for(int tst=1;tst<=TST;++tst){
		int c,d,n;
		char CC[255][255];
		bool DD[255][255];
		char s[120],ans[120];
		int la=0;
		memset(CC,0,sizeof(CC));
		memset(DD,0,sizeof(DD));
		memset(s,0,sizeof(s));
		memset(ans,0,sizeof(ans));
		char ins[3];
		scanf("%d",&c);
		for(int cr=1;cr<=c;++cr){
			scanf("%s",ins);
			CC[ins[0]][ins[1]]=CC[ins[1]][ins[0]]=ins[2];
		}
		scanf("%d",&d);
		for(int dr=1;dr<=d;++dr){
			scanf("%s",ins);
			DD[ins[0]][ins[1]]=DD[ins[1]][ins[0]]=1;
		}
		scanf("%d %s",&n,s);
		for(int i=0;i<n;++i){
			ans[++la]=s[i];
			if(CC[ans[la]][ans[la-1]]){
				ans[la-1]=CC[ans[la]][ans[la-1]];
				--la;
			}
			for(int j=1;j<la;++j) if(DD[ans[j]][ans[la]]){ la=0; break; }
		}
		printf("Case #%d: [",tst);
		if(la){
			printf("%c",ans[1]);
			for(int i=2;i<=la;++i) printf(", %c",ans[i]);
		}
		printf("]\n");
	}
}
