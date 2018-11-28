#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
using namespace std;
const int mD=5005,mL=20;
int L,D,N;
char d[mD][mL],s[30*mL];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d%d%d",&L,&D,&N);
	for(int i=0;i<D;i++)scanf("%s",d[i]);
	
	for(int Cn=1;Cn<=N;Cn++){
		bool fword[D];
		memset(fword,1,sizeof(fword));
		scanf("%s",s);
		int p=0;
		for(int i=0;i<L;i++){
			bool fchar[128]={};
			if(s[p]=='('){
				p++;
				while(s[p]!=')')fchar[s[p++]]=1;
				p++;
			}
			else fchar[s[p++]]=1;
			
			for(int j=0;j<D;j++)
				if(!fchar[d[j][i]])fword[j]=0;
		}
		int ans=0;
		for(int i=0;i<D;i++)
			if(fword[i])ans++;
		printf("Case #%d: ",Cn);
		printf("%d\n",ans);
	}
	return 0;
}
 
