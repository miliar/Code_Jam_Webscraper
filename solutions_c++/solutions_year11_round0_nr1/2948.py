#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
#define ab(x) ((x)>0?(x):-(x))
int nimei[105],mlgb[105];
char s[5];
struct node{
	int myid,target;//myid=0 O myid=1 B
}arr[105];
int main(){
	int olen,blen,i,n,tttttxt,t=0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&tttttxt);
	while(tttttxt--){
		++t;
		scanf("%d",&n);
		olen=blen=0;
		for(i=0;i<n;++i){
			scanf("%s %d",s,&arr[i].target);
			if(s[0]=='O')
				arr[i].myid=0;
			else arr[i].myid=1;
			if(arr[i].myid==0)
				nimei[olen++]=arr[i].target;
			else mlgb[blen++]=arr[i].target;
		}
		int ans=0,ohead=0,bhead=0,os=1,bs=1,tmp;
		for(i=0;i<n;++i){
			if(arr[i].myid==0){//o
				tmp=ab(arr[i].target-os)+1;
				ans+=tmp;
				os=arr[i].target;
				ohead++;
				if(bhead<blen){
					if(ab(bs-mlgb[bhead])<=tmp)
						bs=mlgb[bhead];
					else{
						if(bs<mlgb[bhead])
							bs+=tmp;
						else bs-=tmp;
					}
				}
			}else{
				tmp=ab(arr[i].target-bs)+1;
				ans+=tmp;
				bs=arr[i].target;
				bhead++;
				if(ohead<olen){
					if(ab(os-nimei[ohead])<=tmp)
						os=nimei[ohead];
					else{
						if(os<nimei[ohead])
							os+=tmp;
						else os-=tmp;
					}
				}
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
