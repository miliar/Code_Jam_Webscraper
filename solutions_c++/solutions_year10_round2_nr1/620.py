#include<iostream>
#include<cstdio>
#include<string>
#include<map>
#include<cstring>
using namespace std;

int main(void){
	freopen("C:\\a.in","r",stdin);
	freopen("C:\\a.out","w",stdout);
	int cs;
	scanf("%d",&cs);
	int ttt;
	for(ttt=1;ttt<=cs;ttt++){
		int n,m,t=1;
		scanf("%d%d",&n,&m);
		char ch[110][101];
		int i;
		map<string,int>mp;
		for(i=1;i<=n;i++){
			scanf("%s",&ch[i]);
			string str="";
			int j,len=strlen(ch[i]);
			for(j=1;j<len;j++){
				if(ch[i][j]=='/'){
					int tt=mp[str];
					if(tt==0){
						mp[str]=t++;
					}
				}
				str+=ch[i][j];
			}
			int tx=mp[str];
			if(tx==0) {
				mp[str]=t++;
			}
		}
		int ans=0;
		for(i=1;i<=m;i++){
			char sh[101];
			scanf("%s",sh);
			string ss="";
			for(int j=1;sh[j]!=0;j++){
				if(sh[j]=='/') {
					int tt=mp[ss];
					if(tt==0) {
						mp[ss]=t++;
						++ans;
					}
				}
				ss+=sh[j];
			}
			int tx=mp[ss];
			if(tx==0) {
				mp[ss]++;
				++ans;
			}
		}
		printf("Case #%d: %d\n",ttt,ans);
	}
	return 0;
}