#include<iostream>

using namespace std;

double p[3];
double q[3];
double foundmin(int n ,double a[]){
	double max=9999999999;
	for(int i=0;i<n;i++){
		if(a[i]<max){
			max=a[i];
		}
	}
	return max;
}

int main(){
	freopen("A-small-attempt5.in","r",stdin);
	freopen("out.txt","w",stdout);
	int _t;
	scanf("%d",&_t);
	double temp[5];
	for(int __t=1;__t<=_t;__t++){
		double res;
		int a,b;
		scanf("%d%d",&a,&b);
		for(int i=0;i<a;i++){
			scanf("%lf",&p[i]);
			q[i]=1-p[i];
		}
		if(a==1){
			temp[0]=p[0]*(b-a+1)+(1-p[0])*(2*b-a+2);
			temp[1]=p[0]*(b-a+2)+(1-p[0])*(b+2);
			temp[2]=p[0]*(b+1)+(1-p[0])*(b+1);
			res=foundmin(3,temp);
		}
		else if(a==2){
			temp[0]=p[0]*p[1]*(b-a+1)+(p[0]*q[1]+q[0]*p[1]+q[1]*q[0])*(b-a+1+b+1);
			temp[1]=p[0]*p[1]*(b-a+3)+p[0]*q[1]*(1+b-(a-1)+1)+(q[0]*p[1]+q[0]*q[1])*(1+b-a+1+1+b+1);
			temp[2]=(p[0]*p[1]+p[0]*q[1]+q[0]*p[1]+q[0]*q[1])*(2+b+1);
			temp[3]=(p[0]*p[1]+p[0]*q[1]+q[0]*p[1]+q[0]*q[1])*(1+b+1);
			res=foundmin(4,temp);
		}
		else{
			temp[0]=((p[0]*p[1]+p[0]*q[1]+q[0]*p[1]+q[0]*q[1])*(q[2]+p[2])-p[0]*p[1]*p[2])*(b-a+1+b+1)+p[0]*p[1]*p[2]*(b-a+1);
			temp[1]=(p[0]*p[1])*(p[2]+q[2])*(2+b-a+1)+(p[0]*q[1]+q[0]*p[1]+q[0]*q[1])*(1+b-a+1+1+b+1)*(p[2]+q[2]);
			temp[2]=((p[0]*p[2]+p[0]*q[2]))*(p[1]+q[1])*(4+b-a+1)+(q[0]*p[2]+q[0]*q[2])*(2+b-a+2+1+b+1)*(p[1]+q[1]);
			temp[3]=(p[0]*p[1]+p[0]*q[1]+q[0]*p[1]+q[0]*q[1])*(q[2]+p[2])*(3+b+1);
			temp[4]=((p[0]*p[1]+p[0]*q[1]+q[0]*p[1]+q[0]*q[1])*(q[2]+p[2]))*(1+b+1);
			res=foundmin(5,temp);
		}
		printf("Case #%d: %.6lf\n",__t,res);
	}
	return 0;
}