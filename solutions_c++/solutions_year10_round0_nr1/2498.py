#include<stdio.h>
//using namespace std;
int main()
{
   freopen("c:\\A-large.in","r",stdin);
    freopen("c:\\A-large.out","w",stdout);
    int t,n,k,cns=0,b;
    char str[2][4]={"ON","OFF"};
    scanf("%d",&t);
    while(t--){
		cns++;
		b=0;
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++){
		 if((!(k&(1<<i)))) {b=1;break ;}
}
		printf("Case #%d: %s\n",cns,str[b]);
	}
            
}
