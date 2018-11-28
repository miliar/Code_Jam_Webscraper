#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int main(){
	char tok[105][105];
	int z; scanf("%d",&z);
	for(int zz=1;zz<=z;zz++){
		int s, q;
		scanf("%d",&s);
		gets(tok[0]);
		for(int i=0;i<s;i++){
			gets(tok[i]);
//			puts(tok[i]);
		}
		scanf("%d",&q);
		char buf[10000];
		gets(buf);

		printf("Case #%d: ",zz);

		int id[q];
		for(int j=0;j<q;j++){
			gets(buf);
			if(strlen(buf) > 100)
				id[j]=s;
			else{
				int i=0;
				for(;i<s;i++) if(!strcmp(buf,tok[i])) break;
				id[j]=i;
			}
		}
/*		
		puts("");
		for(int j=0;j<q;j++)
			printf(" %d\n", id[j]);
		puts("");
*/		
		bool vis[s];
		int ans=-1;
		if(q==0) ans=0;
		for(int j=0;j<q;){
			int cnt=0;
			memset(vis,0,sizeof(vis));
//			printf("j=%d\n",j);
			int i;
			for(i=j;cnt<s && i<q;i++)
				if(id[i]<s){
					cnt+=!vis[id[i]], vis[id[i]]=1;
					if(cnt==s)	break;
				}
			ans++;
			j=i;
		}
		printf("%d\n",ans);
	}
	return 0;
}
