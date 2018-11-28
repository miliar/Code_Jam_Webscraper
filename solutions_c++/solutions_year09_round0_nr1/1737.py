#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <vector>
#include <map>
using namespace std;

struct node {
	char word[18];
}dd[5005];

bool cmp(node a,node b){
	return strcmp(a.word,b.word)<0;
}
vector<char> ss[20],qq[20],dic[20];
map<char ,int>my[20],new_my[20];
int k,ans;
int n,D,L;


int main(){
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,J,len,ii;
	char tt[10005];
	scanf("%d%d%d",&L,&D,&n);
	for(i=0;i<L;i++)
		my[i].clear();
	for(i=0;i<D;i++){
		scanf("%s",dd[i].word);
		for(J=0;J<L;J++)
			dic[J].push_back(dd[i].word[J]);
	}
	
	for(i=1;i<=n;i++){
		scanf("%s",tt);
		len=strlen(tt);
		
		for(J=0;J<L;J++){
			ss[J].clear();
	
		}
		
		k=0;	
		ans=0;
		for(J=0;J<len;){
			if(tt[J]=='('){
				J++;
				while(tt[J]!=')'){
					ss[k].push_back(tt[J]);
				
					J++;
				}
				J++;
				k++;
			}
			else{
				ss[k].push_back(tt[J]);
				
				k++;
				J++;
			}
		}
		
		
		int JJ,f;
		for(ii=0;ii<D;ii++){
			for(J=0;J<L;J++){
				f=0;
				for(JJ=0;JJ<ss[J].size();JJ++){
					if(dic[J][ii]==ss[J][JJ]){
						f=1;
						break;
					}
				}
				if(!f) break;
			}
			if(J==L) ans++;
		}
		
		printf("Case #%d: %d\n",i,ans);
		
		
	}
}
	
	
