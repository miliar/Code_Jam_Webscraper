#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>

using namespace std;
int data[20][150],L,D,N,txt,res;
string in[5005];
char ch[26*20];
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int i,j,k,len;
	while(scanf("%d%d%d",&L,&D,&N)==3){
		for(i=1;i<=D;i++)cin>>in[i];
		while(N--){
			memset(data,0,sizeof(data));
			scanf("%s",ch);
			len=strlen(ch);
			for(i=1,j=0;i<=L;i++){
				if(j<len&&ch[j]!=')'&&ch[j]!='('){
					data[i][ch[j]]=1;
					j++;
					continue;
				}
				j++;
				while(j<len&&ch[j]!=')'){
					data[i][ch[j]]=1;
					j++;
				}
				if(j<len&&ch[j]==')')j++;
			}
			res=0;
			for(i=1;i<=D;i++){
				int lim=in[i].size();
				for(j=0;j<lim;j++){
					char c=in[i][j];
					if(data[j+1][c]==0)break;
				}
				if(j==lim)res++;
			}
			printf("Case #%d: %d\n",++txt,res);
		}
	}
	return 0;
}

