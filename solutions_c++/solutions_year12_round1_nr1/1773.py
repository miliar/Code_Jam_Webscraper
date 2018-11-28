#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int t,a,b;
//a already typed
//b all
double ans=0,ans1=0,ans2=0;
double d[100000][3]; 
int back=0;
int dfs(int xx,int yy,double pp,int clear){
	if(xx>a){
		int tmp=0;
		tmp=back*2+b-a+1;
		if(clear<=a-back && clear!=0)tmp+=b+1;
		//printf("%d  %d\n",clear,tmp);
		ans1+=pp*tmp;
		return 0;
	}
	pp=pp*d[xx][yy];
	if(yy==1){
		if(clear==0)clear=xx;
		else if(clear>xx)clear=xx;
	}
	dfs(xx+1,0,pp,clear);
	dfs(xx+1,1,pp,clear);
}
int dfs1(int xx,int yy,double pp,int clear){
	if(xx>a){
		int tmp=b-a+1;
		if(clear)tmp+=b+1;
		
		ans+=pp*tmp;
		return 0;
	}
	pp=pp*d[xx][yy];
	if(yy==1){
		if(clear==0)clear=xx;
		else if(clear>xx)clear=xx;
	}
	dfs1(xx+1,0,pp,clear);
	dfs1(xx+1,1,pp,clear);
}


main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a.out","w",stdout);
	while(scanf("%d",&t)==1){
		for(int k=1;k<=t;k++){
			scanf("%d%d",&a,&b);
			for(int i=1;i<=a;i++){
				scanf("%lf",&d[i][0]);
				d[i][1]=1-d[i][0];
			}
			ans=ans1=0;
			ans2=b+2;
			
			for(int i=1;i<=a;i++){
				back=i;
				dfs(1,0,1,0);
				dfs(1,1,1,0);
				ans1=ans1/2;
				if(ans1<ans2)ans2=ans1;
				//printf("%lf\n",ans1);
				ans1=0;
			}
			dfs1(1,0,1,0);
			dfs1(1,1,1,0);
			ans=ans/2;
			if(ans<ans2)ans2=ans;
			ans=0;
			printf("Case #%d: %lf\n",k,ans2);
			
		}
	}
}
