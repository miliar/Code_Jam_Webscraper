#include<stdio.h>
#include<math.h>

int main(){
    freopen("iny", "r", stdin);
    freopen("out", "w", stdout);
	int t,n;
	scanf("%d",&t);
	char str[10];
	int owei[110][2],bwei[110][2],on,bn,x;
	int Case=1;
	while(t--){
		scanf("%d",&n);
		on=bn=0;
		for(int i=0;i<n;i++){
			scanf("%s %d",str,&x);
			if(str[0]=='O'){
				owei[on][0]=x;
				owei[on++][1]=i;
			}
			else{
				bwei[bn][1]=i;
				bwei[bn++][0]=x;
			}
		}
		int time=0,onowwei=1,bnowwei=1,nowid=0,oid=0,bid=0;
		bool fr=false;

		while(1){
			fr=false;
			if(oid<on){
			if(onowwei!=owei[oid][0]){
				if(onowwei<owei[oid][0]){
					onowwei++;
				}
				else{
					onowwei--;
				}
			}
			else{
				if(nowid==owei[oid][1]){
					oid++;
					nowid++;
					fr=true;
				}
			}
			}
			if(bid<bn){
			if(bnowwei!=bwei[bid][0]){
				if(bnowwei<bwei[bid][0]){
					bnowwei++;
				}
				else{
					bnowwei--;
				}
			}
			else{
				if(nowid==bwei[bid][1]&&!fr){
					bid++;
					nowid++;
				}
			}
			}
			time++;
			if(nowid>=n)break;
		}
		printf("Case #%d: %d\n",Case++,time);
		
	}
	return 0;
}
