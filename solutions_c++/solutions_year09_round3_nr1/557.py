#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string.h>
#include <map>
using namespace std;
map<char,int>my;

int main(){
	int ncase,i,ii,len;
	char tt[100];
	__int64 ss[100];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&ncase);
	for(ii=1;ii<=ncase;ii++){
		my.clear();
		scanf("%s",tt);
		len=strlen(tt);
		long long cnt=1;
		int f=0;
		for(i=0;i<len;i++){
			if(!my[tt[i]]){
				if(i>0&&!f){
					ss[i]=0;
					my[tt[i]]=-1;
					f=1;
				}
				else{
					ss[i]=cnt;
					my[tt[i]]=cnt++;
				}
			}
			else{
				if(my[tt[i]]==-1)
					ss[i]=0;
				else
					ss[i]=my[tt[i]];
			}
		}
		long long ans=0;
		for(i=0;i<len;i++){
			ans=ans*cnt+ss[i];
		}
		printf("Case #%d: %I64d\n",ii,ans);
	}

		
}
	
