#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;
double temp1[100003],temp2[100003],temp3[100003];
int main(){
        int n,A,B;
	double A1,A2,answer,A3;
        scanf("%d",&n);
        for(int tc=0;tc<n;tc++){
                answer=99999999;
                scanf("\n%d %d",&A,&B);
                temp1[0]=0;
		temp2[0]=1;
                for(int i=A;i>=1;i--){
                        scanf("%lf",&temp1[i]);
                        temp2[0]*=temp1[i];
                }
                temp3[0]=temp2[0];
                for(int i=1;i<=A;i++){
                        temp2[i]=((temp2[i-1]/(1-temp1[i-1]))*(1-temp1[i]))/temp1[i];
                        temp3[i]=temp3[i-1]+temp2[i];
                }
                
                A1=temp2[0]*(B-A+1)+(1-temp2[0])*(2*B-A+2);

		A2=B+2;
                if(A2<answer){
			answer=A2;
		}                

		if(A1<answer){
			answer=A1;
		}
                
                for(int i=1;i<=A;i++){
                        A3=(B-A+2*i+1)*(temp2[0]+temp3[i]-temp3[0])+(B-A+2*i+1+B+1)*(1-temp2[0]-temp3[i]+temp3[0]);
                        if(A3<answer){
				answer=A3;
			}
                }
                printf("Case #%d: %.6lf\n",tc+1,answer);
        }
        return 0;
}
