#include<iostream>
#include<cstdio>

using namespace std;

float prob[100010];

int main(){
	int t,kase=1;
	scanf("%d",&t);
	while(t--){
		int a,b,i,fac_a=1,j;
		float op_key,key,joint;
		scanf("%d %d",&a,&b);
		for(i=0;i<a;i++)
		    scanf("%f",&prob[i]);
		op_key=b+2;
		if(a+b+1<op_key)
		    op_key=a+b+1;
		for(i=1;i<=a;i++){
			joint=1.0;
			for(j=0;j<i;j++){
				joint*=prob[j];
			}
			
			key=joint*(a+b-2*i+1)+(1-joint)*(a+b-2*i+1+b+1);
//			printf("%d: %f*%d %f*%d = %f\n",i,joint,a+b-2*i-1,1-joint,a+b-2*i-1+b+1,key);
			if(key<op_key)
			    op_key=key;
		}
		printf("Case #%d: %.6f\n",kase, op_key);
		kase++;
	}
	return 0;
}
