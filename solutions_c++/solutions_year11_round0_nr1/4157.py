#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
#define ab(x) ((x)>0?(x):-(x))
int oo[105],bb[105];
char s[5];
struct node{
	int id,tar;//id=0 O id=1 B
}a[105];
int main(){
	int olen,blen,i,n,txt,t=0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&txt);
	while(txt--){
		++t;
		scanf("%d",&n);
		olen=blen=0;
		for(i=0;i<n;++i){
			scanf("%s %d",s,&a[i].tar);
			if(s[0]=='O')
				a[i].id=0;
			else a[i].id=1;
			if(a[i].id==0)
				oo[olen++]=a[i].tar;
			else bb[blen++]=a[i].tar;
		}
		int ans=0,ohead=0,bhead=0,os=1,bs=1,tmp;
		for(i=0;i<n;++i){
			if(a[i].id==0){//o
				tmp=ab(a[i].tar-os)+1;
				ans+=tmp;
				os=a[i].tar;
				ohead++;
				if(bhead<blen){
					if(ab(bs-bb[bhead])<=tmp)
						bs=bb[bhead];
					else{
						if(bs<bb[bhead])
							bs+=tmp;
						else bs-=tmp;
					}
				}
			}else{
				tmp=ab(a[i].tar-bs)+1;
				ans+=tmp;
				bs=a[i].tar;
				bhead++;
				if(ohead<olen){
					if(ab(os-oo[ohead])<=tmp)
						os=oo[ohead];
					else{
						if(os<oo[ohead])
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
