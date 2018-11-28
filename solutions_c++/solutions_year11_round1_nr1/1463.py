#include<iostream> 
using namespace std;
int main(){
	int n,pd,pg,pd100,pg100;
	int t;
	cin>>t;
	for(int x=1;x<=t;++x){
		cin>>n>>pd>>pg;
		if( (pd<100 && pg==100) || (pd>0 && pg==0) ){
			printf("Case #%d: Broken\n",x);
			continue;
		}
		int t1,t2;
		t1=pd;t2=100;
		while((t1=t1%t2)&&(t2=t2%t1));
		pd/=(t1+t2);
		pd100=100/(t1+t2);
		t1=pg;t2=100;
		while((t1=t1%t2)&&(t2=t2%t1));
		pg/=(t1+t2);
		pg100=100/(t1+t2);
		if( pd100 > n)
			printf("Case #%d: Broken\n",x);
		else
			printf("Case #%d: Possible\n",x);
	}
}
