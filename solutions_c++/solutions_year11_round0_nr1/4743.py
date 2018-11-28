#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int a_id[105],b_id[105];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,T,N,cas,a,b,ans,tmp,na,nb,ta,tb,pa,pb;
	char color[105][5];
	int id[105];
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++){
		scanf("%d",&N);
		a=1;
		b=1;
		ans=0;
		na=0;
		nb=0;
		ta=0;
		tb=0;
		pa=1;
		pb=1;
		for(i=0;i<N;i++){
			scanf("%s%d",color[i],&id[i]);
			if(color[i][0]=='O')
				a_id[na++]=id[i];
			else
				b_id[nb++]=id[i];
		}
		
		for(i=0;i<N;i++){
			if(color[i][0]=='O'){
				ta++;
				if(pa<id[i]){
					if(a>id[i]) a=id[i];
					tmp=id[i]-a+1;
					pa=id[i];
					a=id[i];				
				}else{
					
					if(a<id[i]) a=id[i];
					tmp = a-id[i]+1;
					pa=id[i];
					a=id[i];
					
				}
				
				if(tb<nb){
					if(b_id[tb]>=b){
						b = (b+tmp)> b_id[tb] ? b_id[tb]:b+tmp;
						
					}
					else
					b = (b-tmp)< b_id[tb] ? b_id[tb]:b-tmp;
				}
			}
			else{
				tb++;
				if(pb<id[i]){
					if(b>id[i]) b=id[i];
					tmp=id[i]-b+1;
					pb=id[i];
					b=id[i];				
				}else{
					if(pb>=id[i]){
						if(b<id[i]) b=id[i];
						tmp = b-id[i]+1;
						pb=id[i];
						b=id[i];
					}
				}
				if(ta<na){
					if(a_id[ta]>=a)
						a = (a+tmp)> a_id[ta] ? a_id[ta]:a+tmp;
					else
						a = (a-tmp)< a_id[ta] ? a_id[ta]:a-tmp;
				}
			}
			ans+=tmp;
		}
		
		printf("Case #%d: %d\n",cas,ans);
		
	}
	
}
