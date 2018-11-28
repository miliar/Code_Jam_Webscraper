#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stdlib.h>
using namespace std;
double totl[110];
int main(){
    int tmt,cas=1;
    scanf("%d",&tmt);
    while(tmt--){
	int x,s,r,n,i;
	double t;
	scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
	memset(totl,0,sizeof(totl));
	totl[0]=x;
	while(n--){
	    int a,b,c;
	    scanf("%d%d%d",&a,&b,&c);
	    totl[c]+=b-a;
	    totl[0]-=b-a;
	}
	double ans=0;
	for(i=0;i<=100;i++){
	    if(t==0){
		ans+=totl[i]/(i+s);
	    }else{
		double fr=totl[i]/(i+r);
		if(fr<t){
		    t-=fr;
		    ans+=fr;
		}else{
		    ans+=t+(totl[i]-t*(i+r))/(i+s);
		    t=0;
		}
	    }
	}
	printf("Case #%d: %.9lf\n",cas++,ans);
    }
}
