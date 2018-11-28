#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<stack>
using namespace std;
int main(){
    int C,ccc,m,n,i,k;
    char pc[256][256],pd[256][256],cnt[256],s[256],c;
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&C);
	for(ccc=1;ccc<=C;++ccc){
		scanf("%d",&m);
		memset(pc,0,sizeof(pc));
		memset(pd,0,sizeof(pd));
		memset(cnt,0,sizeof(cnt));
		for(i=0;i<m;++i){
			scanf(" %s",s);
			pc[s[0]][s[1]]=s[2];
			pc[s[1]][s[0]]=s[2];
		}
		scanf("%d",&m);
		for(i=0;i<m;++i){
			scanf(" %s",s);
			pd[s[0]][++pd[s[0]][0]]=s[1];
			pd[s[1]][++pd[s[1]][0]]=s[0];
		}
		scanf("%d",&n);
		scanf("%s",s);
		stack<char> q;
		for(i=0;i<n;++i){
			c=s[i];
			while(!q.empty() && pc[c][q.top()]){
				c=pc[c][q.top()];
				--cnt[q.top()];
				q.pop();
			}
			k=1;
			for(char j=1;j<=pd[c][0];++j)
			  if(cnt[pd[c][j]]){
				do{
					--cnt[q.top()];
					q.pop();
				}while(!q.empty());
				k=0;break;
			}
			if(k){
				++cnt[c];
				q.push(c);
			}
		}
		k=0;
		while(!q.empty()){s[k++]=q.top();q.pop();}
		printf("Case #%d: [",ccc);
		if(k){
			printf("%c",s[--k]);
			for(i=k-1;i>=0;--i)printf(", %c",s[i]);
		}
		puts("]");
	}
	return 0;
}
