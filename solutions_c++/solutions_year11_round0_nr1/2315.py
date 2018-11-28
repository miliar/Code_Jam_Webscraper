#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cmath>
using namespace std;

int ans,ox,ot,bx,bt;

int main()
{
    int T;
	int cas=1;
	freopen("E:\\data\\A-small-attempt0.in","r",stdin);
	freopen("E:\\data\\outA1.txt","w",stdout);
	scanf("%d",&T);
	while(T--){
		int n,i;
		scanf("%d",&n);
		char op;
		int pos;
		ans=0;
		ot=bt=0;
		ox=bx=1;
		for(i=0;i<n;++i){
			getchar();
			scanf("%c %d",&op,&pos);

			if(op=='O'){
				if(abs(pos-ox)+1 > bt-ot){
					ans = ans + abs(pos-ox)+1-((bt-ot)<0?0:(bt-ot));
					ox=pos;
					ot=ans;
				}
				else{
					ans++;
					ox=pos;
					ot=ans;
				}
			}
			else{
				if(abs(pos-bx)+1 > ot-bt){
					ans = ans + abs(pos-bx)+1-((ot-bt)<0?0:(ot-bt));
					bx=pos;
					bt=ans;
				}
				else{
					ans++;
					bx=pos;
					bt=ans;
				}
			}
		}
		printf("Case #%d: %d\n",cas++,ans);
	}
    return 0;
}