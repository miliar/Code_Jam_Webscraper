
#include<stdio.h>
#include<string.h>
#include<queue>
#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t,g,r,k,n,i,j,tot,cnt,no=1;
    queue<int> q;
    scanf("%d",&t);
    while(t--){
	    scanf("%d%d%d",&r,&k,&n);
	    for(i=0;i<n;i++){
		    scanf("%d",&g);
		    q.push(g);
		}
		tot=cnt=j=0;
		while(r--){
  		    while(1){
                if(tot+q.front()>k||j>=n) break;
	 		    tot+=q.front();
	 		    //printf("%d ",q.front());
	 		    q.push(q.front());
	 		    q.pop();
	 		    j++;
	 		}
	 		//printf("tot=%d\n",tot);
	 		cnt+=tot;
	 		tot=j=0;
  		}
  		printf("Case #%d: %d\n",no++,cnt);
  		while(q.empty()!=true) q.pop();
	}
    //system("pause");
    return 0;
}
