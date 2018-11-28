#include<stdio.h>
#include<math.h>
bool deng(double a){
if(a == (int)a)return true;
return false;
}
int main(){
	double i,n,p,g;
	int t= 0,num,ceshi;
	char *ch[2]={"Broken","Possible"};
	freopen("A-small-attempt3.in","r",stdin);
	freopen("a3.out","w",stdout);
	scanf("%d",&num);
	while(t++<num){
	scanf("%lf%lf%lf",&n,&p,&g);
	ceshi = 0;
	if(p!=100&&g==100);
	else if(p!=0&&g==0);
	else{
		p/=100.0,g/=100.0;
		for(i=1;i<=n;i++)
		if(deng(i*p)){
		ceshi = 1;
		break;
		}
	}
	printf("Case #%d: %s\n",t,ch[ceshi]);
	}

} 
